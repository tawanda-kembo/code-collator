# Contributing to Code Collator

Thank you for your interest in contributing to Code Collator! Here are some guidelines to help you get started:

## Getting Started

1. Fork the repository and clone your fork.
2. Create a new branch from the `main` branch for your feature or fix.
3. Make your changes in the new branch.
4. Commit your changes with a meaningful commit message.
5. Push your changes to your fork.
6. Create a pull request (PR) from your forked repository to the main repository.

## Commit Messages

Please follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification for your commit messages. This helps in automating the versioning and changelog generation.

### Commit Message Format

Each commit message consists of a header, a body, and a footer. The header has a specific format that includes a type, an optional scope, and a subject.

#### Type

Must be one of the following:

- **feat**: A new feature
- **fix**: A bug fix
- **docs**: Documentation only changes
- **style**: Changes that do not affect the meaning of the code (white-space, formatting, missing semi-colons, etc)
- **refactor**: A code change that neither fixes a bug nor adds a feature
- **perf**: A code change that improves performance
- **test**: Adding missing or correcting existing tests
- **build**: Changes that affect the build system or external dependencies (example scopes: gulp, broccoli, npm)
- **ci**: Changes to our CI configuration files and scripts (example scopes: Travis, Circle, BrowserStack, SauceLabs)
- **chore**: Other changes that don't modify src or test files
- **revert**: Reverts a previous commit

#### Subject

The subject contains a succinct description of the change:

- Use the imperative, present tense: "change" not "changed" nor "changes"
- Do not capitalize the first letter
- Do not add a period (.) at the end

## Pull Request Process

1. Ensure that your code adheres to the project's coding standards.
2. Ensure that your code passes all tests.
3. Update the documentation as necessary.
4. Create a pull request from your branch to the `main` branch.
5. The pull request will be reviewed by one of the maintainers.
6. Once the pull request is approved, it will be merged into the `main` branch.
7. The version will be automatically updated if your commit messages adhere to the Conventional Commits specification and include a `feat`, `fix`, or other relevant types.

## License

By contributing to Code Collator, you agree that your contributions will be licensed under the MIT License.