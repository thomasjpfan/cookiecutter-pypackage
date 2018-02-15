{{ cookiecutter.project_name }}
{% for _ in cookiecutter.project_name %}*{% endfor %}


.. image:: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}.svg?style=shield
    :target: https://circleci.com/gh/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
    :alt: CI Status

.. image:: https://coveralls.io/repos/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}/badge.svg
:target: https://coveralls.io/github/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}

{{ cookiecutter.project_short_description }}


Features
--------

* This is feature one

Installation
------------

.. code-block:: bash

    pip install git+https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}


Development
-----------

The development version can be installed by:

.. code-block:: bash

    git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}
    cd {{ cookiecutter.project_slug }}
    make dev

Then we can lint ``make lint`` and tests by running ``make test``.
