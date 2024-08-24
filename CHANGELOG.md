# Changelog

## v0.15.0

* Update CHANGELOG.md for v0.14.0
* feat: Add option to exclude comments and docstrings from collated code
* feat: Add support for including/excluding comments and docstrings in code collation
* fix: Add missing imports and definitions to resolve flake8 errors
* feat: integrate collate.py functionality into code_collator/collate.py
* test: Add logging and stderr capture to test_main
* feat: Add comprehensive tests for Code Collator features
* fix: Resolve flake8 errors in tests/test_collate.py
* fix: Remove extra blank lines in tests/test_collate.py
* fix: Remove unused collate.py and output.md files
* fix: Improve import structure in test file
* fix: Rearrange imports to resolve flake8 errors
* fix: Rearrange imports to resolve flake8 E402 errors
* fix: Add comment to test file and use correct output file path in test_main
* fix: Update test_main function to use correct output file path
* fix: Improve comment handling in process_file_content function
* fix: Remove comments and docstrings from processed file content
* fix: Properly remove comments and docstrings when include_comments is False
* fix: Remove comments from output when include_comments is set to False
* fix: Update logging configuration to write to stdout instead of stderr
* fix: Remove single-line comments from processed content
* fix: Add parent directory to Python path in test file
* test: Reorder imports and add missing imports
* fix: Add parent directory to Python path in tests/test_collate.py
* chore: Add E402 to flake8 ignore list
* chore: Remove unused files
* Merge pull request #28 from tawanda-kembo/feat/toggle-include-comments

