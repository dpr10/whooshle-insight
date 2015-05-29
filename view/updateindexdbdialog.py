# _*_coding:utf-8_*_

from thread import allocate_lock, start_new_thread

from PyQt4 import QtGui

from ui.ui_updateindexdbdialog import Ui_UpdateIndexDBDialog
from indexer.indexmanager import IndexManager
from common.utilities import _from_Utf8

class UpdateIndexDBDialog(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)

        self.ui = Ui_UpdateIndexDBDialog(self)
        self.index_manager = IndexManager()

        # connections
        self.ui.action_button.clicked.connect(self.start_thread)

        self.index_manager.updated_progress.connect(self.update_progress)
        self.index_manager.updated_info.connect(self.update_info)
        self.index_manager.update_canceled.connect(self.cancel_update_db)

    def initialize_ui(self):
        self.updating = False

        self.added = 0
        self.removed = 0

        self.documents_added, self.documents_deleted = self.index_manager.search_documents()

        self.ui.info_new_documents_label.setText('Documentos a anadir:')
        self.ui.info_new_documents_value.setText(str(self.documents_added))

        self.ui.info_delete_documents_label.setText('Documentos a eliminar:')
        self.ui.info_delete_documents_value.setText(str(self.documents_deleted))

        self.ui.info_progress_status.setText('')
        self.ui.progress_bar.reset()
        self.ui.progress_bar.setValue(0)

        if self.documents_added + self.documents_deleted == 0:
            self.ui.action_button.setDisabled(True)
        else:
            self.ui.action_button.setText('Actualizar')

    def start_thread(self):
        if not self.updating:
            self.lock = allocate_lock()
            self.index_thread = start_new_thread(self.update_db, (self.lock,))

            # initialize info
            self.ui.info_box.setTitle(_from_Utf8('Procesando'))

            self.ui.info_new_documents_label.setText(_from_Utf8('Documentos añadidos:'))
            self.ui.info_new_documents_value.setText('0 de %d' % self.documents_added)

            self.ui.info_delete_documents_label.setText(_from_Utf8('Documentos eliminados:'))
            self.ui.info_delete_documents_value.setText('0 de %d' % self.documents_deleted)

            self.ui.action_button.setText('Cancelar')

            self.updating = True
        else:
            # cancel index
            self.index_manager.cancel_index()

            # update info
            self.ui.info_progress_status.setText(_from_Utf8('Cancelando...'))

            self.ui.progress_bar.setMinimum(0)
            self.ui.progress_bar.setMaximum(0)

    def update_db(self, lock):
        lock.acquire()
        self.index_manager.index()
        lock.release()

    def update_info(self, added, removed):
        self.added = added
        self.removed = removed

        self.ui.info_new_documents_value.setText('%d de %d' % (added, self.documents_added))
        self.ui.info_delete_documents_value.setText('%d de %d' % (removed, self.documents_deleted))

    def update_progress(self, state, value):
        self.ui.info_progress_status.setText(_from_Utf8(state))
        self.ui.progress_bar.setValue(value)

    def cancel_update_db(self):
        self.ui.info_progress_status.setText('Cancelado')

        self.ui.progress_bar.setMinimum(5)
        self.ui.progress_bar.setMaximum(100)
        self.ui.progress_bar.setValue(0)

        # update action button state
        self.ui.action_button.setText(_from_Utf8('Actualizar'))

        if self.added + self.removed == self.documents_added + self.documents_deleted:
            self.ui.action_button.setDisabled(True)
        else:
            self.ui.action_button.setEnabled(True)