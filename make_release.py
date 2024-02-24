#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Do-nothing script for making a release

This idea comes from here: 
https://blog.danslimmon.com/2019/07/15/do-nothing-scripting-the-key-to-gradual-automation/

Author: Gertjan van den Burg
Date: 2019-07-23

"""

import abc
import collections
import os
import re
import shutil
import subprocess
import sys
import tempfile
import webbrowser

from typing import Dict

import colorama

URLS = {
    "CI": "https://github.com/GjjvdBurg/Veld/actions",
    "tags": "https://github.com/GjjvdBurg/Veld/tags",
}
BRANCH_NAME = "main"
CHANGELOG_FILENAME = "CHANGELOG.md"
MAN_DIRECTORY = "./man"


def color_text(msg, color=None, style=None):
    colors = {
        "red": colorama.Fore.RED,
        "green": colorama.Fore.GREEN,
        "cyan": colorama.Fore.CYAN,
        "yellow": colorama.Fore.YELLOW,
        "magenta": colorama.Fore.MAGENTA,
        None: "",
    }
    styles = {
        "bright": colorama.Style.BRIGHT,
        "dim": colorama.Style.DIM,
        None: "",
    }
    pre = colors[color] + styles[style]
    post = colorama.Style.RESET_ALL
    return f"{pre}{msg}{post}"


def color_print(msg, color=None, style=None):
    print(color_text(msg, color=color, style=style))


def wait_for_enter():
    input(color_text("\nPress Enter to continue", style="dim"))
    print()


def get_package_name():
    with open("./setup.py", "r") as fp:
        nameline = next(
            (line.strip() for line in fp if line.startswith("NAME = ")), None
        )
        return nameline.split("=")[-1].strip().strip('"')


def get_package_version(pkgname):
    ctx = {}
    with open(f"{pkgname.lower()}/__version__.py", "r") as fp:
        exec(fp.read(), ctx)
    return ctx["__version__"]


def get_last_version_tag():
    output = ""
    with subprocess.Popen(
        "git tag -l", shell=True, stdout=subprocess.PIPE, text=True, bufsize=1
    ) as p:
        for line in p.stdout:
            output += line
    tags = output.rstrip().split()
    version_tags = [
        t for t in tags if re.match(r"v\d+\.\d+\.\d+", t) is not None
    ]
    versions = [v.lstrip(".") for v in version_tags]
    versions.sort()
    return versions[-1]


def get_last_release_candidate_tag(version: str):
    output = ""
    with subprocess.Popen(
        "git tag -l", shell=True, stdout=subprocess.PIPE, text=True, bufsize=1
    ) as p:
        for line in p.stdout:
            output += line
    tags = output.rstrip().split()
    version_tags = [
        t
        for t in tags
        if re.match(r"v" + version + r"-rc\.\d+", t) is not None
    ]
    versions = [v.lstrip(".") for v in version_tags]
    versions.sort()
    if not versions:
        return None
    return versions[-1]


def build_release_message(context) -> str:
    message = (
        f"{context['pkgname'].capitalize()} Release "
        f"{context['next_version']}"
    )
    message += "\n"
    message += context["changelog_update"]
    return message


class Step(metaclass=abc.ABCMeta):
    def pre(self, context):
        pass

    def post(self, context):
        wait_for_enter()

    def run(self, context):
        try:
            self.pre(context)
            self.action(context)
            self.post(context)
        except KeyboardInterrupt:
            color_print("\nInterrupted.", color="red")
            raise SystemExit(1)

    def instruct(self, msg):
        color_print(msg, color="green")

    def print_command(self, msg):
        color_print("Run:", color="cyan", style="bright")
        color_print("\t" + msg, color="cyan", style="bright")

    def system(self, cmd: str):
        os.system(cmd)

    def execute(
        self, cmd: str, silent: bool = False, confirm: bool = True
    ) -> str:
        if not silent:
            color_print(f"Running: {cmd}", color="magenta", style="bright")
        if confirm:
            wait_for_enter()
        stdout = ""
        with subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            text=True,
            bufsize=1,
        ) as p:
            for line in p.stdout:
                stdout += line
                if not silent:
                    print(line, end="")
        if p.returncode:
            raise subprocess.CalledProcessError(
                p.returncode, p.args, stdout, p.stderr
            )
        return stdout.rstrip()

    @abc.abstractmethod
    def action(self, context):
        """Action to perform for the step"""


class GitToMain(Step):
    def action(self, context):
        self.instruct(f"Ensuring that you're on the {BRANCH_NAME} branch")
        branch = self.execute(
            "git rev-parse --abbrev-ref HEAD", silent=True, confirm=False
        )
        if not branch == BRANCH_NAME:
            print(f"ERROR: not on {BRANCH_NAME} branch.", file=sys.stderr)
            raise SystemExit(1)

    def post(self, context):
        print("")


class UpdateChangelog(Step):
    _nice_name = {
        "feat": "Features",
        "docs": "Documentation",
        "style": "Code style",
        "build": "Build",
        "test": "Testing",
        "other": "Other",
    }
    _type_sort = ["feat", "test", "docs", "build", "style", "other"]

    def action(self, context):
        self.instruct(
            f"Updating change log for version {context['next_version']}"
        )
        context["changelog_update"] = self.get_changelog_section(context)
        self.update_changelog(context)

    def get_changelog_section(self, context: Dict[str, str]) -> str:
        next_version = context["next_version"]
        prev_version_tag = context["prev_version_tag"]
        commits = self.execute(
            f"git log --pretty=oneline {prev_version_tag}..HEAD | cut -d' ' -f2-",
            silent=True,
            confirm=False,
        )
        commits = commits.split("\n")
        commits.sort()
        by_type = collections.defaultdict(list)
        for commit in commits:
            if ":" not in commit:
                ctype = "other"
                msg = commit
            else:
                ctype, msg = commit.split(":", maxsplit=1)
            if ctype not in self._nice_name:
                ctype = "other"
                msg = commit
            by_type[ctype].append(msg.strip())

        ctypes = sorted(by_type.keys(), key=lambda k: self._type_sort.index(k))

        text = ["", f"## Version {next_version}", ""]
        for ctype in ctypes:
            text.append(f"* {self._nice_name[ctype]}")
            for msg in by_type[ctype]:
                text.append(f"  - {msg.capitalize()}")
        return "\n".join(text)

    def update_changelog(self, context: Dict[str, str]) -> None:
        with open(CHANGELOG_FILENAME, "r") as fp:
            with open(CHANGELOG_FILENAME + ".tmp", "w") as op:
                op.write(fp.readline())
                op.write(context["changelog_update"])
                op.write("\n")
                for line in fp:
                    op.write(line)
        shutil.move(CHANGELOG_FILENAME, CHANGELOG_FILENAME + ".bak")
        shutil.move(CHANGELOG_FILENAME + ".tmp", CHANGELOG_FILENAME)


class UpdateReadme(Step):
    def action(self, context):
        self.instruct("Update readme if necessary")
        self.print_command("vi README.md")


class RunTests(Step):
    def action(self, context):
        self.instruct("Run the unit tests")
        self.execute("make test && make mypy")


class BumpVersionPackage(Step):
    def action(self, context):
        self.instruct("Update __version__.py with new version")
        self.system(f"vi {context['pkgname']}/__version__.py")

    def post(self, context):
        wait_for_enter()
        context["next_version"] = get_package_version(context["pkgname"])


class MakeClean(Step):
    def action(self, context):
        self.execute("make clean")


class MakeDocs(Step):
    def action(self, context):
        self.execute("make docs")


class MakeMan(Step):
    def action(self, context):
        self.execute("make man")


class MakeDist(Step):
    def action(self, context):
        self.execute("make dist")


class PushToTestPyPI(Step):
    def action(self, context):
        self.system(
            "twine upload --repository-url https://test.pypi.org/legacy/ dist/*"
        )


class InstallFromTestPyPI(Step):
    def action(self, context):
        tmpvenv = tempfile.mkdtemp(prefix="veld_venv_")
        self.execute(
            f"python -m venv {tmpvenv} && source {tmpvenv}/bin/activate && "
            "pip install --no-cache-dir --index-url "
            "https://test.pypi.org/simple/ "
            "--extra-index-url https://pypi.org/simple "
            f"{context['pkgname']}=={context['next_version']}"
        )
        context["tmpvenv"] = tmpvenv


class TestPackage(Step):
    def action(self, context):
        self.instruct(
            f"Ensuring that the package has version {context['next_version']}"
        )
        version = self.execute(
            f"source {context['tmpvenv']}/bin/activate && veld -V",
            silent=True,
            confirm=False,
        )
        if not version == context["next_version"]:
            print(
                "ERROR: version installed from TestPyPI doesn't match "
                "expected version."
            )

    def post(self, context):
        print("")


class RemoveVenv(Step):
    def action(self, context):
        self.execute(
            f"rm -rf {context['tmpvenv']}", confirm=False, silent=True
        )

    def post(self, context):
        print("")


class GitTagVersion(Step):
    def action(self, context):
        tag_message = build_release_message(context)
        with open("./tag_message.tmp", "w") as fileobj:
            fileobj.write(tag_message)
        self.instruct("Going to tag with the following message:")
        print("--- BEGIN TAG MESSAGE ---")
        print(tag_message)
        print("--- END TAG MESSAGE ---")
        self.execute(
            f"git tag -F ./tag_message.tmp v{context['next_version']}"
        )
        os.unlink("./tag_message.tmp")


class GitTagPreRelease(Step):
    def action(self, context):
        last_rc_tag = get_last_release_candidate_tag(context["next_version"])
        rc_count = (
            1 if last_rc_tag is None else int(last_rc_tag.split(".")[-1]) + 1
        )
        context["rc_count"] = rc_count
        self.instruct("Tagging version as a pre-release (increment as needed)")
        self.execute(
            f"git tag -m \"{context['pkgname'].capitalize()} Release v"
            f"{context['next_version']} (release candidate {rc_count})\" v"
            f"{context['next_version']}-rc.{rc_count}"
        )


class GitAdd(Step):
    def action(self, context):
        self.instruct("Commit any final changes for release to git")
        self.print_command("git gui")


class GitAddVersionAndMan(Step):
    def action(self, context):
        self.instruct("Add version and man pages to git and commit")
        self.execute(
            f"git add {context['pkgname']}/__version__.py", confirm=False
        )
        self.execute(f"git add {MAN_DIRECTORY}", confirm=False)
        self.execute("git commit -m 'Bump version and update manpages'")


class GitAddRelease(Step):
    def action(self, context):
        self.instruct("Add Changelog & Readme to git")
        self.execute("git add CHANGELOG.md", confirm=False)
        self.execute("git add README.md", confirm=False)
        self.instruct("Going to commit with the following message:")

        commit_message = build_release_message(context)
        print("--- BEGIN COMMIT MESSAGE ---")
        print(commit_message)
        print("--- END COMMIT MESSAGE ---")
        with open("./commit_message.tmp", "w") as fileobj:
            fileobj.write(commit_message)
        self.execute("git commit --file ./commit_message.tmp")
        os.unlink("./commit_message.tmp")


class PushToPyPI(Step):
    def action(self, context):
        self.system("twine upload dist/*")


class PushToGitHub(Step):
    def action(self, context):
        self.execute(f"git push -u --tags origin {BRANCH_NAME}")


class WaitForCI(Step):
    def action(self, context):
        webbrowser.open(URLS["CI"])
        self.instruct("Wait for CI to complete and verify that its successful")


class GitHubRelease(Step):
    def action(self, context):
        webbrowser.open(URLS["tags"])
        self.instruct("Create release from tag and embed release notes")


def main(target=None):
    colorama.init()
    procedure = [
        ("gittomain", GitToMain()),
        ("clean1", MakeClean()),
        ("runtests", RunTests()),
        ("gitadd1", GitAdd()),
        # trigger CI to run tests on all platforms
        ("push1", PushToGitHub()),
        ("ci1", WaitForCI()),
        # ("waitrtd", WaitForRTD()), # TODO
        ("bumpversion", BumpVersionPackage()),
        ("clean2", MakeClean()),
        ("man1", MakeMan()),
        # ("docs2", MakeDocs()), # TODO
        ("gitadd2", GitAddVersionAndMan()),
        ("gittagpre", GitTagPreRelease()),
        # triggers Github Actions to build dists and push to TestPyPI
        ("push2", PushToGitHub()),
        ("ci2", WaitForCI()),
        ("install", InstallFromTestPyPI()),
        ("testpkg", TestPackage()),
        ("remove_venv", RemoveVenv()),
        ("changelog", UpdateChangelog()),
        ("readme", UpdateReadme()),
        ("addrelease", GitAddRelease()),
        ("tagfinal", GitTagVersion()),
        # triggers Github Actions to build dists and push to PyPI
        ("push3", PushToGitHub()),
        ("ci3", WaitForCI()),
    ]
    context = {}
    context["pkgname"] = get_package_name()
    context["prev_version_tag"] = get_last_version_tag()
    context["next_version"] = get_package_version(context["pkgname"])
    skip = True if target else False
    for name, step in procedure:
        if not name == target and skip:
            continue
        skip = False
        print(f"Running step: {name}")
        step.run(context)
    color_print("\nDone!", color="yellow", style="bright")


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else None
    main(target=target)
