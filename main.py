from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
import sys

class MyCalculator(QMainWindow):
    def __init__(self):
        super(MyCalculator, self).__init__()
        self.setGeometry(200, 200, 800, 500)
        self.setWindowTitle("Biblioteka")
        self.setFixedSize(800, 500)

        self.DB()
        self.initUI()

    def DB(self):
        self.con = QSqlDatabase.addDatabase("QSQLITE")
        self.con.setDatabaseName("library.sqlite")
        if not self.con.open():
            QMessageBox.critical(self, "Database Error", "Unable to connect to the database")
            sys.exit(1)

        createTableQuery = QSqlQuery()
        createTableQuery.exec(
            """
            CREATE TABLE `ksiazki` (
            `id` integer PRIMARY KEY,
            `tytul` varchar(255),
            `autor_imie` varchar(255),
            `autor_nazwisko` varchar(255),
            `gatunek` varchar(255)
            );
            """
        )
        createTableQuery.exec(
            """
            CREATE TABLE `osoby` (
            `id` integer PRIMARY KEY,
            `imie` varchar(255),
            `nazwisko` varchar(255)
            );
            """
        )
        createTableQuery.exec(
            """
            CREATE TABLE `wypozyczenia` (
            `id` integer,
            `id_osoby` integer,
            `id_ksiazki` integer
            );
            """
        )
        createTableQuery.exec(
            """
            ALTER TABLE `wypozyczenia` ADD FOREIGN KEY (`id_ksiazki`) REFERENCES `ksiazki` (`id`);
            """
        )
        createTableQuery.exec(
            """
            ALTER TABLE `wypozyczenia` ADD FOREIGN KEY (`id_osoby`) REFERENCES `osoby` (`id`);
            """
        )

        id = 1
        imie = "Oskar"
        nazwisko = "Swat"

        query = QSqlQuery()
        query.exec(
            f"""INSERT INTO osoby (id, imie, nazwisko)
            VALUES ('{id}', '{imie}', '{nazwisko}')"""
        )
        query.exec(
            f"""INSERT INTO ksiazki (id, tytul, autor_imie, autor_nazwisko, gatunek)
            VALUES ('1', 'Krzyzacy', 'Boleslaw', 'Prus', 'historyczne')"""
        )
        query.exec(
            f"""INSERT INTO wypozyczenia (id, id_osoby, id_ksiazki)
            VALUES ('1', '1', '1')"""
        )


    def initUI(self):
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(10, 10, 780, 480)
        self.tableWidget.setColumnCount(5)  # Liczba kolumn odpowiadająca tabeli `osoby`
        self.tableWidget.setHorizontalHeaderLabels(["ID", "Imię", "Nazwisko", "Tytuł Książki", "Gatunek"])

        query = QSqlQuery("SELECT osoby.id, osoby.imie, osoby.nazwisko, ksiazki.tytul, ksiazki.gatunek FROM osoby JOIN wypozyczenia ON osoby.id = wypozyczenia.id_osoby JOIN ksiazki ON ksiazki.id = wypozyczenia.id_ksiazki")
        row = 0
        while query.next():
            self.tableWidget.insertRow(row)
            for i in range(5):
                self.tableWidget.setItem(row, i, QTableWidgetItem(str(query.value(i))))
            row += 1

def window():
    app = QApplication(sys.argv)
    win = MyCalculator()
    win.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    window()
