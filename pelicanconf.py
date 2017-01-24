#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'HackerCorp'
SITENAME = u'Projets'
SITEURL = 'http://www.hackercorp.eu'
PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'fr'
BOOTSTRAP_NAVBAR_INVERSE = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
#LINKS = (('HacKerCorp', SITEURL),)#'Pelican', 'http://getpelican.com/'),
#         ('Python.org', 'http://python.org/'),
#         ('Jinja2', 'http://jinja.pocoo.org/'),
#         ('You can modify those links in your config file', '#'),)
SHOW_ARTICLE_AUTHOR = True
# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

THEME = 'pelican-bootstrap3'
PLUGIN_PATHS = ["plugins"]
PLUGINS = ['i18n_subsites', 'render_math', 'pelican-toc',]

# Version française de la variable
BY = 'Par'
LISTE = 'Liste des auteurs sur'
# mapping: language_code -> settings_overrides_dict
I18N_SUBSITES = {
    'en': {
        'SITENAME': 'Projects',
        'I18N_UNTRANSLATED_PAGES': 'remove',
        'I18N_UNTRANSLATED_ARTICLES': 'keep',
        # Version anglaise de la variable
        'BY' : 'By',
        'LISTE' : 'Authors on'
    }
}

TOC = {
    'TOC_HEADERS' : '^h[1-3]',
    # What headers should be included in the generated toc
    # Expected format is a regular expression

    'TOC_RUN' : 'true',
    # Default value for toc generation, if it does not evaluate
    # to 'true' no toc will be generated
}
