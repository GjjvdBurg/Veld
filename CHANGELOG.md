# Changelog

## Version 0.1.5

* Features
  - Add reversal options to frequency command
  - Handle mixed data types in barcount
* Fixes
  - Handle scientific number notation
* Continuous Integration
  - Update github release workflow

## Version 0.1.4

* Features
  - Add frequency command
  - Add modulo command
  - Add pass-through command
  - Add product command
  - Add summary command
  - Add basic math operators
  - Add support for non-numeric values in some commands
  - Support non-numeric values in barcount
* Fixes
  - Checkout code in build action
  - Make test dir importable
  - Quotation marks in release workflow
  - Use urls without variables
* Testing
  - Rewrite cumsum test
  - Add unit tests for trimmed mean
* Documentation
  - Minor documentation and testing updates
* Build
  - Explicitly specify numpy dependency
  - Various changes to release script
* Continuous Integration
  - Add release workflow with trusted publishers
  - Updates to release script
  - Take release notes from tag
  - Various improvements to release script
* Code style
  - Code formatting
  - Update linters

## Version 0.1.3

* Features
  - Add paired t-test command
* Testing
  - Add missing main for cumsum unittest
  - Remove unnecessary unlinks
* Documentation
  - Format command list by group in manpage
  - Minor readme updates
  - Add additional documentation to veld man page
  - Add badges to readme
  - Add chaining example to readme
* Build
  - Add commitizen pre-commit configuration
  - Automate some steps of the release process
* Code style
  - Simplify comparison operator implementation
  - Use hyphen for multi-word commands

## Version 0.1.2

* Add round command
* Add line plot command

## Version 0.1.1

* Added numerous commands
* Added unit tests

## Version 0.1.0

* Initial release
