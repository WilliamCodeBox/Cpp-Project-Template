# Configuration file for the Sphinx documentation builder.

# -- Theme information -----------------------------------------------------

import os
# on_rtd is whether we are on readthedocs.org, this line of code grabbed from docs.readthedocs.org
on_rtd = os.environ.get('READTHEDOCS', None) == 'True'
if not on_rtd:  # only import and set the theme if we're building docs locally
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import json
from datetime import date

currentYear = str(date.today().year)

with open("./config.json", "r") as configFile:
    config = json.load(configFile)

    # -- Project information -----------------------------------------------------
    project = config["ProjectConfig"]["project-name"]
    author = config["ProjectConfig"]["author"]
    copyright = currentYear + ", " + author
    release = config["ProjectConfig"]["release"]

    # -- Doc information -----------------------------------------------------
    sourceDir = config["DocConfig"][
        "sourceDir"]  # source files you want to be documented
    docOutputDir = "./api"  # Warning: if you change `docOutputDir`, you have to change `index.rst` accordingly
    rootFileTitle = "Library API"
    configFile.close()

currentTime = str(date.today())
rst_str = f""".. {project} documentation master file, created on {currentTime}.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to {project}'s documentation!
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api/library_root

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
"""

with open("./index.rst", "w") as rstFile:
    rstFile.writelines(rst_str)
    rstFile.close()
# -- General configuration ---------------------------------------------------

extensions = [
    # there may be others here already, e.g. 'sphinx.ext.mathjax'
    'breathe',
    'exhale'
]

# Setup the breathe extension
breathe_projects = {"My Project": "./doxyoutput/xml"}
breathe_default_project = "My Project"


# somewhere in `conf.py`, *BERORE* declaring `exhale_args`
def specificationsForKind(kind):
    '''
    For a given input ``kind``, return the list of reStructuredText specifications
    for the associated Breathe directive.
    '''
    # Change the defaults for .. doxygenclass:: and .. doxygenstruct::
    if kind == "class" or kind == "struct":
        return [
            ":members:", ":protected-members:", ":private-members:",
            ":undoc-members:"
        ]
    # Change the defaults for .. doxygenenum::
    elif kind == "enum":
        return [":no-link:"]
    # An empty list signals to Exhale to use the defaults
    else:
        return []


# Use exhale's utility function to transform `specificationsForKind`
# defined above into something Exhale can use
from exhale import utils
# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":
    docOutputDir,
    "rootFileName":
    "library_root.rst",
    "rootFileTitle":
    rootFileTitle,
    "doxygenStripFromPath":
    "..",
    # Suggested optional arguments
    "createTreeView":
    True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen":
    True,
    "exhaleDoxygenStdin":
    "INPUT = " + sourceDir,
    "customSpecificationsMapping":
    utils.makeCustomSpecificationsMapping(specificationsForKind)
}

# Tell sphinx what the primary language being documented is.
primary_domain = 'cpp'

# Tell sphinx what the pygments highlight language should be.
highlight_language = 'cpp'

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']