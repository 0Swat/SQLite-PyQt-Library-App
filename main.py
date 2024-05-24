from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

class MyCalculator(QMainWindow):
    def __init__(self):
        super(MyCalculator, self).__init__()
        self.setGeometry(200, 200, 1200, 800)
        self.setWindowTitle("Biblioteka")
        self.setFixedSize(1200, 800)

        

        self.initUI()

    def initUI(self):
        self.AreaOne()
        return
    
    def AreaOne(self):
        self.label1 = QtWidgets.QLabel(self)
        self.label1.setGeometry(QtCore.QRect(0, 0, 300, 50))
        self.label1.setAlignment(QtCore.Qt.AlignCenter)
        self.label1.setText("Książki")
        self.label1.setStyleSheet("color: black; border: 1px solid #ccc;")
        self.label1.setFont(QtGui.QFont('Arial', 22))

        self.textBrowser1 = QtWidgets.QTextBrowser(self)
        self.textBrowser1.setGeometry(QtCore.QRect(0, 50, 300, 350))
        self.textBrowser1.setObjectName("textBrowser")

        self.label2 = QtWidgets.QLabel(self)
        self.label2.setGeometry(QtCore.QRect(300, 0, 300, 50))
        self.label2.setAlignment(QtCore.Qt.AlignCenter)
        self.label2.setText("No data connection")
        self.label2.setStyleSheet("color: black; border: 1px solid #ccc;")
        self.label2.setFont(QtGui.QFont('Arial', 14))

        self.label3 = QtWidgets.QLabel(self)
        self.label3.setGeometry(QtCore.QRect(300, 50, 300, 30))
        self.label3.setAlignment(QtCore.Qt.AlignCenter)
        self.label3.setText("Wprowadź tytuł")
        self.label3.setStyleSheet("color: black; border: 1px solid #ccc;")
        self.label3.setFont(QtGui.QFont('Arial', 8))

        self.lineEdit1 = QtWidgets.QLineEdit(self)
        self.lineEdit1.setGeometry(QtCore.QRect(300, 80, 300, 30))

        self.label4 = QtWidgets.QLabel(self)
        self.label4.setGeometry(QtCore.QRect(300, 120, 300, 30))
        self.label4.setAlignment(QtCore.Qt.AlignCenter)
        self.label4.setText("Wprowadź autora")
        self.label4.setStyleSheet("color: black; border: 1px solid #ccc;")
        self.label4.setFont(QtGui.QFont('Arial', 8))

        self.lineEdit2 = QtWidgets.QLineEdit(self)
        self.lineEdit2.setGeometry(QtCore.QRect(300, 150, 300, 30))

        self.label5 = QtWidgets.QLabel(self)
        self.label5.setGeometry(QtCore.QRect(300, 190, 300, 30))
        self.label5.setAlignment(QtCore.Qt.AlignCenter)
        self.label5.setText("Wprowadź gatunek")
        self.label5.setStyleSheet("color: black; border: 1px solid #ccc;")
        self.label5.setFont(QtGui.QFont('Arial', 8))

        self.lineEdit3 = QtWidgets.QLineEdit(self)
        self.lineEdit3.setGeometry(QtCore.QRect(300, 220, 300, 30))

        self.pushButton_1 = QtWidgets.QPushButton(self)
        self.pushButton_1.setGeometry(QtCore.QRect(300, 250, 150, 150))
        self.pushButton_1.setText("Dodaj")

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(450, 250, 150, 150))
        self.pushButton_2.setText("Usuń")



def window():
    app = QApplication(sys.argv)
    win = MyCalculator()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
