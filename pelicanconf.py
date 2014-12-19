#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'FerraraLUG'
SITENAME = u'FerraraLUG'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
ARTICLE_URL = '{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

PAGE_PATHS = ['pages']
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'

ARTICLE_PATHS = ['posts']

STATIC_PATHS = ['static']
WITH_FUTURE_DATES = False
EXTRA_PATH_METADATA = {}
TIMEZONE = 'Europe/Rome'
FILENAME_METADATA='(?P<date>\d{4}-\d{2}-\d{2})_(?P<slug>.*)'

# Feed generation is usually not desired when developing
FEED_ATOM = None
FEED_MAX_ITEMS = 15
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social widget
SOCIAL = ()

DEFAULT_PAGINATION = 10
DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_TAGS_ON_SIDEBAR = False
# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False

# Blogroll
LINKS = ()

