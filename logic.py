from PyQt6.QtWidgets import *
from gui import *
from television import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        tv = Television()
        
        self.power_button.clicked.connect(lambda : tv.power())