# _*_coding:utf-8_*_

from os import system

from PyQt4 import QtGui
from PyQt4.QtCore import QFileInfo

from common.utilities import _from_Utf8
from ui.ui_mainwindow import Ui_MainWindow
from view.configview.configurationdialog import ConfigurationDialog
from view.updateindexdbdialog import UpdateIndexDBDialog
from indexer.querymanager import QueryManager
from indexer.indexmanager import IndexManager
from config.configuration import Configuration

FIELD_OPTIONS = (
    'title',
    'author',
    'content'
)


class MainWindow(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow(self)

        # components
        self.configuration_dialog = ConfigurationDialog()
        self.configuration_dialog.setModal(True)

        self.update_db_dialog = UpdateIndexDBDialog()
        self.update_db_dialog.setModal(True)

        # connections
        self.ui.search_button.clicked.connect(self.search)
        self.ui.search_results_list.itemDoubleClicked.connect(
            self.open_document
        )

        # menu
        self.ui.update_index_db.triggered.connect(self.show_update_db_dialog)
        self.ui.configuration_action.triggered.connect(self.show_configuration)
        self.ui.about_qt_action.triggered.connect(QtGui.QApplication.aboutQt)

    def show_configuration(self):
        self.configuration_dialog.initialize_ui()
        self.configuration_dialog.show()

    def show_update_db_dialog(self):
        self.update_db_dialog.initialize_ui()
        self.update_db_dialog.show()

    def update_db(self):
        index_manager = IndexManager()
        index_manager.index()

    def search(self):
        self.ui.banner.setVisible(False)

        if len(Configuration.indexed_documents()) != 0:
            query_manager = QueryManager()
            results = query_manager.serch(
                to_search=unicode(self.ui.search_text.text()),
                field=FIELD_OPTIONS[self.ui.search_filter.currentIndex()]
            )

            if len(results) == 0:
                self.ui.info_label.setText(
                    _from_Utf8(
                        'No se encontró ningún documento con esa descripción'
                    )
                )

                self.ui.search_results_list.setVisible(False)
                self.ui.info_label.setVisible(True)
            else:
                self.ui.search_results_list.clear()

                for result in results:
                    self.ui.search_results_list.addItem(result['url'])

                self.ui.search_results_list.setVisible(True)
                self.ui.info_label.setVisible(False)
        else:
            self.ui.info_label.setText(
                _from_Utf8(
                    'No exsiten documentos indexados en la base de datos'
                )
            )

            self.ui.search_results_list.setVisible(False)
            self.ui.info_label.setVisible(True)

    def open_document(self, item):
        system('"%s"' % item.text())
