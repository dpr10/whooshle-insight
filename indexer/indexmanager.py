# _*_coding:utf-8_*_

from os.path import exists
from os import mkdir

from whoosh.index import create_in, open_dir
from whoosh.fields import *
from PyQt4 import QtCore

from config.configuration import Configuration
from indexer.tools.documentfinder import DocumentFinder
from parsers.pdfparser import PdfParser
# from parsers.htmlparser import HtmlParser
# from parsers.epubparser import EpubParser
# from parsers.chmparser import ChmParser

DOCUMENTS_PARSERS = {
    'pdf': PdfParser()
    # 'html': HtmlParser(),
    # 'htm': Htmlarser()
    # 'epub': EpubParser(),
    # 'chm': ChmParser()
}

URL_FIELD = 'url'

ADDING_STATE = 'Añadiendo documentos...'
REMOVING_STATE = 'Eliminando documentos...'
DONE_STATE = 'Terminado'

class IndexManager(QtCore.QObject):
    updated_progress = QtCore.pyqtSignal(str, int)
    updated_info = QtCore.pyqtSignal(int, int)
    update_canceled = QtCore.pyqtSignal()

    def __init__(self):
        QtCore.QObject.__init__(self)

        if not exists(Configuration.index_path()):
            mkdir(Configuration.index_path())

            schema = Schema(
                title=TEXT(stored=True),
                author=TEXT(stored=True),
                content=TEXT(),
                url=ID(unique=True, stored=True)
            )

            create_in(dirname=str(Configuration.index_path()), schema=schema)

        self._index_database = open_dir(
            dirname=str(Configuration.index_path())
        )

    def _index_document(self, title, author, content, url):
        """
        index current document
        :param title: document title
        :param author: document author
        :param content: document content
        :param url: document url
        :return:
        """
        writer = self._index_database.writer()

        writer.add_document(
            title=title,
            author=author,
            content=content,
            url=url
        )

        writer.commit()

    def _remove_document(self, content, field='url'):
        """
        remove any document with field=content
        :param content: content to search
        :param field: field to search
        :return:
        """
        writer = self._index_database.writer()
        writer.delete_by_term(fieldname=field, text=content)
        writer.commit()

    def cancel_index(self, cancel=True):
        self.cancel = cancel

    def search_documents(self):
        """
        search valid documents in config routes
        :return: document_added, documents deleted
        """
        self.documents_added = []
        self.documents_deleted = []

        routes = Configuration.routes()

        for route in routes:
            document_finder = DocumentFinder(path=route)

            added, deleted = document_finder.find_documents()

            self.documents_added += added
            self.documents_deleted += deleted

        return len(self.documents_added), len(self.documents_deleted)

    def index(self):
        """
        index all documents available
        :return:
        """
        self.cancel = False

        # start progress bar data
        current_document = 0
        total_documents = len(self.documents_added) + len(self.documents_deleted)

        # start info data
        documents_added = 0
        documents_deleted = 0

        # update progress bar
        self.updated_progress.emit(ADDING_STATE, current_document * 100 / total_documents)

        # add new documents
        for document_added in self.documents_added:
            file_info = QtCore.QFileInfo(document_added)

            document_type = str(file_info.suffix().toLower())

            if document_type in DOCUMENTS_PARSERS:
                parser = DOCUMENTS_PARSERS[document_type]
                parser.set_filename(document_added)

                self._index_document(
                    title=parser.title(),
                    author=parser.author(),
                    content=parser.content(),
                    url=unicode(document_added)
                )

                current_document += 1
                documents_added += 1

                # update indexed documents configuration
                indexed_documents = Configuration.indexed_documents()
                indexed_documents.append(document_added)
                Configuration.set_indexed_documents(indexed_documents)

                # update info
                self.updated_info.emit(documents_added, documents_deleted)

                # cancel index process
                if self.cancel:
                    self.update_canceled.emit()
                    return

                # update progress bar
                self.updated_progress.emit(ADDING_STATE, current_document * 100 / total_documents)

        # update progress bar
        self.updated_progress.emit(REMOVING_STATE, current_document * 100 / total_documents)

        # delete removed documents
        for document_deleted in self.documents_deleted:
            self._remove_document(content=document_deleted)

            current_document += 1
            documents_deleted += 1

            indexed_documents = Configuration.indexed_documents()
            indexed_documents.remove(document_deleted)
            Configuration.set_indexed_documents(indexed_documents)

            # update info
            self.updated_info.emit(documents_added, documents_deleted)

            # cancel index process
            if self.cancel:
                self.update_canceled.emit()
                return

            # update progress bar
            self.updated_progress.emit(REMOVING_STATE, current_document * 100 / total_documents)

        # update progress bar
        self.updated_progress.emit(DONE_STATE, 100)

        # update info
        self.updated_info.emit(documents_added, documents_deleted)

