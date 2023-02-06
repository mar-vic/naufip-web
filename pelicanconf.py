#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'naufip'
SITENAME = u'NAUFIP'
SITESUBTITLE = u'Naturalizmus ako univerzálny filozofický program'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Bratislava'

DEFAULT_LANG = u'sk'

DEFAULT_DATE_FORMAT = '%d-%m-%Y'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

THEME = 'themes/naufip-sk'

# Gallery configuration
PHOTO_LIBRARY = "./photos"
PHOTO_GALLERY = (1024, 768, 80)
PHOTO_ARTICLE = (760, 506, 80)
PHOTO_THUMB = (192, 144, 60)
PHOTO_SQUARE_THUMB = False
PHOTO_RESIZE_JOB = 5
# GALLERY_PATH = "./images/gallery"
# IMAGE_PATH = "./images"
# THUMBNAIL_DIR = "./images"
# THUMBNAIL_KEEP_NAME = True
# THUMBNAIL_KEEP_TREE = True

# RESIZE = [
#             ('gallery', False, 200,200),
#           ]

HEADER_IMAG = "science_cropped.jpg"

MENUITEMS = [('Domov','/'),
             ('O projekte','/pages/o-projekte.html'),
             ('Riešiteľský kolektív','/pages/riesitelsky-kolektiv.html'),
             ('Aktivity', '/category/activities.html'),
              # '/pages/aktivity.html'),
             ('Výstupy','/pages/vystupy.html')
             # ('Médiá','/category/media.html')
             # ('EN','/en/')
             ]

DISPLAY_CATEGORIES_ON_MENU = False
DISPLAY_PAGES_ON_MENU = False

# Blogroll
LINKS = (('Katedra filozofie a dejín filozofie',
          'https://fphil.uniba.sk/katedry-a-odborne-pracoviska/katedra-filozofie-a-dejin-filozofie/'),
         ('Agentúra na podporu výskumu a vývoja',
          'https://www.apvv.sk/'),
         ('Sledujte nás na Facebooku',
          'https://www.facebook.com/kfdf.fif.uk/'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)


LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

PLUGIN_PATHS = ["./plugins/"]
PLUGINS = ['i18n_subsites', 'photos']

DEFAULT_PAGINATION = 5

PAGINATED_TEMPLATES = {'index':3, 'category':5}

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}

I18N_SUBSITES = {
    'en': {
        'THEME': 'themes/naufip-en',
	    'SITENAME': 'NAUFIP',
        'SITESUBTITLE': 'Naturalism as an Universal Philosophical Programme',
        'MENUITEMS': [('Home','/en'),
                      ('About','/en/pages/about-the-project.html'),
                      ('Researchers','/en/pages/researchers.html'),
                      ('Activities', '/en/category/activities.html'),
                      ('Publications','/en/pages/publications.html'),
                    ],
        'LINKS': (('Department of Philosophy and History of Philosophy',
                   'https://fphil.uniba.sk/en/departments-and-research-centres/department-of-philosophy-and-history-of-philosophy/'),
                  ('Slovak Research and Development Agency',
                   'https://www.apvv.sk/?lang=en'),
                  ('Follow us on Facebook', 'https://www.facebook.com/kfdf.fif.uk/'),),
	}
}
