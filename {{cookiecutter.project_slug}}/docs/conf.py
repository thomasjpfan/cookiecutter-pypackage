#!/usr/bin/env python

import os
import sys
sys.path.insert(0, os.path.abspath('..'))


extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinx.ext.intersphinx']

intersphinx_mapping = {
    'python': ('https://docs.python.org/3', None),
}

templates_path = ['_templates']

source_suffix = '.rst'
master_doc = 'index'

project = u'{{ cookiecutter.project_name }}'
copyright = u"{% now 'local', '%Y' %}, {{ cookiecutter.full_name }}"
author = u"{{ cookiecutter.full_name }}"

with open('../VERSION', 'r') as f:
    release = f.read().strip()
    version = release.rsplit('.', 1)[0]

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = False

# HTML output theme
html_theme = 'sphinx_rtd_theme'

htmlhelp_basename = '{{ cookiecutter.project_slug }}doc'

# Latex
latex_elements = {}

latex_documents = [
    (master_doc, '{{ cookiecutter.project_slug }}.tex',
     u'{{ cookiecutter.project_name }} Documentation',
     u'{{ cookiecutter.full_name }}', 'manual'),
]

# Manual page output
man_pages = [
    (master_doc, '{{ cookiecutter.project_slug }}',
     u'{{ cookiecutter.project_name }} Documentation',
     [author], 1)
]

# Textinfo output
texinfo_documents = [
    (master_doc, '{{ cookiecutter.project_slug }}',
     u'{{ cookiecutter.project_name }} Documentation',
     author,
     '{{ cookiecutter.project_slug }}',
     'One line description of project.',
     'Miscellaneous'),
]
