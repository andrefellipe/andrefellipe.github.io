#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Andre Fellipe'
SITEURL = 'https://andrefellipe.com'
SITENAME = u"Andre Fellipe"
SITETITLE = u'Andre Fellipe'
SITESUBTITLE = u'made on the internet'
SITEDESCRIPTION = "Andre's personal site"
SITELOGO = './images/badge.jpeg'
USER_LOGO_URL = './images/badge.jpeg'
RELATIVE_URLS = True
DISABLE_URL_HASH = True
PYGMENTS_STYLE = 'native'
BROWSER_COLOR = '#333333'

ROBOTS = 'index, follow'
PATH = 'content'

TIMEZONE = 'America/Recife'
DEFAULT_LANG = u'en'
OG_LOCALE = u'en_US.utf8'
LOCALE = u'en_US.utf8'
DATE_FORMATS = {
    'en': '%b %d, %Y',
}

MAIN_MENU = True
MENUITEMS = (
        ('Archives', '/archives.html'),
        ('Categories', '/categories.html'),)
HOME_HIDE_TAGS = True
DISPLAY_CATEGORIES_ON_MENU = True
DEFAULT_PAGINATION = 10

CC_LICENSE = {
    'name': 'Creative Commons Attribution-ShareAlike',
    'version': '4.0',
    'slug': 'by-sa'
}

COPYRIGHT_YEAR = 2018

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/andrefellipe/'),
        ('github', 'https://github.com/andrefellipe/'),
        ('envelope-o', 'mailto:andrefellipern@gmail.com'),
        )

STATIC_PATHS = ['images', 'extra']
ARTICLE_EXCLUDES = ['extra']
EXTRA_PATH_METADATA = {
        'extra/CNAME': {'path': 'CNAME'},
        'extra/favicon.ico': {'path': 'favicon.ico'},
}

USE_LESS = True

THEME = "./flex"

PLUGIN_PATHS = ["./plugins"]
PLUGINS = ['code_include']

DISQUS_SITENAME = "andrefellipe"
ADD_THIS_ID = 'ra-5ba05ddbeb328e87'
