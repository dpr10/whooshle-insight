from PyQt4 import QtGui


class Ui_RoutesConfiguration:

    def __init__(self, parent):
        # components
        self.routes_list = QtGui.QListWidget()

        self.add_route = QtGui.QToolButton()
        self.add_route.setIcon(QtGui.QIcon(':/img/add.svg'))

        self.remove_route = QtGui.QToolButton()
        self.remove_route.setIcon(QtGui.QIcon(':/img/remove.svg'))

        # spcaers
        horizontal_spacer = QtGui.QSpacerItem(
            40, 20,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum
        )

        # layouts
        self.button_layout = QtGui.QHBoxLayout()
        self.button_layout.addItem(horizontal_spacer)
        self.button_layout.addWidget(self.add_route)
        self.button_layout.addWidget(self.remove_route)

        self.main_layout = QtGui.QGridLayout()
        self.main_layout.addLayout(self.button_layout, 0, 0)
        self.main_layout.addWidget(self.routes_list)

        # parent
        parent.setLayout(self.main_layout)
