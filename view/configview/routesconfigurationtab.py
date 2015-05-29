# _*_coding:utf-8_*_

from PyQt4 import QtGui, QtCore

from common.utilities import _from_Utf8
from ui.configui.ui_routesconfiguration import Ui_RoutesConfiguration
from config.configuration import Configuration


class RoutesConfigurationTab(QtGui.QWidget):

    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_RoutesConfiguration(self)

        # connections
        self.ui.add_route.clicked.connect(self.add_route)
        self.ui.remove_route.clicked.connect(self.remove_route)

    def initialize_ui(self):
        routes = Configuration.routes()

        self.ui.routes_list.clear()

        for route in routes:
            self.ui.routes_list.addItem(route)

        if len(routes) > 0:
            self.ui.remove_route.setEnabled(True)
        else:
            self.ui.remove_route.setDisabled(True)

    def add_route(self):
        path = QtGui.QFileDialog.getExistingDirectory(
            self,
            'Seleccionar ruta',
            QtCore.QDir.homePath()
        )

        if path != '':
            for index in xrange(self.ui.routes_list.count()):
                if self.ui.routes_list.item(index).text() == path:
                    QtGui.QMessageBox.information(
                        self,
                        _from_Utf8('Añadir ruta'),
                        'La ruta seleccionada ya existe'
                    )

                    return

            path_dir = QtCore.QDir(path)

            if not path_dir.isReadable:
                QtGui.QMessageBox.critical(
                    self,
                    _from_Utf8('Añadir ruta'),
                    'El directorio seleccionado no tiene permiso de lectura'
                )

                return

            # update ui
            self.ui.routes_list.addItem(path)

            # update configuration
            routes = Configuration.routes()
            routes.append(path)
            Configuration.set_routes(routes=routes)

    def remove_route(self):
        self.ui.routes_list.blockSignals(True)

        # fix it!!!
        current_row = self.ui.routes_list.currentRow()
        current_path = self.ui.routes_list.currentItem().text()
        self.ui.routes_list.takeItem(current_row)

        self.ui.routes_list.blockSignals(False)

        # update configuration
        routes = Configuration.routes()
        routes.remove(current_path)
        Configuration.set_routes(routes=routes)
