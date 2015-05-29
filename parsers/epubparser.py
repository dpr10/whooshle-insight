from ebooklib.epub import EpubReader, EpubHtml

from epubzilla.epubzilla import Epub
from htmlparser import HtmlParser
from parsers.parser import Parser


class EpubParser(Parser):
    def filename(self):
        return self._filename

    def set_filename(self, filename):
        self._filename = filename
        self._epub_info = Epub.from_file(epub_file=self._filename)

    def title(self):
        return unicode(self._epub_info.title)

    def author(self):
        if self._epub_info.author:
            return self._epub_info.author
        else:
            return u'<Desconocido>'

    def content(self):
        content = u''

        epub_reader = EpubReader(self._filename)
        epub = epub_reader.load()

        for item in epub.items:
            if isinstance(item, EpubHtml):
                html_parser = HtmlParser(html=item.get_body_content())
                content += html_parser.content() + '\n'

        return content
