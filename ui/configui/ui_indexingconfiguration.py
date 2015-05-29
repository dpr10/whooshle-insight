from PyQt4 import QtGui


class Ui_IndexingConfiguration:

    def __init__(self, parent):
        # components
        self.index_path = QtGui.QLineEdit()
        self.index_path.setReadOnly(True)

        self.index_path_label = QtGui.QLabel('<strong>Base de datos:</strong>')

        self.index_path_button = QtGui.QToolButton()
        self.index_path_button.setIcon(QtGui.QIcon(':/img/open.svg'))

        # documets to index box options
        self.documents_box = QtGui.QGroupBox('Documentos')

        self.pdf_document = QtGui.QCheckBox('PDF')
        self.html_document = QtGui.QCheckBox('HTML')
        self.epub_document = QtGui.QCheckBox('EPUB')
        self.chm_document = QtGui.QCheckBox('CHM')

        # spacer
        vertical_spacer = QtGui.QSpacerItem(
            0, 0,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding
        )

        # layouts
        self.index_layout = QtGui.QHBoxLayout()
        self.index_layout.addWidget(self.index_path)
        self.index_layout.addWidget(self.index_path_button)

        self.documents_layout = QtGui.QVBoxLayout()
        self.documents_layout.addWidget(self.pdf_document)
        self.documents_layout.addWidget(self.chm_document)
        self.documents_layout.addWidget(self.epub_document)
        self.documents_layout.addWidget(self.html_document)
        self.documents_layout.addItem(vertical_spacer)

        self.documents_box.setLayout(self.documents_layout)

        # main layout
        self.main_layout = QtGui.QGridLayout()
        self.main_layout.addWidget(self.index_path_label)
        self.main_layout.addLayout(self.index_layout, 1, 0)
        self.main_layout.addWidget(self.documents_box)

        # parent
        parent.setLayout(self.main_layout)
