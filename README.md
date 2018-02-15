# Cookiecutter PyPackage

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for a Python package.

## Features

* [CircleCI](https://circleci.com): Ready for CircleCI Testing with different python versions
* [Coveralls](https://coveralls.io): Uses Coveralls for converge tracking
* [PyPI](https://pypi.python.org/pypi): Uses CircleCI to upload to PyPI

## Usage

Install the latest version of Cookiecutter

```bash
pip install -U cookiecutter
```

Generate a Python package project:

```bash
cookiecutter https://github.com/thomasjpfan/cookiecutter-pypackage.git
```

Then:

1. Create repo on github.
1. Add repo to CircleCi.
1. Add repo to Coveralls and add `COVERALLS_REPO_TOKEN` to CircleCI's environment variables.
1. Register on PyPI-Test and PyPI-live and upload with twine. Look at this [Tutorial](https://packaging.python.org/guides/using-testpypi/) for details.
1. Add `PYPI_USERNAME` and `PYPI_PASSWORD` to CircleCI.
1. Add the repo to [ReadTheDocs](https://readthedocs.io/) account and activate service hook.

## License

MIT
