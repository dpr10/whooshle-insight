from PyQt4 import QtGui
from PyQt4.QtCore import Qt


class Ui_UpdateIndexDBDialog:

    def __init__(self, parent):
        # info labels
        self.info_new_documents_label = QtGui.QLabel('label:')
        self.info_new_documents_label.setAlignment(Qt.AlignRight)

        self.info_new_documents_value = QtGui.QLabel('0')
        self.info_new_documents_value.setAlignment(Qt.AlignLeft)

        self.info_delete_documents_label = QtGui.QLabel('label:')
        self.info_delete_documents_label.setAlignment(Qt.AlignRight)

        self.info_delete_documents_value = QtGui.QLabel('0')
        self.info_delete_documents_value.setAlignment(Qt.AlignLeft)

        # info box
        self.info_box = QtGui.QGroupBox('Documentos a procesar')

        # progress bar box
        self.info_progress_status = QtGui.QLabel('progress...')
        self.progress_bar = QtGui.QProgressBar()

        # action button
        self.action_button = QtGui.QPushButton('Actualizar')

        # spacers
        vertical_spacer = QtGui.QSpacerItem(
            0, 0,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding
        )
        horizontal_spacer = QtGui.QSpacerItem(
            0, 0,
            QtGui.QSizePolicy.Expanding,
            QtGui.QSizePolicy.Minimum
        )

        # layouts
        self.info_box_layout = QtGui.QGridLayout()
        self.info_box_layout.addWidget(self.info_new_documents_label, 0, 0)
        self.info_box_layout.addWidget(self.info_new_documents_value, 0, 1)
        self.info_box_layout.addWidget(self.info_delete_documents_label, 1, 0)
        self.info_box_layout.addWidget(self.info_delete_documents_value, 1, 1)
        self.info_box.setLayout(self.info_box_layout)

        self.action_layout = QtGui.QHBoxLayout()
        self.action_layout.addItem(horizontal_spacer)
        self.action_layout.addWidget(self.action_button)
        self.action_layout.addItem(horizontal_spacer)

        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.addWidget(self.info_box)
        self.main_layout.addWidget(self.info_progress_status)
        self.main_layout.addWidget(self.progress_bar)
        self.main_layout.addItem(vertical_spacer)
        self.main_layout.addLayout(self.action_layout)

        # parent
        parent.setWindowTitle('Actualizar base de datos')
        parent.setLayout(self.main_layout)

        parent.setMinimumWidth(400)
        parent.setMinimumHeight(200)
        parent.setMaximumHeight(200)

        parent.resize(400, 200)
