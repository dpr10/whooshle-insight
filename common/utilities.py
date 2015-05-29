from PyQt4.QtCore import QString

try:
    _from_Utf8 = QString.fromUtf8
except AttributeError:
    _from_Utf8 = lambda s: s
