from collections import deque

from PyQt4 import QtCore

from config.configuration import Configuration

DOCUMENTS_EXTENSION = (
    '*.pdf',
    '*.html',
    '*.htm',
    '*.chm',
    '*.epub'
)


class DocumentFinder:

    def __init__(self, path):
        self._path = path

    def _find_documents(self):
        dir_list = deque()
        dir_list.append(self._path)

        self._documents_finded = []

        while len(dir_list) > 0:
            current_path = dir_list.popleft()
            current_dir = QtCore.QDir(current_path)

            for document in current_dir.entryInfoList(DOCUMENTS_EXTENSION, QtCore.QDir.Files, QtCore.QDir.Name):
                self._documents_finded.append(document.absoluteFilePath())

            for next_dir in current_dir.entryInfoList(QtCore.QDir.AllDirs | QtCore.QDir.NoDot | QtCore.QDir.NoDotDot, QtCore.QDir.Name):
                dir_list.append(next_dir.absoluteFilePath())

    def find_documents(self):
        """
        find valid documents
        :return:
        """
        self._find_documents()

        documents = Configuration.indexed_documents()

        documents_added = []

        for document in self._documents_finded:
            if document in documents:
                documents.remove(document)
            else:
                documents_added.append(document)

        return documents_added, documents
