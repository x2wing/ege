# import PyQt5
import sys
from PyQt5.QtWidgets import QApplication, QWidget




class MyListModel(QAbstractListModel):
    def__init__(self, parent=None):
        super(MyListModel, self).__init__(parent)
        self._data = [70, 90, 20, 50]
    def rowCount(self, parent=QModelIndex()):
        return len (self._data)
    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or\
           not 0 <= index.row() < self.rowCount():
            return QVariant()
        row = index.row()
        if role == Qt.DisplayRole:
            return str(self._data[row])
        return QVariant()






class AWidget(QWidget):
    def __init__(self, parent=None):
        super(AWidget, self).__init__(parent)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = AWidget()
    win.show()
    sys.exit(app.exec_())