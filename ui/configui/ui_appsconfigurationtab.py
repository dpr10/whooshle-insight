from PyQt4 import QtGui


class Ui_AppsConfigurationTab:

    def __init__(self, parent):
        # componets
        # pdf box
        self.pdf_label = QtGui.QLabel('PDF')
        self.pdf_label.setMinimumWidth(30)

        self.pdf_app_route = QtGui.QLineEdit()
        self.pdf_app_route.setReadOnly(True)

        self.pdf_app_open = QtGui.QToolButton()
        self.pdf_app_open.setIcon(QtGui.QIcon(':/img/open.svg'))

        # html box
        # self.html_label = QtGui.QLabel('HTML')
        # self.html_label.setMinimumWidth(30)

        # self.html_app_route = QtGui.QLineEdit()
        # self.html_app_route.setReadOnly(True)

        # self.html_app_open = QtGui.QToolButton()
        # self.html_app_open.setIcon(QtGui.QIcon(':/img/open.svg'))

        # chm box
        # self.chm_label = QtGui.QLabel('CHM')
        # self.chm_label.setMinimumWidth(30)

        # self.chm_app_route = QtGui.QLineEdit()
        # self.chm_app_route.setReadOnly(True)

        # self.chm_app_open = QtGui.QToolButton()
        # self.chm_app_open.setIcon(QtGui.QIcon(':/img/open.svg'))

        # epub box
        # self.epub_label = QtGui.QLabel('EPUB')
        # self.epub_label.setMinimumWidth(30)

        # self.epub_app_route = QtGui.QLineEdit()
        # self.epub_app_route.setReadOnly(True)

        # self.epub_app_open = QtGui.QToolButton()
        # self.epub_app_open.setIcon(QtGui.QIcon(':/img/open.svg'))

        # spacers
        vertcal_spacer = QtGui.QSpacerItem(
            0, 0,
            QtGui.QSizePolicy.Minimum,
            QtGui.QSizePolicy.Expanding
        )

        # layouts
        self.pdf_layout = QtGui.QHBoxLayout()
        self.pdf_layout.addWidget(self.pdf_label)
        self.pdf_layout.addWidget(self.pdf_app_route)
        self.pdf_layout.addWidget(self.pdf_app_open)

        # self.html_layout = QtGui.QHBoxLayout()
        # self.html_layout.addWidget(self.html_label)
        # self.html_layout.addWidget(self.html_app_route)
        # self.html_layout.addWidget(self.html_app_open)

        # self.chm_layout = QtGui.QHBoxLayout()
        # self.chm_layout.addWidget(self.chm_label)
        # self.chm_layout.addWidget(self.chm_app_route)
        # self.chm_layout.addWidget(self.chm_app_open)

        # self.epub_layout = QtGui.QHBoxLayout()
        # self.epub_layout.addWidget(self.epub_label)
        # self.epub_layout.addWidget(self.epub_app_route)
        # self.epub_layout.addWidget(self.epub_app_open)

        # main layout
        self.main_layout = QtGui.QVBoxLayout()
        self.main_layout.addLayout(self.pdf_layout)
        # self.main_layout.addLayout(self.html_layout)
        # self.main_layout.addLayout(self.chm_layout)
        # self.main_layout.addLayout(self.epub_layout)
        self.main_layout.addItem(vertcal_spacer)

        # parent
        parent.setLayout(self.main_layout)
