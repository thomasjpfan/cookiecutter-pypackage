"""Top-level package for {{ cookiecutter.project_name }}."""

from .__version__ import __version__

from .subtracter import Subtracter

__all__ = [__version__, Subtracter]
