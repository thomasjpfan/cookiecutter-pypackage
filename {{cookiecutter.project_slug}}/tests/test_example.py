from {{cookiecutter.project_slug}}.add import add


def test_add():
    assert add(1, 2) == 3
