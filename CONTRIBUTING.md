# Contributing to Shieldhood

Thank you for considering contributing to **Shieldhood**!  
We welcome contributions from the community to help make AI agents on Robinhood Chain more secure.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Reporting Bugs](#reporting-bugs)
- [Suggesting Features](#suggesting-features)
- [Development Setup](#development-setup)
- [Pull Request Guidelines](#pull-request-guidelines)

---

## Code of Conduct

We follow the [Contributor Covenant Code of Conduct](https://www.contributor-covenant.org/version/2/1/code_of_conduct/).  
Please be respectful, inclusive, and constructive.

---

## How to Contribute

### 1. Reporting Bugs

- Open an issue using the **Bug Report** template
- Include:
  - Shieldhood version (`shieldhood --version`)
  - Python version
  - Steps to reproduce
  - Expected vs actual behavior

### 2. Suggesting Features

- Open an issue using the **Feature Request** template
- Explain the problem you're trying to solve and why it's important

### 3. Submitting Code Changes

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Test your changes
5. Commit with clear messages
6. Push to your branch and open a Pull Request

---

## Development Setup

```bash
git clone https://github.com/0xPoyraz/Shieldhood.git
cd Shieldhood

# Install development dependencies
pip install -e .[dev]

# Install pre-commit hooks
pre-commit install
```

---

## Coding Standards

- **Code Formatter**: Black
- **Linter**: Ruff
- **Type Checking**: MyPy (optional)
- Follow PEP 8 guidelines

Run checks before committing:

```bash
# Format code
black .

# Lint code
ruff check .

# Run tests
pytest
```

---

## Pull Request Guidelines

- PR title should be clear and descriptive
- Link related issues (if any)
- Include description of changes
- Add tests if applicable
- Make sure all tests pass
- Update documentation if needed

---

## Thank You

Every contribution helps make Shieldhood better.  
Whether it's a bug report, documentation fix, or new feature — we appreciate your help!

---

**Questions?**  
Feel free to open an issue or contact [@0xPoyraz](https://x.com/0xPoyraz).

Happy contributing! 🛡️
```
