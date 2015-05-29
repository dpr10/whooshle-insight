from cStringIO import StringIO

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfinterp import PDFResourceManager
from pdfminer.pdfinterp import PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

from parsers.parser import Parser


class PdfParser(Parser):

    def __init__(self):
        self._title = u'<Desconocido>'
        self._author = u'<Desconocido>'
        self._content = u''

    def extract_data(self):
        retstr = StringIO()
        parser = PDFParser(open(self._filename, 'rb'))

        try:
            document = PDFDocument(parser)

            for info in document.info:
                if 'Title' in info and len(info['Title']) > 0:
                    self._title = unicode(info['Title'], errors='ignore')
                if 'Author' in info and len(info['Author']) > 0:
                    self._author = unicode(info['Author'], errors='ignore')
        except Exception as e:
            self._content = u''

        if document.is_extractable:
            rsrcmgr = PDFResourceManager()
            device = TextConverter(
                rsrcmgr, retstr, codec='utf-8', laparams=LAParams())
            interpreter = PDFPageInterpreter(rsrcmgr, device)

            for page in PDFPage.create_pages(document):
                interpreter.process_page(page)

            self._content = unicode(retstr.getvalue(), errors='ignore')
        else:
            self._content = u''

    def set_filename(self, filename):
        self._filename = filename
        self.extract_data()
