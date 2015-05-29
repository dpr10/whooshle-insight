from sys import argv

from PyQt4.QtGui import QApplication

from view.mainwindow import MainWindow

if __name__ == '__main__':
    app = QApplication(argv)

    main_window = MainWindow()
    main_window.show()

    app.exec_()
