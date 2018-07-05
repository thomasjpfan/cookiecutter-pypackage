{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}={% endfor %}

{{ cookiecutter.project_short_description }}. The documentation is hosted at `ReadTheDocs <https://{{ cookiecutter.github_repo }}.readthedocs.io/en/latest/>`_.

.. image:: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}.svg?style=shield
    :target: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}
    :alt: CI Status

{% if cookiecutter.coverage == 'coveralls' -%}
.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}/badge.svg
    :target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}
    :alt: Coveralls Status
{%- elif cookiecutter.coverage == 'codecov' -%}
.. image:: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.github_repo }}
    :alt: Codecov Status
{%- endif %}

Features
--------

- This is feature one


Installation
------------

You can install {{ cookiecutter.github_repo }} directly from pypi:

.. code-block:: bash

    pip install {{ cookiecutter.github_repo }}

Development
-----------

The development version can be installed by running ``make dev``. Then we can lint ``make lint`` and tests by running ``pytest``.
