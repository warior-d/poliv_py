from PyQt5.QtWidgets import QDialog, QHBoxLayout, QLabel, QWidget, QApplication, \
    QAction, qApp, QPushButton, QDesktopWidget, QComboBox, QProgressBar, QLineEdit, \
    QSpacerItem, QVBoxLayout, QGroupBox
import os
from PyQt5 import uic



class MainWidget(QWidget):

    def __init__(self):
        super().__init__()
        uic.loadUi('widj.ui', self)
        #self.label_2.setText()



if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)

    window = MainWidget()
    window.show()
    sys.exit(app.exec_())