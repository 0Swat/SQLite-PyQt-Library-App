from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

class MyCalculator(QMainWindow):
    def __init__(self):
        super(MyCalculator, self).__init__()

        self.DB()

        self.setGeometry(200, 200, 1200, 800)
        self.setWindowTitle("Biblioteka")
        self.setFixedSize(1200, 800)
        self.initUI()

        self.BooksLoad()
        self.PeopleLoad()
        self.BorrowedLoad()

    def initUI(self):
        self.AreaOne()
        self.AreaTwo()
        self.AreaThree()
        self.AreaFour()
        return
    
    def AreaOne(self):
        self.area1_label1 = QtWidgets.QLabel(self)
        self.area1_label1.setGeometry(QtCore.QRect(0, 0, 300, 50))
        self.area1_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.area1_label1.setText("Książki")
        self.area1_label1.setFont(QtGui.QFont('Arial', 22))

        self.area1_textBrowser1 = QtWidgets.QTextBrowser(self)
        self.area1_textBrowser1.setGeometry(QtCore.QRect(10, 60, 280, 330))
        self.area1_textBrowser1.setStyleSheet("border: 1px solid #777;") 

        self.area1_label2 = QtWidgets.QLabel(self)
        self.area1_label2.setGeometry(QtCore.QRect(300, 0, 300, 50))
        self.area1_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.area1_label2.setFont(QtGui.QFont('Arial', 14))

        self.area1_label3 = QtWidgets.QLabel(self)
        self.area1_label3.setGeometry(QtCore.QRect(300, 50, 300, 30))
        self.area1_label3.setAlignment(QtCore.Qt.AlignCenter)
        self.area1_label3.setText("Wprowadź tytuł")
        self.area1_label3.setFont(QtGui.QFont('Arial', 10))

        self.area1_lineEdit1 = QtWidgets.QLineEdit(self)
        self.area1_lineEdit1.setGeometry(QtCore.QRect(310, 80, 280, 30))
        self.area1_lineEdit1.setStyleSheet("border: 1px solid #777;") 

        self.area1_label4 = QtWidgets.QLabel(self)
        self.area1_label4.setGeometry(QtCore.QRect(300, 120, 300, 30))
        self.area1_label4.setAlignment(QtCore.Qt.AlignCenter)
        self.area1_label4.setText("Wprowadź autora")
        self.area1_label4.setFont(QtGui.QFont('Arial', 10))

        self.area1_lineEdit2 = QtWidgets.QLineEdit(self)
        self.area1_lineEdit2.setGeometry(QtCore.QRect(310, 150, 280, 30))
        self.area1_lineEdit2.setStyleSheet("border: 1px solid #777;") 

        self.area1_label5 = QtWidgets.QLabel(self)
        self.area1_label5.setGeometry(QtCore.QRect(300, 190, 300, 30))
        self.area1_label5.setAlignment(QtCore.Qt.AlignCenter)
        self.area1_label5.setText("Wprowadź gatunek")
        self.area1_label5.setFont(QtGui.QFont('Arial', 10))

        self.area1_lineEdit3 = QtWidgets.QLineEdit(self)
        self.area1_lineEdit3.setGeometry(QtCore.QRect(310, 220, 280, 30))
        self.area1_lineEdit3.setStyleSheet("border: 1px solid #777;") 

        self.area1_pushButton_1 = QtWidgets.QPushButton(self)
        self.area1_pushButton_1.setGeometry(QtCore.QRect(335, 285, 80, 80))
        self.area1_pushButton_1.setText("Dodaj")
        self.area1_pushButton_1.setFont(QtGui.QFont('Arial', 12))
        self.area1_pushButton_1.clicked.connect(self.BookAdd)

        self.area1_pushButton_2 = QtWidgets.QPushButton(self)
        self.area1_pushButton_2.setGeometry(QtCore.QRect(450+35, 250+35, 80, 80))
        self.area1_pushButton_2.setText("Usuń")
        self.area1_pushButton_2.setFont(QtGui.QFont('Arial', 12))
        self.area1_pushButton_2.clicked.connect(self.BookRemove)

    def AreaTwo(self):
        self.area2_label = QtWidgets.QLabel(self)
        self.area2_label.setGeometry(QtCore.QRect(600, 0, 600, 50))
        self.area2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.area2_label.setText("Pożyczone książki")
        self.area2_label.setFont(QtGui.QFont('Arial', 22))

        self.area2_textBrowser1 = QtWidgets.QTextBrowser(self)
        self.area2_textBrowser1.setGeometry(QtCore.QRect(610, 60, 280, 330))
        self.area2_textBrowser1.setObjectName("textBrowser")
        self.area2_textBrowser1.setStyleSheet("border: 1px solid #777;") 

        self.area2_label2 = QtWidgets.QLabel(self)
        self.area2_label2.setGeometry(QtCore.QRect(900, 50, 300, 50))
        self.area2_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.area2_label2.setText("Informacje o pożyczce")
        self.area2_label2.setFont(QtGui.QFont('Arial', 10))

        self.area2_label3 = QtWidgets.QLabel(self)
        self.area2_label3.setGeometry(QtCore.QRect(910, 100, 280, 280))
        self.area2_label3.setAlignment(QtCore.Qt.AlignCenter)
        self.area2_label3.setFont(QtGui.QFont('Arial', 12))
        self.area2_label3.setStyleSheet("border: 1px solid #777;") 
        self.area2_label3.setText("--- W BUDOWIE ---")

    def AreaThree(self):
        self.area3_label1 = QtWidgets.QLabel(self)
        self.area3_label1.setGeometry(QtCore.QRect(0, 400, 300, 50))
        self.area3_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.area3_label1.setText("Osoby")
        self.area3_label1.setFont(QtGui.QFont('Arial', 22))

        self.area3_textBrowser1 = QtWidgets.QTextBrowser(self)
        self.area3_textBrowser1.setGeometry(QtCore.QRect(10, 460, 280, 330))
        self.area3_textBrowser1.setObjectName("textBrowser")
        self.area3_textBrowser1.setStyleSheet("border: 1px solid #777;") 

        self.area3_label2 = QtWidgets.QLabel(self)
        self.area3_label2.setGeometry(QtCore.QRect(300, 400, 300, 50))
        self.area3_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.area3_label2.setFont(QtGui.QFont('Arial', 14))

        self.area3_label3 = QtWidgets.QLabel(self)
        self.area3_label3.setGeometry(QtCore.QRect(300, 450, 300, 30))
        self.area3_label3.setAlignment(QtCore.Qt.AlignCenter)
        self.area3_label3.setText("Wprowadź imię")
        self.area3_label3.setFont(QtGui.QFont('Arial', 10))

        self.area3_lineEdit1 = QtWidgets.QLineEdit(self)
        self.area3_lineEdit1.setGeometry(QtCore.QRect(300, 480, 280, 30))
        self.area3_lineEdit1.setStyleSheet("border: 1px solid #777;")

        self.area3_label4 = QtWidgets.QLabel(self)
        self.area3_label4.setGeometry(QtCore.QRect(300, 520, 300, 30))
        self.area3_label4.setAlignment(QtCore.Qt.AlignCenter)
        self.area3_label4.setText("Wprowadź nazwisko")
        self.area3_label4.setFont(QtGui.QFont('Arial', 10))

        self.area3_lineEdit2 = QtWidgets.QLineEdit(self)
        self.area3_lineEdit2.setGeometry(QtCore.QRect(300, 550, 280, 30))
        self.area3_lineEdit2.setStyleSheet("border: 1px solid #777;")

        self.area3_pushButton_1 = QtWidgets.QPushButton(self)
        self.area3_pushButton_1.setGeometry(QtCore.QRect(335, 625, 80, 80))
        self.area3_pushButton_1.setText("Dodaj")
        self.area3_pushButton_1.clicked.connect(self.PersonAdd)
        self.area3_pushButton_1.setFont(QtGui.QFont('Arial', 12))

        self.area3_pushButton_2 = QtWidgets.QPushButton(self)
        self.area3_pushButton_2.setGeometry(QtCore.QRect(485, 625, 80, 80))
        self.area3_pushButton_2.setText("Usuń")
        self.area3_pushButton_2.clicked.connect(self.PersonRemove)
        self.area3_pushButton_2.setFont(QtGui.QFont('Arial', 12))

    def AreaFour(self):
        self.area4_label1 = QtWidgets.QLabel(self)
        self.area4_label1.setGeometry(QtCore.QRect(600, 400, 600, 50))
        self.area4_label1.setAlignment(QtCore.Qt.AlignCenter)
        self.area4_label1.setText("Akcje")
        self.area4_label1.setFont(QtGui.QFont('Arial', 22))

        self.area4_label = QtWidgets.QLabel(self)
        self.area4_label.setGeometry(QtCore.QRect(600, 450, 600, 30))
        self.area4_label.setAlignment(QtCore.Qt.AlignCenter)
        self.area4_label.setFont(QtGui.QFont('Arial', 14))

        self.area4_label2 = QtWidgets.QLabel(self)
        self.area4_label2.setGeometry(QtCore.QRect(600, 480, 300, 30))
        self.area4_label2.setAlignment(QtCore.Qt.AlignCenter)
        self.area4_label2.setText("Książka")
        self.area4_label2.setStyleSheet("font-weight: bold;")
        self.area4_label2.setFont(QtGui.QFont('Arial', 12))

        self.area4_label3 = QtWidgets.QLabel(self)
        self.area4_label3.setGeometry(QtCore.QRect(600, 520, 300, 30))
        self.area4_label3.setAlignment(QtCore.Qt.AlignCenter)
        self.area4_label3.setText("Tytuł")
        self.area4_label3.setFont(QtGui.QFont('Arial', 10))

        self.area4_lineEdit1 = QtWidgets.QLineEdit(self)
        self.area4_lineEdit1.setGeometry(QtCore.QRect(610, 550, 280, 30))
        self.area4_lineEdit1.setStyleSheet("border: 1px solid #777;") 

        self.area4_label4 = QtWidgets.QLabel(self)
        self.area4_label4.setGeometry(QtCore.QRect(610, 590, 280, 30))
        self.area4_label4.setAlignment(QtCore.Qt.AlignCenter)
        self.area4_label4.setText("Autor")
        self.area4_label4.setFont(QtGui.QFont('Arial', 10))

        self.area4_lineEdit2 = QtWidgets.QLineEdit(self)
        self.area4_lineEdit2.setGeometry(QtCore.QRect(610, 620, 280, 30))
        self.area4_lineEdit2.setStyleSheet("border: 1px solid #777;") 

        self.area4_pushButton_1 = QtWidgets.QPushButton(self)
        self.area4_pushButton_1.setGeometry(QtCore.QRect(750, 685, 80, 80))
        self.area4_pushButton_1.setText("Pożycz")
        self.area4_pushButton_1.clicked.connect(self.BorrowBook)
        self.area4_pushButton_1.setFont(QtGui.QFont('Arial', 12))

        self.area4_label5 = QtWidgets.QLabel(self)
        self.area4_label5.setGeometry(QtCore.QRect(900, 480, 300, 30))
        self.area4_label5.setAlignment(QtCore.Qt.AlignCenter)
        self.area4_label5.setText("Osoba")
        self.area4_label5.setStyleSheet("font-weight: bold; color: black;")
        self.area4_label5.setFont(QtGui.QFont('Arial', 12))

        self.area4_label6 = QtWidgets.QLabel(self)
        self.area4_label6.setGeometry(QtCore.QRect(900, 520, 300, 30))
        self.area4_label6.setAlignment(QtCore.Qt.AlignCenter)
        self.area4_label6.setText("Imię")
        self.area4_label6.setFont(QtGui.QFont('Arial', 12))

        self.area4_lineEdit3 = QtWidgets.QLineEdit(self)
        self.area4_lineEdit3.setGeometry(QtCore.QRect(910, 550, 280, 30))
        self.area4_lineEdit3.setStyleSheet("border: 1px solid #777;") 

        self.area4_label7 = QtWidgets.QLabel(self)
        self.area4_label7.setGeometry(QtCore.QRect(900, 590, 300, 30))
        self.area4_label7.setAlignment(QtCore.Qt.AlignCenter)
        self.area4_label7.setText("Nazwisko")
        self.area4_label7.setFont(QtGui.QFont('Arial', 12))

        self.area4_lineEdit4 = QtWidgets.QLineEdit(self)
        self.area4_lineEdit4.setGeometry(QtCore.QRect(910, 620, 280, 30))
        self.area4_lineEdit4.setStyleSheet("border: 1px solid #777;") 

        self.area4_pushButton_2 = QtWidgets.QPushButton(self)
        self.area4_pushButton_2.setGeometry(QtCore.QRect(985, 685, 80, 80))
        self.area4_pushButton_2.setText("Oddaj")
        self.area4_pushButton_2.clicked.connect(self.UnBorrowBook)
        self.area4_pushButton_2.setFont(QtGui.QFont('Arial', 12))

    def DB(self):
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("library.sqlite")
        if not self.con.open():
            QMessageBox.critical(self, "Database Error", "Unable to connect to the database")
            self.area1_label2.setText("No data connection")
            self.area3_label2.setText("No data connection")
            self.area4_label.setText("No data connection")
            sys.exit(1)

        createTableQuery = QSqlQuery()
        createTableQuery.exec(
            """
            CREATE TABLE IF NOT EXISTS `ksiazki` (
            `id` INTEGER PRIMARY KEY,
            `tytul` TEXT,
            `autor` TEXT,
            `gatunek` TEXT
            );
            """
        )
        createTableQuery.exec(
            """
            CREATE TABLE IF NOT EXISTS `osoby` (
            `id` INTEGER PRIMARY KEY,
            `imie` TEXT,
            `nazwisko` TEXT
            );
            """
        )
        createTableQuery.exec(
            """
            CREATE TABLE IF NOT EXISTS `wypozyczenia` (
            `id` INTEGER PRIMARY KEY,
            `id_osoby` INTEGER,
            `id_ksiazki` INTEGER,
            FOREIGN KEY (`id_ksiazki`) REFERENCES `ksiazki` (`id`),
            FOREIGN KEY (`id_osoby`) REFERENCES `osoby` (`id`)
            );
            """
        )
    
    def BooksLoad(self):
        query = QSqlQuery()
        query.exec_("SELECT id, tytul, autor, gatunek FROM ksiazki")
        output = ""

        while query.next():
            id = query.value(0)
            title = '"' + query.value(1) + '"'
            author = query.value(2)
            genre = query.value(3)
            output += f"{id}. {title}, {author}, {genre}\n"

        self.area1_textBrowser1.setText(output)

    def BookAdd(self):
        tytul = self.area1_lineEdit1.text().strip()
        autor = self.area1_lineEdit2.text().strip()
        gatunek = self.area1_lineEdit3.text().strip()

        if tytul == "" or autor == "" or gatunek == "":
            self.area1_label2.setText("Podaj wszystkie dane!")
            return

        checkQuery = QSqlQuery()
        checkQuery.prepare("SELECT COUNT(*) FROM ksiazki WHERE tytul = :tytul")
        checkQuery.bindValue(":tytul", tytul)
        checkQuery.exec()

        if checkQuery.next():
            if checkQuery.value(0) > 0:
                self.area1_label2.setText("Taka książka już istnieje!")
                return 

        insertQuery = QSqlQuery()
        if insertQuery.exec(
                f"""INSERT INTO ksiazki (tytul, autor, gatunek)
                VALUES ('{tytul}', '{autor}', '{gatunek}')"""
        ):
            self.area1_label2.setText("Dodano!")
        else:
            self.area1_label2.setText("Błąd przy dodawaniu książki.")

        self.BooksLoad()

    def BookRemove(self):
        tytul = self.area1_lineEdit1.text().strip()
        autor = self.area1_lineEdit2.text().strip()
        gatunek = self.area1_lineEdit3.text().strip()

        if tytul == "" or autor == "" or gatunek == "":
            self.area1_label2.setText("Podaj wszystkie dane!")
            return

        checkQuery = QSqlQuery()
        checkQuery.prepare("SELECT COUNT(*) FROM ksiazki WHERE tytul = :tytul AND autor = :autor AND gatunek = :gatunek")
        checkQuery.bindValue(":tytul", tytul)
        checkQuery.bindValue(":autor", autor)
        checkQuery.bindValue(":gatunek", gatunek)
        checkQuery.exec()

        if checkQuery.next() and checkQuery.value(0) > 0:
            deleteQuery = QSqlQuery()
            deleteQuery.prepare("DELETE FROM ksiazki WHERE tytul = :tytul AND autor = :autor AND gatunek = :gatunek")
            deleteQuery.bindValue(":tytul", tytul)
            deleteQuery.bindValue(":autor", autor)
            deleteQuery.bindValue(":gatunek", gatunek)
            if deleteQuery.exec():
                self.area1_label2.setText("Usunięto książkę!")
            else:
                self.area1_label2.setText("Błąd przy usuwaniu książki.")
        else:
            self.area1_label2.setText("Nie znaleziono takiej książki.")

        self.BooksLoad()

    def PeopleLoad(self):
        query = QSqlQuery()
        query.exec_("SELECT id, imie, nazwisko FROM osoby")
        output = ""

        while query.next():
            id = query.value(0)
            imie = query.value(1)
            nazwisko = query.value(2)
            output += f"{id}. {imie} {nazwisko}\n"

        self.area3_textBrowser1.setText(output)
        
    def PersonAdd(self):
        imie = self.area3_lineEdit1.text().strip()
        nazwisko = self.area3_lineEdit2.text().strip()

        if imie == "" or nazwisko == "":
            self.area3_label2.setText("Podaj wszystkie dane!")
            return

        checkQuery = QSqlQuery()
        checkQuery.prepare("SELECT COUNT(*) FROM osoby WHERE imie = :imie AND nazwisko = :nazwisko")
        checkQuery.bindValue(":imie", imie)
        checkQuery.bindValue(":nazwisko", nazwisko)
        checkQuery.exec()

        if checkQuery.next():
            if checkQuery.value(0) > 0:
                self.area3_label2.setText("Taka osoba już istnieje!")
                return 

        insertQuery = QSqlQuery()
        if insertQuery.exec(
                f"""INSERT INTO osoby (imie, nazwisko)
                VALUES ('{imie}', '{nazwisko}')"""
        ):
            self.area3_label2.setText("Dodano!")
        else:
            self.area3_label2.setText("Błąd przy dodawaniu osoby.")

        self.PeopleLoad()

    def PersonRemove(self):
        imie = self.area3_lineEdit1.text().strip()
        nazwisko = self.area3_lineEdit2.text().strip()

        if imie == "" or nazwisko == "":
            self.area3_label2.setText("Podaj wszystkie dane!")
            return

        checkQuery = QSqlQuery()
        checkQuery.prepare("SELECT COUNT(*) FROM osoby WHERE imie = :imie AND nazwisko = :nazwisko")
        checkQuery.bindValue(":imie", imie)
        checkQuery.bindValue(":nazwisko", nazwisko)
        checkQuery.exec()

        if checkQuery.next() and checkQuery.value(0) > 0:
            deleteQuery = QSqlQuery()
            deleteQuery.prepare("DELETE FROM osoby WHERE imie = :imie AND nazwisko = :nazwisko")
            deleteQuery.bindValue(":imie", imie)
            deleteQuery.bindValue(":nazwisko", nazwisko)
            if deleteQuery.exec():
                self.area3_label2.setText("Usunięto osobę!")
            else:
                self.area3_label2.setText("Błąd przy usuwaniu osoby.")
        else:
            self.area3_label2.setText("Nie znaleziono takiej osoby.")

        self.PeopleLoad()

    def BorrowedLoad(self):
        query = QSqlQuery()
        query.exec_("SELECT wypozyczenia.id, osoby.imie, osoby.nazwisko, ksiazki.tytul, ksiazki.autor FROM osoby JOIN wypozyczenia ON osoby.id = wypozyczenia.id_osoby JOIN ksiazki ON ksiazki.id = wypozyczenia.id_ksiazki")

        output = ""

        while query.next():
            id = query.value(0)
            imie = query.value(1)
            nazwisko = query.value(2)
            tytul = '"' + query.value(3) + '"'
            autor = query.value(4)
            output += f"{id}. {imie} {nazwisko}: {tytul} - {autor}\n"

        self.area2_textBrowser1.setText(output)

    def BorrowBook(self):
        ksiazka = self.area4_lineEdit1.text().strip()
        autor = self.area4_lineEdit2.text().strip()
        imie = self.area4_lineEdit3.text().strip()
        nazwisko = self.area4_lineEdit4.text().strip()

        if ksiazka == "" or autor == "" or imie == "" or nazwisko == "":
            self.area4_label.setText("Podaj wszystkie dane!")
            return

        bookQuery = QSqlQuery()
        bookQuery.prepare("SELECT id FROM ksiazki WHERE tytul = :tytul AND autor = :autor")
        bookQuery.bindValue(":tytul", ksiazka)
        bookQuery.bindValue(":autor", autor)
        bookQuery.exec()
        
        book_id = None
        if bookQuery.next():
            book_id = bookQuery.value(0)
        else:
            self.area4_label.setText("Nie znaleziono książki!")
            return

        personQuery = QSqlQuery()
        personQuery.prepare("SELECT id FROM osoby WHERE imie = :imie AND nazwisko = :nazwisko")
        personQuery.bindValue(":imie", imie)
        personQuery.bindValue(":nazwisko", nazwisko)
        personQuery.exec()

        person_id = None
        if personQuery.next():
            person_id = personQuery.value(0)
        else:
            self.area4_label.setText("Nie znaleziono osoby!")
            return

        checkQuery = QSqlQuery()
        checkQuery.prepare("SELECT COUNT(*) FROM wypozyczenia WHERE id_ksiazki = :book_id")
        checkQuery.bindValue(":book_id", book_id)
        checkQuery.exec()
        if checkQuery.next() and checkQuery.value(0) > 0:
            self.area4_label.setText("Książka już wypożyczona!")
            return

        borrowQuery = QSqlQuery()
        borrowQuery.prepare("INSERT INTO wypozyczenia (id_osoby, id_ksiazki) VALUES (:person_id, :book_id)")
        borrowQuery.bindValue(":person_id", person_id)
        borrowQuery.bindValue(":book_id", book_id)
        if borrowQuery.exec():
            self.area4_label.setText("Książka wypożyczona pomyślnie!")
        else:
            self.area4_label.setText("Błąd przy wypożyczaniu książki.")

        self.BorrowedLoad()  
    
    def UnBorrowBook(self):
        ksiazka = self.area4_lineEdit1.text().strip()
        autor = self.area4_lineEdit2.text().strip()
        imie = self.area4_lineEdit3.text().strip()
        nazwisko = self.area4_lineEdit4.text().strip()

        if ksiazka == "" or autor == "" or imie == "" or nazwisko == "":
            self.area4_label.setText("Podaj wszystkie dane książki i osoby!")
            return

        bookQuery = QSqlQuery()
        bookQuery.prepare("SELECT id FROM ksiazki WHERE tytul = :tytul AND autor = :autor")
        bookQuery.bindValue(":tytul", ksiazka)
        bookQuery.bindValue(":autor", autor)
        bookQuery.exec()

        if not bookQuery.next():
            self.area4_label.setText("Nie znaleziono takiej książki!")
            return
        book_id = bookQuery.value(0)

        personQuery = QSqlQuery()
        personQuery.prepare("SELECT id FROM osoby WHERE imie = :imie AND nazwisko = :nazwisko")
        personQuery.bindValue(":imie", imie)
        personQuery.bindValue(":nazwisko", nazwisko)
        personQuery.exec()

        if not personQuery.next():
            self.area4_label.setText("Nie znaleziono takiej osoby!")
            return
        person_id = personQuery.value(0)

        borrowQuery = QSqlQuery()
        borrowQuery.prepare("SELECT id FROM wypozyczenia WHERE id_osoby = :person_id AND id_ksiazki = :book_id")
        borrowQuery.bindValue(":person_id", person_id)
        borrowQuery.bindValue(":book_id", book_id)
        borrowQuery.exec()

        if borrowQuery.next():
            borrow_id = borrowQuery.value(0)
            deleteQuery = QSqlQuery()
            deleteQuery.prepare("DELETE FROM wypozyczenia WHERE id = :borrow_id")
            deleteQuery.bindValue(":borrow_id", borrow_id)
            if deleteQuery.exec():
                self.area4_label.setText("Książka oddana pomyślnie!")
            else:
                self.area4_label.setText("Błąd przy oddawaniu książki.")
        else:
            self.area4_label.setText("Nie znaleziono wypożyczenia dla tej książki i osoby!")

        self.BorrowedLoad()


def window():
    app = QApplication(sys.argv)
    win = MyCalculator()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
