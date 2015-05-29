from PyQt4 import QtGui
from PyQt4 import QtCore

from ui.configui.ui_indexingconfiguration import Ui_IndexingConfiguration
from config.configuration import Configuration


class IndexingConfigurationTab(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_IndexingConfiguration(self)

        # connections
        self.ui.index_path_button.clicked.connect(self.select_index_path)

        self.ui.pdf_document.clicked.connect(self.update_documents_config)
        self.ui.html_document.clicked.connect(self.update_documents_config)
        self.ui.epub_document.clicked.connect(self.update_documents_config)
        self.ui.chm_document.clicked.connect(self.update_documents_config)

    def initialize_ui(self):
        self.ui.index_path.setText(Configuration.index_path())

        self.ui.pdf_document.setChecked(
            Configuration.index_document(
                document_type=Configuration.PDF_DOCUMENT
            )
        )

        self.ui.html_document.setChecked(
            Configuration.index_document(
                document_type=Configuration.HTML_DOCUMENT
            )
        )

        self.ui.epub_document.setChecked(
            Configuration.index_document(
                document_type=Configuration.EPUB_DOCUMENT
            )
        )

        self.ui.chm_document.setChecked(
            Configuration.index_document(
                document_type=Configuration.CHM_DOCUMENT
            )
        )

    def select_index_path(self):
        index_path = QtGui.QFileDialog.getExistingDirectory(
            self,
            'Abrir',
            QtCore.QDir.homePath()
        )

        if index_path != '':
            self.ui.index_path.setText(
                QtCore.QDir.fromNativeSeparators(
                    '%s/%s' % (index_path, 'index_db')
                )
            )

            Configuration.set_index_path(
                path=QtCore.QDir.fromNativeSeparators(
                    '%s/%s' % (index_path, 'index_db')
                )
            )

    def update_documents_config(self):
        if self.ui.pdf_document.isChecked():
            Configuration.set_index_document(
                document_type=Configuration.PDF_DOCUMENT,
                value=1
            )
        else:
            Configuration.set_index_document(
                document_type=Configuration.PDF_DOCUMENT,
                value=0
            )

        if self.ui.html_document.isChecked():
            Configuration.set_index_document(
                document_type=Configuration.HTML_DOCUMENT,
                value=1
            )
        else:
            Configuration.set_index_document(
                document_type=Configuration.HTML_DOCUMENT,
                value=0
            )

        if self.ui.chm_document.isChecked():
            Configuration.set_index_document(
                document_type=Configuration.CHM_DOCUMENT,
                value=1
            )
        else:
            Configuration.set_index_document(
                document_type=Configuration.CHM_DOCUMENT,
                value=0
            )

        if self.ui.epub_document.isChecked():
            Configuration.set_index_document(
                document_type=Configuration.EPUB_DOCUMENT,
                value=1
            )
        else:
            Configuration.set_index_document(
                document_type=Configuration.EPUB_DOCUMENT,
                value=0
            )
