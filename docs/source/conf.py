# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
import sys

sys.path.insert(0, "/home/dev/src/prospero/client/structify/")

project = "Structify"
copyright = "2024, YMTM Inc."
author = "Alex Reichenbach & Ronak Gandhi"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    # "autoapi.extension",
    # "sphinx.ext.autosectionlabel",
    # "sphinx.ext.napoleon",
]

templates_path = ["/docs/_templates"]
pygments_style = "sphinx"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinxawesome_theme"
extensions += ["sphinxawesome_theme.highlighting", "sphinxcontrib.details.directive"]
html_title = "Structify"

autoapi_dirs = ["../../../"]
autoapi_options = [
    "members",
    "show-inheritance",
    "show-module-summary",
    "imported-members",  # This is the problematic option
    "undoc-members",
]


html_baseurl = "/docs/"
html_static_path = ["_static/"]
html_logo = "_static/webclip.png"
html_favicon = "_static/favicon.png"

html_js_files = ["/docs"]
