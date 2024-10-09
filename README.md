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
- **Comment Exclusion Option**: Allows users to exclude comments and docstrings from the collated code.
- **Help Command**: Provides a help command to display usage instructions.

## Demo Video

[![Watch the demo video](https://img.youtube.com/vi/e8Ep_NOi_xU/0.jpg)](https://youtu.be/e8Ep_NOi_xU)

*Click the image above to watch a hands-on demo of how Code Collator works.*

## Installation

You can easily install Code Collator using pip:

```sh
pip install code-collator
