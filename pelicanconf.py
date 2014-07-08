#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Smith'
SITENAME = u'SmithEllis'
SITEURL = ''

THEME='pelican-themes/pelican-bootstrap3'

GOOGLE_ANALYTICS='UA-94703-1'
DISPLAY_CATEGORIES_ON_MENU = False

GITHUB_USER="smithellis"
GITHUB_SKIP_FORK = True
PATH = 'content'

TIMEZONE = 'US/Eastern'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Paul McLanahan', 'http://pmac.io/'),
         ('Blackcattips', 'http://blackcattips.com/'),
         ('Mike Mitchell', 'http://sirmitchell.com/'),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/smith_ellis'),
          ('linkedin', 'http://www.linkedin.com/in/smithellis/'),
          ('github', 'http://github.com/smithellis'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
