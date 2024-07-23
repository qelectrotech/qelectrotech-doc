import sys, os
sys.path.append('.')
#from links.link import *
#from links import *
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Qelectrotech'
copyright = '2024, QelectroTech Team'
author = 'Integrat-edCircuit'
release = ''

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx_copybutton',
    'sphinx.ext.extlinks',
    "sphinx_design"
]

templates_path = ['_templates']
exclude_patterns = []

pygments_style = 'monokai'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
html_css_files = ['custom.css']
html_logo = "_external/_images/logo.png" 
html_theme_options = {
    "sidebar_hide_name": True,
    "navigation_with_keys": True,
}