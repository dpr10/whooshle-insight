# _*_coding:utf-8_*_

from PyQt4 import QtGui

from common.utilities import _from_Utf8
from view.configview.routesconfigurationtab import RoutesConfigurationTab
from view.configview.indexingconfigurationtab import IndexingConfigurationTab
from view.configview.appsconfigurationtab import AppsConfigurationTab


class Ui_Configuration:

    def __init__(self, parent):
        # components
        # self.apps_configuration = AppsConfigurationTab()
        self.routes_configuration = RoutesConfigurationTab()
        self.indexing_configuration = IndexingConfigurationTab()

        self.tab_options = QtGui.QTabWidget()
        # self.tab_options.addTab(self.apps_configuration, 'Aplicaciones')
        self.tab_options.addTab(self.routes_configuration, 'Rutas')
        self.tab_options.addTab(self.indexing_configuration, 'Indexar')

        self.close = QtGui.QPushButton('Cerrar')
        self.close.setIcon(QtGui.QIcon(':/img/close.svg'))

        # spacers
        horizontal_spacer = QtGui.QSpacerItem(
            40, 20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum
        )

        # layout
        self.button_box_layout = QtGui.QHBoxLayout()
        self.button_box_layout.addItem(horizontal_spacer)
        self.button_box_layout.addWidget(self.close)

        self.main_layout = QtGui.QGridLayout()
        self.main_layout.addWidget(self.tab_options, 0, 0)
        self.main_layout.addLayout(self.button_box_layout, 1, 0)

        # parent
        parent.setWindowTitle(_from_Utf8('Configuración'))
        parent.setLayout(self.main_layout)
        parent.resize(600, 400)
