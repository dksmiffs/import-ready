[![image](https://img.shields.io/github/license/dksmiffs/importable.svg)](https://github.com/dksmiffs/importable)
[![image](https://img.shields.io/github/release/dksmiffs/importable.svg)](https://github.com/dksmiffs/importable/releases)

importable demonstrate the pieces needed to publish an importable Python package to [TestPyPi][1].

## Publish Guidance
1. Follow [these steps][2] before installing Python packages.
1. Update version in setup.py per [semantic versioning][3] guidance.
1. Git commit, tag, & push all desired edits for release.
1. Create a new release in GitHub to mirror your new version.
1. [Generate distribution archives][4] for your package.
1. [Upload your package][5] to TestPyPi.

[1]: https://test.pypi.org/
[2]: https://packaging.python.org/tutorials/installing-packages/#requirements-for-installing-packages
[3]: https://semver.org/
[4]: https://packaging.python.org/tutorials/packaging-projects/#generating-distribution-archives
[5]: https://packaging.python.org/tutorials/packaging-projects/#uploading-the-distribution-archives
