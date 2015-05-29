from HTMLParser import HTMLParser

from lxml.html import tostring, document_fromstring
from lxml.html.clean import Cleaner

from parsers.parser import Parser


class HtmlParser(HTMLParser, Parser):

    def __init__(self):
        HTMLParser.__init__(self)

        self._title_finded = False

        self._clean_html()

        self._content = u''
        self._title = u'<Desconocido>'
        self._author = u'<Desconocido>'

        self.feed(data=self._filename)

    def _clean_html(self):
        cleaner = Cleaner(
            scripts=True,
            forms=True,
            links=True,
            comments=True,
            style=True,
            page_structure=False
        )

        self._filename = tostring(
            doc=cleaner.clean_html(
                html=document_fromstring(html=self._filename)
            )
        )

    def handle_starttag(self, tag, attrs):
        if tag == 'title' and not self._title_finded:
            self._title_finded = True
        elif tag == 'meta':
            author_finded = False

            for attr in attrs:
                if attr[0].lower() == 'name' and attr[1].lower() == 'author':
                    author_finded = True
                    continue
                if attr[0].lower() == 'content' and author_finded:
                    self._author = attr[1]
                    break

    def handle_endtag(self, tag):
        if tag == 'title' and self._title_finded:
            self._title_finded = False

    def handle_data(self, data):
        if self._title_finded:
            self._title += data
        elif len(data.strip()) > 0:
            self._content += '%s\n' % data.strip()
