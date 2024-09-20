import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTimeEdit, QPushButton, QVBoxLayout, QWidget, QListWidgetItem, QListWidget, QTableWidgetItem, QDialog
from PyQt5 import QtWidgets
from PyQt5.QtCore import QTimer
import math
from window import Ui_MainWindow
from BDGO import baza
from create import Ui_create_window
from open import Ui_open_window

class Open(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_open_window()
        self.ui.setupUi(self)
        self.b = baza()
        self.ui.pushButton_2.clicked.connect(self.open_main)



    def open_main(self):
        open_win.close()
        main_window.show()
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.b = baza()
        self.show_partners()
        self.fill_combo_partners()
        self.show_product()
        self.fill_combo_product()
        self.show_history()
        self.fill_product_combo()
        self.fill_partner_combo_2()
        self.fill_combo_product_type()
        self.fill_combo_material_type()
        self.ui.pushButton.clicked.connect(self.edit)
        self.ui.tableWidget.itemClicked.connect(self.show_edit)
        self.ui.pushButton_2.clicked.connect(self.open_create)
        self.ui.pushButton_3.clicked.connect(self.delete_partner)
        self.ui.pushButton_4.clicked.connect(self.show_partners)
        self.ui.pushButton_4.clicked.connect(self.fill_combo_partners)
        self.ui.pushButton_4.clicked.connect(self.ui.label_2.clear)
        self.ui.pushButton_5.clicked.connect(self.add_product)
        self.ui.pushButton_8.clicked.connect(self.show_product)
        self.ui.pushButton_8.clicked.connect(self.fill_combo_product)
        self.ui.pushButton_7.clicked.connect(self.delete_product)
        self.ui.pushButton_6.clicked.connect(self.edit_product)
        self.ui.tableWidget_2.itemClicked.connect(self.show_edit_product)
        self.ui.comboBox_4.currentTextChanged.connect(self.show_history_bypartner)
        self.ui.comboBox_3.currentTextChanged.connect(self.show_history_byproduct)
        self.ui.pushButton_10.clicked.connect(self.clear_filter)
        self.ui.pushButton_12.clicked.connect(self.calculate)


    def open_create(self):
        create_win.show()

    def show_partners(self):
        # Получаем все объекты и описание столбцов из базы данных
        objects, column_description = self.b.show_partners()

        # Определяем количество строк и столбцов в таблице
        num_rows = len(objects)
        num_cols = len(column_description)

        # Устанавливаем количество строк и столбцов в таблице
        self.ui.tableWidget.setRowCount(num_rows)
        self.ui.tableWidget.setColumnCount(num_cols)

        # Заполняем заголовки столбцов таблицы
        column_headers = [column[0] for column in column_description]
        self.ui.tableWidget.setHorizontalHeaderLabels(column_headers)

        # Заполняем ячейки таблицы данными из объектов
        for i, row in enumerate(objects):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget.setItem(i, j, item)

    def fill_combo_partners(self):
        self.ui.comboBox.clear()
        values = self.b.out_partner_name()
        for value in values:
            self.ui.comboBox.addItem(value[0])

    def delete_partner(self):
        partner = self.ui.comboBox.currentText()
        self.b.drop_partner(partner)
        self.ui.label_2.setText("Партнер удален.Обновите таблицу.")
        self.ui.label_2.adjustSize()


    def edit(self):
        select = self.ui.tableWidget.selectedIndexes()
        if select:
            row = select[0].row()
            col = select[0].column()
            key = self.ui.tableWidget.item(row, 1).text()

            # Получение текста из строки редактирования
            new_text = self.ui.lineEdit.text()

            # Обновление ячейки
            self.ui.tableWidget.setItem(row, col, QTableWidgetItem(new_text))

            column_name = self.ui.tableWidget.horizontalHeaderItem(col).text()

            self.b.edit(new_text, column_name, key)


            # Очистка строки редактирования
            self.ui.lineEdit.clear()
            self.ui.label_2.setText("Данные изменены! Обновите таблицу")
            self.ui.label_2.adjustSize()

    def show_edit(self):
        select = self.ui.tableWidget.selectedIndexes()
        if select:
            row = select[0].row()
            col = select[0].column()

            cell_text = self.ui.tableWidget.item(row, col).text()

            # Отображение текста в строке редактирования
            self.ui.lineEdit.setText(cell_text)

############  ПРОДУКЦИЯ  ###########

    def show_product(self):
        # Получаем все объекты и описание столбцов из базы данных
        objects, column_description = self.b.show_product()

        # Определяем количество строк и столбцов в таблице
        num_rows = len(objects)
        num_cols = len(column_description)

        # Устанавливаем количество строк и столбцов в таблице
        self.ui.tableWidget_2.setRowCount(num_rows)
        self.ui.tableWidget_2.setColumnCount(num_cols)

        # Заполняем заголовки столбцов таблицы
        column_headers = [column[0] for column in column_description]
        self.ui.tableWidget_2.setHorizontalHeaderLabels(column_headers)

        # Заполняем ячейки таблицы данными из объектов
        for i, row in enumerate(objects):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget_2.setItem(i, j, item)


    def add_product(self):
        type = self.ui.comboBox_5.currentText()
        name = self.ui.lineEdit_4.text()
        article = self.ui.lineEdit_5.text()
        min_price = self.ui.lineEdit_6.text()


        if not type or not name or not article or not min_price:
            self.ui.label_5.setText("Заполните все поля")
            self.ui.label_5.adjustSize()
            return

        self.b.add_product(type, name, article, min_price)
        self.ui.label_5.setText("Продукт добавлен! Обновите таблицу")
        self.ui.label_5.adjustSize()

    def fill_combo_product(self):
        self.ui.comboBox_2.clear()
        values = self.b.out_product_name()
        for value in values:
            self.ui.comboBox_2.addItem(value[0])

    def delete_product(self):
        product = self.ui.comboBox_2.currentText()
        self.b.drop_product(product)
        self.ui.label_5.setText("Продукт удален.Обновите таблицу.")
        self.ui.label_5.adjustSize()

    def edit_product(self):
        select = self.ui.tableWidget_2.selectedIndexes()
        if select:
            row = select[0].row()
            col = select[0].column()
            key = self.ui.tableWidget_2.item(row, 1).text()

            # Получение текста из строки редактирования
            new_text = self.ui.lineEdit_2.text()

            # Обновление ячейки
            self.ui.tableWidget_2.setItem(row, col, QTableWidgetItem(new_text))

            column_name = self.ui.tableWidget_2.horizontalHeaderItem(col).text()

            self.b.edit_product(new_text, column_name, key)


            # Очистка строки редактирования
            self.ui.lineEdit_2.clear()
            self.ui.label_5.setText("Данные изменены! Обновите таблицу")
            self.ui.label_5.adjustSize()

    def show_edit_product(self):
        select = self.ui.tableWidget_2.selectedIndexes()
        if select:
            row = select[0].row()
            col = select[0].column()

            cell_text = self.ui.tableWidget_2.item(row, col).text()

            # Отображение текста в строке редактирования
            self.ui.lineEdit_2.setText(cell_text)

################# ИСТОРИЯ ПРОДАЖ ####################

    def show_history(self):
        # Получаем все объекты и описание столбцов из базы данных
        objects, column_description = self.b.show_history()

        # Определяем количество строк и столбцов в таблице
        num_rows = len(objects)
        num_cols = len(column_description)

        # Устанавливаем количество строк и столбцов в таблице
        self.ui.tableWidget_3.setRowCount(num_rows)
        self.ui.tableWidget_3.setColumnCount(num_cols)

        # Заполняем заголовки столбцов таблицы
        column_headers = [column[0] for column in column_description]
        self.ui.tableWidget_3.setHorizontalHeaderLabels(column_headers)

        # Заполняем ячейки таблицы данными из объектов
        for i, row in enumerate(objects):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget_3.setItem(i, j, item)

    def fill_product_combo(self):
        values = self.b.out_product_history()
        for value in values:
            self.ui.comboBox_3.addItem(value[0])


    def fill_partner_combo_2(self):
        values = self.b.out_partner_name()
        for value in values:
            self.ui.comboBox_4.addItem(value[0])

    def show_history_bypartner(self):
        partner = self.ui.comboBox_4.currentText()
        # Получаем все объекты и описание столбцов из базы данных
        objects, column_description = self.b.show_history_bypartner(partner)

        # Определяем количество строк и столбцов в таблице
        num_rows = len(objects)
        num_cols = len(column_description)

        # Устанавливаем количество строк и столбцов в таблице
        self.ui.tableWidget_3.setRowCount(num_rows)
        self.ui.tableWidget_3.setColumnCount(num_cols)

        # Заполняем заголовки столбцов таблицы
        column_headers = [column[0] for column in column_description]
        self.ui.tableWidget_3.setHorizontalHeaderLabels(column_headers)

        # Заполняем ячейки таблицы данными из объектов
        for i, row in enumerate(objects):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget_3.setItem(i, j, item)

    def show_history_byproduct(self):
        product = self.ui.comboBox_3.currentText()
        # Получаем все объекты и описание столбцов из базы данных
        objects, column_description = self.b.show_history_byproduct(product)

        # Определяем количество строк и столбцов в таблице
        num_rows = len(objects)
        num_cols = len(column_description)

        # Устанавливаем количество строк и столбцов в таблице
        self.ui.tableWidget_3.setRowCount(num_rows)
        self.ui.tableWidget_3.setColumnCount(num_cols)

        # Заполняем заголовки столбцов таблицы
        column_headers = [column[0] for column in column_description]
        self.ui.tableWidget_3.setHorizontalHeaderLabels(column_headers)

        # Заполняем ячейки таблицы данными из объектов
        for i, row in enumerate(objects):
            for j, value in enumerate(row):
                item = QTableWidgetItem(str(value))
                self.ui.tableWidget_3.setItem(i, j, item)

    def clear_filter(self):
        self.show_history()
        self.ui.comboBox_3.setCurrentIndex(0)
        self.ui.comboBox_4.setCurrentIndex(0)



############  Материалы ###########

    def fill_combo_product_type(self):
        self.ui.comboBox_6.clear()
        values = self.b.out_product_type()
        for value in values:
            self.ui.comboBox_6.addItem(value[0])

    def fill_combo_material_type(self):
        self.ui.comboBox_7.clear()
        values = self.b.out_material_type()
        for value in values:
            self.ui.comboBox_7.addItem(value[0])


    def calculate(self):
        material = self.ui.comboBox_7.currentText()
        product = self.ui.comboBox_6.currentText()
        value = self.ui.spinBox.value()
        defect_percentages = {
            "Тип материала 1": 0.001,
            "Тип материала 2": 0.0095,
            "Тип материала 3": 0.0028,
            "Тип материала 4": 0.0055,
            "Тип материала 5": 0.0034
        }

        material_requirements = {
            "Ламинат": {
                "Тип материала 1": 2,  # Например, 2 единицы материала 1 для ламината
                "Тип материала 2": 3,  # Например, 3 единицы материала 2 для ламината
                "Тип материала 3": 1,  # ...
                "Тип материала 4": 4,
                "Тип материала 5": 5
            },
            "Паркетная доска": {
                "Тип материала 1": 1.5,  # Например, 1.5 единицы материала 1 для паркетной доски
                "Тип материала 2": 2.5,
                "Тип материала 3": 1,
                "Тип материала 4": 3,
                "Тип материала 5": 4
            },
            "Пробковое покрытие": {
                "Тип материала 1": 2.2,  # Например, 2.2 единицы материала 1 для пробкового покрытия
                "Тип материала 2": 3.1,
                "Тип материала 3": 1.2,
                "Тип материала 4": 4.5,
                "Тип материала 5": 5.3
            }
        }

        defect_percentage = defect_percentages[material]
        material_need = material_requirements[product][material]
        sum = math.ceil(value*material_need/(1-defect_percentage))
        self.ui.label_16.setText(f"Для изготовления {value}  изделий типа {product} \nнеобходимо {sum} единиц {material}" )
        self.ui.label_16.adjustSize()


class AddPartner(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_create_window()
        self.ui.setupUi(self)
        self.b = baza()
        self.ui.pushButton.clicked.connect(self.add_partner)
        self.setWindowTitle("Добавление партнера")

    def add_partner(self):
        type = self.ui.comboBox.currentText()
        name = self.ui.lineEdit_2.text()
        director = self.ui.lineEdit_3.text()
        email = self.ui.lineEdit_4.text()
        phone = self.ui.lineEdit_5.text()
        address = self.ui.lineEdit_6.text()
        inn = self.ui.lineEdit_7.text()

        if not type or not name or not email or not address or not inn or not phone or not director:
            self.ui.label.setText("Заполните все поля")
            self.ui.label.adjustSize()
            return

        self.b.add(type, name, director, email, phone, address, inn)
        create_win.close()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    create_win = AddPartner()
    open_win=Open()
    open_win.show()
    sys.exit(app.exec_())