COURSE_NAME = 'CS109A'

AUTHOR = 'Pavlos Protopapas, Kevin Rader'

SITEURL = 'https://harvard-iacs.github.io/2018-CS109A'

GITHUB = 'https://github.com/Harvard-IACS/2018-CS109A'

COLOR = '#8996A0'

MENUITEMS = [
    ('Syllabus', 'pages/syllabus.html'),
    ('Schedule', 'pages/schedule.html'),
    ('Materials', 'pages/materials.html'),
    ('Sections', 'category/sections.html')
]

PATH = 'content'

OUTPUT_PATH = 'docs'

TIMEZONE = 'EST'

DEFAULT_LANG = 'en'

FEED_ALL_ATOM = None

CATEGORY_FEED_ATOM = None

TRANSLATION_FEED_ATOM = None

AUTHOR_FEED_ATOM = None

AUTHOR_FEED_RSS = None

DEFAULT_PAGINATION = 10

DEFAULT_CATEGORY = 'pages'

AUTHORS_SAVE_AS = ''

CATEGORIES_SAVE_AS = ''

ARCHIVES_SAVE_AS = ''

ARTICLE_SAVE_AS = '{category}/{slug}/index.html'

ARTICLE_URL = '{category}/{slug}/'

AUTHOR_URL = ''

AUTHOR_SAVE_AS = ''

INDEX_SAVE_AS = 'pages/materials.html'

THEME_STATIC_DIR = 'style'

DELETE_OUTPUT_DIRECTORY = True

MARKUP = ['md', 'ipynb']

PLUGIN_PATHS = ['plugins']

PLUGINS = ['ipynb.markup', 'tipue_search']

IGNORE_FILES = ['.ipynb_checkpoints', 'README.md', "*.html"]

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

STATIC_PATHS = ['lectures', 'labs', 'homeworks', 'a-sections', 'sections', 'wiki', 'images', 'projects', 'slides', 'data']

DIRECT_TEMPLATES = ['index', 'category', 'tags', 'search']

import re

JINJA_FILTERS = {
    'original_content': lambda x: re.search(r"content/.*", x).group(0)
}

USE_FOLDER_AS_CATEGORY = False

CACHE_CONTENT = True

import logging

LOG_FILTER = [
    (logging.WARN, "Empty alt attribute for image %s in %s"),
    (logging.WARN, "Meta tag in file %s does not have a 'name' attribute, skipping. Attributes: content=%s")
]
