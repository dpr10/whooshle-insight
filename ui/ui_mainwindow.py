# _*_coding:utf-8_*_

from PyQt4 import QtGui, QtCore

from common.utilities import _from_Utf8

import res.img_rc

SEARCH_FILTERS = (
    'Titulo',
    'Autor',
    'Contenido'
)


class Ui_MainWindow:

    def __init__(self, parent):
        # components
        self.search_text = QtGui.QLineEdit()
        self.search_text.setPlaceholderText('Buscar...')

        self.search_button = QtGui.QPushButton()
        self.search_button.setIcon(QtGui.QIcon(':/img/search.svg'))
        self.search_button.setShortcut(QtCore.Qt.Key_Return)

        self.search_filter = QtGui.QComboBox()
        self.search_filter.addItems(SEARCH_FILTERS)
        self.search_filter.setCurrentIndex(2)

        self.separation_line = QtGui.QFrame()
        self.separation_line.setFrameShape(QtGui.QFrame.HLine)
        self.separation_line.setFrameShadow(QtGui.QFrame.Sunken)

        self.banner = QtGui.QLabel()
        self.banner.setText(
            '<html><img src=":/img/logo_insight.png" /></html>'
        )

        self.info_label = QtGui.QLabel()
        font = QtGui.QFont()
        font.setBold(True)
        font.setPointSize(12)
        self.info_label.setFont(font)

        self.search_results_list = QtGui.QListWidget()
        self.search_results_list.setVisible(False)

        # menu
        self.menu_bar = QtGui.QMenuBar()

        self.index_db_menu = self.menu_bar.addMenu('Base de datos')
        self.update_index_db = QtGui.QAction('Actualizar', self.index_db_menu)
        self.update_index_db.setIcon(QtGui.QIcon(':/img/update.svg'))
        self.index_db_menu.addAction(self.update_index_db)

        self.option_menu = self.menu_bar.addMenu('Opciones')

        self.configuration_action = QtGui.QAction(
            _from_Utf8('Configuración'),
            self.option_menu
        )
        self.configuration_action.setIcon(
            QtGui.QIcon(':/img/configuration.svg')
        )

        self.option_menu.addAction(self.configuration_action)

        self.help_menu = self.menu_bar.addMenu('Ayuda')

        self.about_action = QtGui.QAction('Acerca de..', self.help_menu)
        self.about_action.setIcon(QtGui.QIcon(':/img/about.svg'))

        self.about_qt_action = QtGui.QAction('Acerca de Qt', self.help_menu)
        self.about_qt_action.setIcon(QtGui.QIcon(':/img/qt.svg'))

        self.help_menu.addAction(self.about_action)
        self.help_menu.addAction(self.about_qt_action)

        # layouts
        self.search_layout = QtGui.QHBoxLayout()
        self.search_layout.addWidget(self.search_text)
        self.search_layout.addWidget(self.search_button)
        self.search_layout.addWidget(self.search_filter)

        self.main_layout = QtGui.QGridLayout()
        self.main_layout.addLayout(self.search_layout, 0, 0)
        self.main_layout.addWidget(self.separation_line)
        self.main_layout.addWidget(self.search_results_list)
        self.main_layout.addWidget(
            self.info_label, 3, 0, QtCore.Qt.AlignCenter)
        self.main_layout.addWidget(self.banner, 3, 0, QtCore.Qt.AlignCenter)

        # central widget
        self.central_widget = QtGui.QWidget()
        self.central_widget.setLayout(self.main_layout)

        # status bar
        self.status_bar = QtGui.QStatusBar()

        # parent
        parent.setWindowTitle('Whooshle Insight v1.0.0')
        parent.setMenuBar(self.menu_bar)
        parent.setCentralWidget(self.central_widget)
        parent.setStatusBar(self.status_bar)

        parent.setMinimumWidth(480)
        parent.setMinimumHeight(320)
        parent.resize(640, 480)
