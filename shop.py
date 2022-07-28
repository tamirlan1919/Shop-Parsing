# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'shop.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import csv
import pandas as pd
import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from bs4 import BeautifulSoup

class Ui_MainWindow(object):w):
    def setupUi(self, MainWindo
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(395, 466)
        MainWindow.setStyleSheet("background-color:#22222f;\n"
"")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 280, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color:#d3574b;\n"
"color:white;\n"
"font-size:20px;\n"
"border-radius:12px;\n"
"")
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(90, 120, 231, 51))
        self.textEdit.setStyleSheet("color:white;\n"
"border:1px solid #ff695b;\n"
"border-radius:12px;\n"
"font-size:18px;\n"
"")
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 361, 61))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setStyleSheet("QLabel{\n"
"color:white;\n"
"text-align:center\n"
"}")
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        self.pushButton.clicked.connect(self.othvat)
    def othvat(self):
        x = self.textEdit.toPlainText() #Сохранение значени в переменную x
        y = x.replace(' ','+')
        URL_TEMPLATE2 = f"https://www.citilink.ru/search/?text={y}"

        print(URL_TEMPLATE2)
        responce = requests.get(URL_TEMPLATE2)
        soup2 = BeautifulSoup(responce.text, 'html.parser')
        tech_laptop = soup2.find_all('a', class_='ProductCardVertical__name')
        tech_laptop_price = soup2.find_all('span', class_='ProductCardVerticalPrice__price-current_current-price')
        print('--------------------------------------------------------------------------------------------------------------')
        self.lst1 = []
        self.lst2 = []
        for item, item1 in zip(tech_laptop, tech_laptop_price):
            print(item.text + '   :Цена - ' + item1.text.strip())
            self.lst1.append(item.text)
            self.lst2.append(item1.text.strip())
        print('--------------------------------------------------------------------------------------------------------------')
        print(self.lst1)
        print(self.lst2)
        self.save()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "ВЫГРУЗИТЬ В ФАЙЛ"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\">ПО ДЛЯ ПАРСИНГА ЦЕН</p><p align=\"center\">ЦЕН В РАЗНЫХ ИНТЕРНЕТ-МАГАЗИНАХ</p></body></html>"))


    def save(self):
        shop = {'Name':self.lst1,
                'Price':self.lst2}
        shop_df = pd.DataFrame(shop)
        shop_df.to_csv('university_records.csv',index=False,encoding="utf-8-sig",header=True)
        writer = pd.ExcelWriter('output.xlsx')
        # write dataframe to excel
        shop_df.to_excel(writer)
        # save the excel
        writer.save()
        print('DataFrame is written successfully to Excel File.')