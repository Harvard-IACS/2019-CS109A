from __future__ import absolute_import, print_function, unicode_literals

import os
import re

from liquid_tags.mdx_liquid_tags import LiquidTags

from .core import get_html_from_filepath, fix_css


SYNTAX = "{% notebook ~/absolute/path/to/notebook.ipynb [cells[start:end]] %}"
FORMAT = re.compile(r"""
^(\s+)?                                                # whitespace
(?P<src>\S+)                                           # source path
(\s+)?                                                 # whitespace
((cells\[)(?P<start>-?[0-9]*):(?P<end>-?[0-9]*)(\]))?  # optional cells
(\s+)?$                                                # whitespace
""", re.VERBOSE)

@LiquidTags.register('notebook')
def notebook(preprocessor, tag, markup):
    match = FORMAT.search(markup)
    if match:
        argdict = match.groupdict()
        src = argdict['src']
        start = argdict['start']
        end = argdict['end']
    else:
        raise ValueError("Error processing input, "
                         "expected syntax: {0}".format(SYNTAX))

    start = int(start) if start else 0
    end = int(end) if end else None

    # nb_dir =  preprocessor.configs.getConfig('NOTEBOOK_DIR')
    nb_path = os.path.join('content', src)
    content, info = get_html_from_filepath(nb_path, start=start, end=end)
    ignore_css = preprocessor.configs.getConfig('IPYNB_IGNORE_CSS', False)
    content = fix_css(content, info, ignore_css=ignore_css)
    content = preprocessor.configs.htmlStash.store(content, safe=True)
    return content


# ---------------------------------------------------
# This import allows notebook tag to be a Pelican plugin
from liquid_tags import register  # noqa
