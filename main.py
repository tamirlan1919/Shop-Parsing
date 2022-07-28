import sys
from PyQt5 import *

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget
from shop import Ui_MainWindow
import requests
from bs4 import BeautifulSoup as bs
import pandas as pd




app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
MainWindow.show()
sys.exit(app.exec())
