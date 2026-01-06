# Release 1.6.0

## General Changes

- Convert README from RST to Markdown format.
- Rename LICENSE to LICENSE.txt.
- Add Docker configuration files (Dockerfile, docker-compose.yaml).
- Add several PowerShell utility scripts for installation and setup.
- Update configuration files: .flake8, .gitattributes, .gitignore, .pre-commit-config.yaml, .readthedocs.yaml.
- Add .rstcheck.cfg configuration.

## GitHub Actions and Templates

- Remove discontinued workflows and issue templates.
- Rename dependabot.yml to dependabot.yaml.

## Testing

- Update tests for better compatibility with time_machine.

## Statistics

- **Branch Name:** hendrik/urs-315-feature-dateid-remove-discontinued-workflow
- **Files Changed:** 35
- **Insertions:** 1538
- **Deletions:** 940
- **Modified Files:**
  - .flake8
  - .gitattributes
  - .github/CODEOWNERS
  - .github/ISSUE_TEMPLATE/bugfix.md
  - .github/ISSUE_TEMPLATE/config.yaml
  - .github/ISSUE_TEMPLATE/enhancement.md
  - .github/ISSUE_TEMPLATE/hotfix.md
  - .github/ISSUE_TEMPLATE/release.md
  - .github/dependabot.yaml
  - .github/workflows/00-deployment-pipeline.yaml
  - .github/workflows/01-pre-commit-and-document-check.yaml
  - .github/workflows/03-ci.yaml
  - .github/workflows/04-build-and-publish-to-pypi.yaml
  - .gitignore
  - .pre-commit-config.yaml
  - .readthedocs.yaml
  - .rstcheck.cfg
  - CreateDbSqlScript.ps1
  - Dockerfile
  - Install.ps1
  - InstallDevEnv.ps1
  - LICENSE.txt
  - README.md
  - README.rst
  - ReleaseNotes.md
  - SetupDotEnv.ps1
  - SetupGitHubAccess.ps1
  - SetupPrivateRepoAccess.ps1
  - coverage.xml
  - docker-compose.yaml
  - docs/requirements_docs.txt
  - install.ps1
  - poetry.lock
  - pyproject.toml
  - tests/test_dateid.py

______________________________________________________________________

# Release 1.5.9

- Fix URL references in pyprject.toml
- Fix badges references in README

______________________________________________________________________

# Release 1.5.8

- Update ISSUE_TEMPLATE's
- Implement GitHub Reusable workflows.
- Remove unnecessary doc folder.
- Upgrade to support Python 13.1
- Update formatting configuration files
  - flake8
  - .gitattributes
  - .gitignore
  - .pre-commit-config.yaml
  - readthedocs.yaml
  - rstcheck.cfg
- Delete redundant files
  - Docker files
  - install.ps1
- Add utility scripts
  - InstallDevEnv.ps1
  - SetupDotEnv.ps1
  - SetupGitHubAccess.ps1
  - SetupPrivateRepoAccess.ps1
- Update time_machine in pytest
  - Add decorator
  - Removed duplicate test

______________________________________________________________________

# Release 1.5.7

- Cleaning up
  - 03-ci.yaml
  - dependabot.yaml
- Updated
  - .flake8
  - .gitignore
  - install.ps1
  - LICENSE
- Deleted
  - MANIFEST.IN
  - t.yaml

______________________________________________________________________

# Release 1.5.6

- Fix badges in README.rst
  - Maintenance
  - License

______________________________________________________________________

# Release 1.5.5

- Fix "Send Notice" to Workflow

______________________________________________________________________

# Release 1.5.4

- Fix "Send Notice" to Workflow

______________________________________________________________________

# Release 1.5.3

- Add "Send Notice" to Workflow

______________________________________________________________________

# Release 1.5.2

- Add Release to Workflow

______________________________________________________________________

# Release 1.5.1

- Add git merge to Workflow

______________________________________________________________________

# Release 1.5.0

## General Changes

- Update the ISSUE_TEMPLATE's
- Rename the Workflow files from .yml to .yaml
- Update the pre-commit hooks
- Fix the Workflows
- Fix the single quote's to double quote's
- Replace the CHANGES.md with ReleaseNotes.md
- Remove the MANIFEST.in file
- Adapt pyproject.toml with Poetry configurations.
