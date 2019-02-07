[![image](https://img.shields.io/github/license/dksmiffs/importable.svg)](https://github.com/dksmiffs/importable)
[![image](https://img.shields.io/github/release/dksmiffs/importable.svg)](https://github.com/dksmiffs/importable/releases)
[![image](https://img.shields.io/travis/dksmiffs/importable.svg)](https://travis-ci.org/dksmiffs/importable)
[![image](https://img.shields.io/codecov/c/github/dksmiffs/importable.svg)](https://codecov.io/gh/dksmiffs/importable)
[![image](https://img.shields.io/codacy/grade/d02f4f80df0445738821c692f4bbe16f.svg)](https://app.codacy.com/project/dksmiffs/importable/dashboard)

Demonstrate the pieces needed to publish an importable Python package to [TestPyPi][1].  Inside importable is a package called 'huntsville\_havoc' that divulges a couple of historical secrets that most diehard SPHL [Huntsville Havoc][6] fans don't know.

## Publish Guidance
1.  Follow [these steps][2] before installing Python packages.
2.  Update version in setup.py per [semantic versioning][3] guidance.
3.  Git commit, tag, & push all desired edits for release.
4.  Create a new release in GitHub to mirror your new version.
5.  [Generate distribution archives][4] for your package.
6.  [Upload your package][5] to TestPyPi.

## Testing
1.  'origins\_test.py' file under 'huntsville\_havoc' demonstrates package developer/internal unit testing, using pytest.
2.  The top level 'tests' directory demonstrates external usage of this package via TestPyPi, again using pytest.

[1]: https://test.pypi.org/
[2]: https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages
[3]: https://semver.org/
[4]: https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
[5]: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives
[6]: http://huntsvillehavoc.com
