#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from os.path import exists

AUTHOR = u'Ben Lindsay'
SITENAME = u'Ben Lindsay'
OUTPUT_PATH = 'output/'
SITEURL = ''

# put articles (posts) in blog/
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
# we need to change the main index page now though...
INDEX_SAVE_AS = 'index.html'
INDEX_URL = ''
#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
CATEGORIES_URL = 'categories/'
CATEGORIES_SAVE_AS = 'categories/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
TAGS_URL = 'tag/'
TAGS_SAVE_AS = 'tag/index.html'
ARCHIVES_URL = 'archives/'
ARCHIVES_SAVE_AS = 'archives/index.html'
AUTHOR_SAVE_AS = ''
AUTHORS_SAVE_AS = ''

AVATAR = "images/profile.jpg"
ABOUT_ME = """
Hi! I'm Ben. I'm a PhD student at UPenn, data science enthusiast, and
co-founder of <a href="http://penndsg.com/">Penn Data Science Group</a>.
I enjoy hacking around with new tools and finding ways to automate things.
I am an avid Python user and a diehard Vim fan. I'll be graduating in 2019.
"""
ABOUT_ME_HEADER = ''

I18N_TEMPLATES_LANG = 'en'
JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

MARKUP = ('rst', 'md', 'ipynb')
# put pages in the root directory
PAGE_SAVE_AS = '{slug}/index.html'
PAGE_URL = '{slug}/'

PLUGIN_PATHS = ['plugins', '../pelican-plugins']
# https://github.com/getpelican/pelican-plugins/tree/master/liquid_tags#liquid-style-tags
PLUGINS = ['tag_cloud', 'render_math', 'liquid_tags.img', 'liquid_tags.video',
           'liquid_tags.youtube', 'liquid_tags.include_code',
           'liquid_tags.notebook', 'i18n_subsites']

STATIC_PATHS = ['js', 'css', 'images', 'CNAME', 'notebooks']

TAG_CLOUD_STEPS = 50
TAG_CLOUD_MAX_ITEMS = 20
TAG_CLOUD_SORTING = 'size'
TAG_CLOUD_BADGE = True

DISPLAY_PAGES_ON_MENU = False
DISPLAY_CATEGORIES_ON_MENU = False
USE_FOLDER_AS_CATEGORY = True
MENUITEMS = [('Blog', '/blog/'), ('Projects', '/projects/')]
THEME = '../pelican-themes/pelican-bootstrap3'

PATH = 'content'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

SOCIAL = (
    ('github', 'https://github.com/benlindsay'),
    ('linkedin', 'https://www.linkedin.com/in/benjlindsay/'),
    ('email', 'mailto:benjlindsay+website@gmail.com', 'envelope'),
    ('twitter', 'https://twitter.com/ben_j_lindsay'),
)

DISQUS_SITENAME = 'benlindsay'

DEFAULT_PAGINATION = 10

GOOGLE_ANALYTICS_ID = 'UA-71898636-1'
GOOGLE_ANALYTICS_SITENAME = 'auto'
