.PHONY: dev test package clean lint docs

test:
	pytest --cov={{ cookiecutter.project_slug }}

lint:
	flake8 {{ cookiecutter.project_slug }} tests

dev:
	pip install -r requirements_dev.txt
	pip install -e .

package:
	python setup.py sdist
	python setup.py bdist_wheel

clean:
	rm -rf dist/*

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
