"""
Core module that handles the conversion from notebook to HTML plus some utilities
"""
from __future__ import absolute_import, print_function, division

import re

import IPython
try:
    # Jupyter
    from traitlets.config import Config
    from traitlets import Integer
except ImportError:
    # IPython < 4.0
    from IPython.config import Config
    from IPython.utils.traitlets import Integer

try:
    # Jupyter
    from nbconvert.preprocessors import Preprocessor
except ImportError:
    # IPython < 4.0
    from IPython.nbconvert.preprocessors import Preprocessor

try:
    # Jupyter
    import nbconvert
except ImportError:
    # IPython < 4.0
    import IPython.nbconvert as nbconvert

from nbconvert.exporters import HTMLExporter
try:
    from nbconvert.filters.highlight import _pygment_highlight
except ImportError:
    # IPython < 2.0
    from nbconvert.filters.highlight import _pygments_highlight

try:
    from bs4 import BeautifulSoup
except:
    BeautifulSoup = None

from pygments.formatters import HtmlFormatter

from copy import deepcopy


LATEX_CUSTOM_SCRIPT = """
<script type="text/javascript">if (!document.getElementById('mathjaxscript_pelican_#%@#$@#')) {
    var mathjaxscript = document.createElement('script');
    mathjaxscript.id = 'mathjaxscript_pelican_#%@#$@#';
    mathjaxscript.type = 'text/javascript';
    mathjaxscript.src = '//cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.1/MathJax.js?config=TeX-AMS-MML_HTMLorMML';
    mathjaxscript[(window.opera ? "innerHTML" : "text")] =
        "MathJax.Hub.Config({" +
        "    config: ['MMLorHTML.js']," +
        "    TeX: { extensions: ['AMSmath.js','AMSsymbols.js','noErrors.js','noUndefined.js'], equationNumbers: { autoNumber: 'AMS' } }," +
        "    jax: ['input/TeX','input/MathML','output/HTML-CSS']," +
        "    extensions: ['tex2jax.js','mml2jax.js','MathMenu.js','MathZoom.js']," +
        "    displayAlign: 'center'," +
        "    displayIndent: '0em'," +
        "    showMathMenu: true," +
        "    tex2jax: { " +
        "        inlineMath: [ ['$','$'] ], " +
        "        displayMath: [ ['$$','$$'] ]," +
        "        processEscapes: true," +
        "        preview: 'TeX'," +
        "    }, " +
        "    'HTML-CSS': { " +
        " linebreaks: { automatic: true, width: '95% container' }, " +
        "        styles: { '.MathJax_Display, .MathJax .mo, .MathJax .mi, .MathJax .mn': {color: 'black ! important'} }" +
        "    } " +
        "}); ";
    (document.body || document.getElementsByTagName('head')[0]).appendChild(mathjaxscript);
}
</script>
"""


def get_html_from_filepath(filepath, start=0, end=None):
    """Convert ipython notebook to html
    Return: html content of the converted notebook
    """
    config = Config({'CSSHTMLHeaderTransformer': {'enabled': True,
                     'highlight_class': '.highlight-ipynb'},
                     'SubCell': {'enabled':True, 'start':start, 'end':end}})
    exporter = HTMLExporter(config=config, template_file='basic',
                            filters={'highlight2html': custom_highlighter},
                            preprocessors=[SubCell])
    content, info = exporter.from_filename(filepath)

    if BeautifulSoup:
        soup = BeautifulSoup(content, 'html.parser')
        for i in soup.findAll('div', {'class': 'input'}):
            if i.findChildren()[1].find(text='#ignore') is not None:
                i.extract()
        content = soup.decode(formatter=None)

    return content, info


def fix_css(content, info, ignore_css=False):
    """
    General fixes for the notebook generated html
    """
    def filter_css(style_text):
        """
        HACK: IPython returns a lot of CSS including its own bootstrap.
        Get only the IPython Notebook CSS styles.
        """
        index = style_text.find('/*!\n*\n* IPython notebook\n*\n*/')
        if index > 0:
            style_text = style_text[index:]
        index = style_text.find('/*!\n*\n* IPython notebook webapp\n*\n*/')
        if index > 0:
            style_text = style_text[:index]

        style_text = re.sub(r'color\:\#0+(;)?', '', style_text)
        style_text = re.sub(r'\.rendered_html[a-z0-9,._ ]*\{[a-z0-9:;%.#\-\s\n]+\}', '', style_text)
        return '<style type=\"text/css\">{0}</style>'.format(style_text)

    if ignore_css:
        content = content + LATEX_CUSTOM_SCRIPT
    else:
        ipython_css = '\n'.join(filter_css(css_style) for css_style in info['inlining']['css'])
        content = ipython_css + content + LATEX_CUSTOM_SCRIPT
    return content


def custom_highlighter(source, language='python', metadata=None):
    """
    Makes the syntax highlighting from pygments have prefix(`highlight-ipynb`)
    So it doesn't break the theme pygments

    This modifies both css prefixes and html tags

    Returns new html content
    """
    if not language:
        language = 'python'

    formatter = HtmlFormatter(cssclass='highlight-ipynb')
    output = _pygments_highlight(source, formatter, language, metadata)
    output = output.replace('<pre>', '<pre class="ipynb">')
    return output

#----------------------------------------------------------------------
# Create a preprocessor to slice notebook by cells

class SliceIndex(Integer):
    """An integer trait that accepts None"""
    default_value = None

    def validate(self, obj, value):
        if value is None:
            return value
        else:
            return super(SliceIndex, self).validate(obj, value)


class SubCell(Preprocessor):
    """A preprocessor to select a slice of the cells of a notebook"""
    start = SliceIndex(0, config=True, help="first cell of notebook")
    end = SliceIndex(None, config=True, help="last cell of notebook")

    def preprocess(self, nb, resources):
        nbc = deepcopy(nb)
        nbc.cells = nbc.cells[self.start:self.end]
        return nbc, resources
