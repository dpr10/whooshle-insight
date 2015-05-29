from PyQt4 import QtGui, QtCore

from ui.configui.ui_appsconfigurationtab import Ui_AppsConfigurationTab
from config.configuration import Configuration


class AppsConfigurationTab(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_AppsConfigurationTab(self)

        # connections
        self.ui.pdf_app_open.clicked.connect(self.select_pdf_app)

    def initialize_ui(self):
        self.ui.pdf_app_route.setText(
            Configuration.app_route(document_type=Configuration.PDF_DOCUMENT)
        )

    def select_pdf_app(self):
        pdf_app = QtGui.QFileDialog.getOpenFileName(
            self,
            'Abrir',
            QtCore.QDir.homePath(),
            'Ejecutables (*.exe *.bat)'
        )

        if pdf_app != '':
            self.ui.pdf_app_route.setText(
                QtCore.QDir.fromNativeSeparators(pdf_app)
            )

            Configuration.set_app_route(
                document_type=Configuration.PDF_DOCUMENT,
                route=pdf_app
            )
