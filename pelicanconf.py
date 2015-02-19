#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
PLUGIN_PATHS = ['plugins/pelican-plugins']
PLUGINS = ['related_posts','sitemap']
AUTHOR = u'Smith Ellis'
SITENAME = u'A blog for Smith Ellis'
SITESUBTITLE = u'webdev, code, smith and such'
SITEURL = 'http://smithellis.com'

THEME='themes/pelican-bootstrap3'

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

# Limit the tag cloud
TAG_CLOUD_MAX_ITEMS=10

# Blogroll
LINKS = (('Paul McLanahan', 'http://pmac.io/'),
         ('Blackcattips', 'http://blackcattips.com/'),
         ('Mike Mitchell', 'http://sirmitchell.com/'),
         ('AwesomeAthens', "http://www.awesomeathens.com/"),
         ('Smith Ellis', "http://smithellis.com/"),
	 	 ('ThriftKid', "http://thriftkid.com"),)

# Social widget
SOCIAL = (('twitter', 'http://twitter.com/smith_ellis'),
          ('linkedin', 'http://www.linkedin.com/in/smithellis/'),
          ('github', 'http://github.com/smithellis'),)

DEFAULT_PAGINATION = 10

DISQUS_SITENAME='smithellisblog'

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#Lifted this from Paul McLanahan - lets see
#If I get friendly URLS

FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'
ARTICLE_EXCLUDES = ('pages', 'extra')
