# Makefile for easier installation and cleanup.
#
# Uses self-documenting macros from here:
# http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

PACKAGE=veld
VENV_DIR=/tmp/veld_venv/

.PHONY: help dist venv

.DEFAULT_GOAL := help

help:
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) |\
		 awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-15s\033[0m\
		 %s\n", $$1, $$2}'

################
# Installation #
################

.PHONY: install

install: dist ## Install for the current user using the default python command
	pip install --user ./dist/$(PACKAGE)-*.whl

################
# Distribution #
################

.PHONY: release dist

release: ## Make a release
	python make_release.py

dist: man ## Make Python source distribution
	python setup.py sdist bdist_wheel

###########
# Testing #
###########

.PHONY: test mypy

test: venv ## Run unit tests
	source $(VENV_DIR)/bin/activate && \
		python -m unittest discover -vv -s ./tests && \
		mypy --check-untyped-defs $(PACKAGE)

test_direct: ## Run unit tests directly (without virtualenv)
	pip install .[tests] && \
		python -m unittest discover -vv -f -s ./tests && \
		mypy --check-untyped-defs $(PACKAGE)

mypy: venv ## Run mypy
	source $(VENV_DIR)/bin/activate && \
	       	mypy --check-untyped-defs $(PACKAGE)

#################
# Documentation #
#################

.PHONY: man

man: ## Build documentation with Sphinx
	python setup.py build_manpages

clean_man: ## Clean up man pages
	rm -f man/*.1

#######################
# Virtual environment #
#######################

.PHONY: venv clean_venv

venv: $(VENV_DIR)/bin/activate

$(VENV_DIR)/bin/activate:
	test -d $(VENV_DIR) || python -m venv $(VENV_DIR)
	source $(VENV_DIR)/bin/activate && pip install -e .[dev]
	touch $(VENV_DIR)/bin/activate

clean_venv:
	rm -rf $(VENV_DIR)

############
# Clean up #
############

.PHONY: clean

clean: clean_venv ## Clean build dist and egg directories left after install
	rm -rf ./dist
	rm -rf ./build
	rm -rf ./$(PACKAGE).egg-info
	rm -rf ./cover
	rm -f MANIFEST
	rm -f ./$(PACKAGE)/*.so
	rm -f ./*_valgrind.log*
	find . -type f -iname '*.pyc' -delete
	find . -type d -name '__pycache__' -empty -delete
