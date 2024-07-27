# Code Collator

Code Collator is a powerful CLI tool designed to streamline your code review and documentation process by collating your entire codebase into a single, organised Markdown file. This is particularly useful for sharing with AI tools like ChatGPT or Claude for analysis, troubleshooting, or documentation.

## Use Case

Have you ever needed to provide a comprehensive overview of your codebase for a code review, AI analysis, or detailed documentation? Code Collator simplifies this task by aggregating all your code files into a single Markdown file. This makes it easy to:
- Share your code with AI tools like ChatGPT or Claude for intelligent analysis.
- Generate a unified document for code reviews or team collaboration.
- Create comprehensive documentation for your projects with minimal effort.

## Features
- **Full Codebase Collation**: Collates all files in the specified directory and subdirectories into one Markdown file.
- **.gitignore Support**: Automatically ignores files specified in the `.gitignore` file if one exists.
- **Customizable Output**: Outputs a single Markdown file named `collated-code.md` by default, with options to specify the path to the codebase directory and output file name.
- **Binary File Inclusion**: Includes binary files such as images in the output with a note about their file type.
- **Help Command**: Provides a help command to display usage instructions.

## Installation

You can easily install Code Collator using pip:

```sh
pip install code-collator
```

## Usage

Here’s a basic example of how to use Code Collator:

```sh
code-collator --path /path/to/codebase --output my-collated-code.md
```

For more detailed usage instructions, use the help command:

```sh
code-collator --help
```



## Running Tests

To run the tests locally:

```sh
pytest tests/
```

To run tests with coverage:

```sh
pytest tests/ --cov=code_collator --cov-report=term-missing
```

## Linting

To run the linter:

```sh
flake8 code_collator/ tests/
```

Automatically fix many style issues:

```sh
autopep8 --in-place --aggressive --aggressive -r code_collator/ tests/
```

To check for linting issues:

```bash
python setup.py lint
```

To automatically fix many linting issues:

```sh
python setup.py lint --fix
```

## Contributing

Please see CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE file for details.