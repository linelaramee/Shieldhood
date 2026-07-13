# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]
### Added
- GitHub Actions CI/CD workflow for automated testing and linting
- Support for multiple Python versions in CI
- Ruff linting integration

### Changed
- Improved README with new badges and clearer structure

### Fixed
- Minor improvements in test coverage and documentation

## [2.0.1] - 2026-07-12
### Added
- Full professional package structure with `pyproject.toml`
- DeepDecoder with Base64, Hex, ROT-N, Entropy detection
- Human Confirmation Gate
- Spending Policy Engine + Address Allowlist
- State Persistence for daily limits
- `.github` folder (ISSUE_TEMPLATE, PULL_REQUEST_TEMPLATE, FUNDING.yml)
- CITATION.cff, CODE_OF_CONDUCT.md, CONTRIBUTING.md, SECURITY.md
- Docker + docker-compose support
- Bankr.bot skill integration files (SKILL.md + catalog.json)

### Changed
- Significantly improved README with badges, roadmap, and examples
- Updated tests and example.py for Bankr.bot

### Security
- Enhanced multi-layer prompt injection protection

## [2.0.0] - 2026-07-12
### Added
- Initial public release to PyPI
- Core Shieldhood guard with Deep Multi-Layer Detection
- Recursive DeepDecoder
- Basic CLI commands for Bankr.bot

---

**Next planned (v2.2)**
- `/shieldhood status` command
- Detailed logging system
- More advanced evasion technique detection
