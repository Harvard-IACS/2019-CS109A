from __future__ import absolute_import, print_function, unicode_literals

import os
import json
import six

try:
    # Py3k
    from html.parser import HTMLParser
except ImportError:
    # Py2.7
    from HTMLParser import HTMLParser

from pelican import signals
from pelican.readers import MarkdownReader, HTMLReader, BaseReader

from .ipynb import get_html_from_filepath, fix_css


def register():
    """
    Register the new "ipynb" reader
    """
    def add_reader(arg):
        arg.settings["READERS"]["ipynb"] = IPythonNB
    signals.initialized.connect(add_reader)


class IPythonNB(BaseReader):
    """
    Extend the Pelican.BaseReader to `.ipynb` files can be recognized
    as a markup language:

    Setup:

    `pelicanconf.py`:
    ```
    MARKUP = ('md', 'ipynb')
    ```
    """
    enabled = True
    file_extensions = ['ipynb']

    def read(self, filepath):
        metadata = {}
        metadata['ipython'] = True

        # Files
        filedir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)
        metadata_filename = os.path.splitext(filename)[0] + '.ipynb-meta'
        metadata_filepath = os.path.join(filedir, metadata_filename)

        if os.path.exists(metadata_filepath):
            # Metadata is on a external file,
            # process using Pelican MD Reader
            md_reader = MarkdownReader(self.settings)
            _content, metadata = md_reader.read(metadata_filepath)
        else:
            # Load metadata from ipython notebook file
            ipynb_file = open(filepath)
            notebook_metadata = json.load(ipynb_file)['metadata']

            # Change to standard pelican metadata
            for key, value in notebook_metadata.items():
                key = key.lower()
                if key in ("title", "date", "category", "tags", "slug", "author"):
                    metadata[key] = self.process_metadata(key, value)

        keys = [k.lower() for k in metadata.keys()]
        if not set(['title', 'date']).issubset(set(keys)):
            # Probably using ipynb.liquid mode
            md_filename = filename.split('.')[0] + '.md'
            md_filepath = os.path.join(filedir, md_filename)
            if not os.path.exists(md_filepath):
                raise Exception("Could not find metadata in `.ipynb-meta`, inside `.ipynb` or external `.md` file.")
            else:
                raise Exception("Could not find metadata in `.ipynb-meta` or inside `.ipynb` but found `.md` file, "
                      "assuming that this notebook is for liquid tag usage if true ignore this error")

        content, info = get_html_from_filepath(filepath)

        # Generate Summary: Do it before cleaning CSS
        if 'summary' not in [key.lower() for key in self.settings.keys()]:
            parser = MyHTMLParser(self.settings, filename)
            if isinstance(content, six.binary_type): # PY2 (str) or PY3 (bytes) to PY2 (unicode) or PY3 (str)
                # unicode_literals makes format() try to decode as ASCII. Enforce decoding as UTF-8.
                content = '<body>{0}</body>'.format(content.decode("utf-8"))
            else:
                # Content already decoded
                content = '<body>{0}</body>'.format(content)
            parser.feed(content)
            parser.close()
            content = parser.body
            if ('IPYNB_USE_META_SUMMARY' in self.settings.keys() and \
              self.settings['IPYNB_USE_META_SUMMARY'] == False) or \
              'IPYNB_USE_META_SUMMARY' not in self.settings.keys():
                metadata['summary'] = parser.summary

        ignore_css = True if 'IPYNB_IGNORE_CSS' in self.settings.keys() else False
        content = fix_css(content, info, ignore_css=ignore_css)
        return content, metadata


class MyHTMLParser(HTMLReader._HTMLParser):
    """
    Custom Pelican `HTMLReader._HTMLParser` to create the summary of the content
    based on settings['SUMMARY_MAX_LENGTH'].

    Summary is stoped if founds any div containing ipython notebook code cells.
    This is needed in order to generate valid HTML for the summary,
    a simple string split will break the html generating errors on the theme.
    The downside is that the summary length is not exactly the specified, it stops at
    completed div/p/li/etc tags.
    """
    def __init__(self, settings, filename):
        HTMLReader._HTMLParser.__init__(self, settings, filename)
        self.settings = settings
        self.filename = filename
        self.wordcount = 0
        self.summary = None

        self.stop_tags = [('div', ('class', 'input')), ('div', ('class', 'output')), ('h2', ('id', 'Header-2'))]
        if 'IPYNB_STOP_SUMMARY_TAGS' in self.settings.keys():
            self.stop_tags = self.settings['IPYNB_STOP_SUMMARY_TAGS']
        if 'IPYNB_EXTEND_STOP_SUMMARY_TAGS' in self.settings.keys():
            self.stop_tags.extend(self.settings['IPYNB_EXTEND_STOP_SUMMARY_TAGS'])

    def handle_starttag(self, tag, attrs):
        HTMLReader._HTMLParser.handle_starttag(self, tag, attrs)

        if self.wordcount < self.settings['SUMMARY_MAX_LENGTH']:
            mask = [stoptag[0] == tag and (stoptag[1] is None or stoptag[1] in attrs) for stoptag in self.stop_tags]
            if any(mask):
                self.summary = self._data_buffer
                self.wordcount = self.settings['SUMMARY_MAX_LENGTH']

    def handle_endtag(self, tag):
        HTMLReader._HTMLParser.handle_endtag(self, tag)

        if self.wordcount < self.settings['SUMMARY_MAX_LENGTH']:
            self.wordcount = len(strip_tags(self._data_buffer).split(' '))
            if self.wordcount >= self.settings['SUMMARY_MAX_LENGTH']:
                self.summary = self._data_buffer


def strip_tags(html):
    """
    Strip html tags from html content (str)
    Useful for summary creation
    """
    s = HTMLTagStripper()
    s.feed(html)
    return s.get_data()


class HTMLTagStripper(HTMLParser):
    """
    Custom HTML Parser to strip HTML tags
    Useful for summary creation
    """
    def __init__(self):
        HTMLParser.__init__(self)
        self.reset()
        self.fed = []

    def handle_data(self, html):
        self.fed.append(html)

    def get_data(self):
        return ''.join(self.fed)
