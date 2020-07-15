# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import os

import sphinx_py3doc_enhanced_theme

extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.doctest",
    "sphinx.ext.extlinks",
    "sphinx.ext.ifconfig",
    "sphinx.ext.napoleon",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
]
if os.getenv("SPELLCHECK"):
    extensions += ("sphinxcontrib.spelling",)
    spelling_show_suggestions = True
    spelling_lang = "en_US"

source_suffix = ".rst"
master_doc = "index"
project = "Docx Utils"
year = "2018"
author = "Laurent LAPORTE"
copyright = "{0}, {1}".format(year, author)
release = "0.2.0"
version = ".".join(release.split(".")[:2])  # 'major.minor'

pygments_style = "trac"
templates_path = ["."]
extlinks = {
    "issue": ("https://github.com/tantale/docx_utils/issues/%s", "#"),
    "pr": ("https://github.com/tantale/docx_utils/pull/%s", "PR #"),
}
html_theme = "sphinx_py3doc_enhanced_theme"
html_theme_path = [sphinx_py3doc_enhanced_theme.get_html_theme_path()]
html_theme_options = {"githuburl": "https://github.com/tantale/docx_utils/"}

html_use_smartypants = True
html_last_updated_fmt = "%b %d, %Y"
html_split_index = False
html_sidebars = {
    "**": ["searchbox.html", "globaltoc.html", "sourcelink.html"],
}
html_short_title = "%s-%s" % (project, version)
html_show_sourcelink = False
html_static_path = ["_static"]

napoleon_use_ivar = True
napoleon_use_rtype = False
napoleon_use_param = False

intersphinx_mapping = {"http://docs.python.org/": None}

linkcheck_ignore = []

# This value selects if automatically documented members are sorted alphabetical
# (value 'alphabetical'), by member type (value 'groupwise') or by source order
# (value 'bysource'). The default is alphabetical.
autodoc_member_order = "bysource"
