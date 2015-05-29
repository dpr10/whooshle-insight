from PyQt4 import QtGui

from ui.configui.ui_configuration import Ui_Configuration


class ConfigurationDialog(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Configuration(self)

        # connections
        self.ui.close.clicked.connect(self.close)

    def initialize_ui(self):
        # self.ui.apps_configuration.initialize_ui()
        self.ui.routes_configuration.initialize_ui()
        self.ui.indexing_configuration.initialize_ui()

        self.ui.tab_options.setCurrentIndex(0)
