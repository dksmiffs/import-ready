[![image](https://img.shields.io/github/license/dksmiffs/import-ready.svg)](https://github.com/dksmiffs/import-ready)
[![image](https://img.shields.io/github/release/dksmiffs/import-ready.svg)](https://github.com/dksmiffs/import-ready/releases)
[![image](https://img.shields.io/travis/dksmiffs/import-ready.svg)](https://travis-ci.org/dksmiffs/import-ready)
[![image](https://img.shields.io/codecov/c/github/dksmiffs/import-ready.svg)](https://codecov.io/gh/dksmiffs/import-ready)
[![image](https://img.shields.io/codacy/grade/d02f4f80df0445738821c692f4bbe16f.svg)](https://app.codacy.com/project/dksmiffs/import-ready/dashboard)

Demonstrate the pieces needed to publish an importable Python package to [TestPyPI][1].  Inside _import-ready_ is a package called `huntsville_havoc` that divulges a couple of historical secrets that most diehard SPHL [Huntsville Havoc][6] fans don't know.

## Publish Guidance
Follow these general suggestions to publish your own Python package to TestPyPI:
1.  [Prepare your environment][2] before installing Python packages.
2.  Update version in setup.py per [semantic versioning][3] guidance.
3.  Git commit, tag, & push all desired edits for release.
4.  Create a new release in GitHub to mirror your new version.
5.  [Generate distribution archives][4] for your package.
6.  [Upload your package][5] to TestPyPI.

## Testing _import-ready_
_import-ready_ contains two types of tests, both contained under the top level `tests` directory:
1.  **Unit tests**:  These are development time (pre-publish) tests. Run as follows from the top level directory:
```bash
$ python -m pytest tests/local
```
2.  **Package tests**:  These are post-publish tests, importing _import-ready_ itself back from TestPyPI. Run as follows from the `tests/TestPyPI` directory in a clean venv:
```bash
$ python -m pip install -r requirements_TestPyPI.txt
$ python -m pytest
```

[1]: https://test.pypi.org/
[2]: https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages
[3]: https://semver.org/
[4]: https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
[5]: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives
[6]: http://huntsvillehavoc.com
