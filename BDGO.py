import sys
import pymysql
import os
global current
class baza:
    def __init__(self):
        self.connection = pymysql.connect(host='localhost',
                                          user='root',
                                          password='',
                                          database='files')
        try:
            with self.connection:
                self.cr = self.connection.cursor()
                self.cr.execute("SELECT VERSION()")
                version = self.cr.fetchone()
                print("Database version: {}".format(version[0]))
                print(self.connection.get_server_info())

        except:
            sys.exit()

    def show_partners(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM partners_import"
        cursor.execute(query)
        objects = cursor.fetchall()
        column_description = cursor.description
        return objects, column_description

    def drop_partner(self, fio):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"DELETE FROM partners_import WHERE partner_name = '{fio}'"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def edit(self, new_text, col, key):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"UPDATE partners_import SET {col} = %s WHERE partner_name = %s"
        cursor.execute(query, (new_text, key))
        connection.commit()
        connection.close()

    def out_partner_name(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"SELECT partner_name FROM partners_import "
        cursor.execute(query)
        result = cursor.fetchall()
        return result


    def add(self, type, name, director, email, phone, address, inn):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()

        query = "INSERT INTO partners_import (type, partner_name, director, email, phone, address, INN) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        mem = (type, name, director, email, phone, address, inn)
        cursor.execute(query, mem)
        connection.commit()
        connection.close()
        result = cursor.fetchone()
        return result

    def show_product(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM products_import"
        cursor.execute(query)
        objects = cursor.fetchall()
        column_description = cursor.description
        return objects, column_description

    def add_product(self, type, name, article, min_price):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()

        query = "INSERT INTO products_import (product_type, product_name, article, min_price) VALUES (%s, %s, %s, %s)"
        mem = (type, name, article, min_price)
        cursor.execute(query, mem)
        connection.commit()
        connection.close()
        result = cursor.fetchone()
        return result

    def out_product_name(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"SELECT product_name FROM products_import "
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def drop_product(self, fio):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"DELETE FROM products_import WHERE product_name = '{fio}'"
        cursor.execute(query)
        connection.commit()
        connection.close()

    def edit_product(self, new_text, col, key):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"UPDATE products_import SET {col} = %s WHERE product_name = %s"
        cursor.execute(query, (new_text, key))
        connection.commit()
        connection.close()

    def show_history(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM partner_products_import"
        cursor.execute(query)
        objects = cursor.fetchall()
        column_description = cursor.description
        return objects, column_description

    def out_product_type(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"SELECT DISTINCT product_type FROM products_import "
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def out_material_type(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"SELECT material_type FROM material_type_import "
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def out_product_from_type(self, type):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"SELECT product_name FROM products_import WHERE product_type = %s  "
        cursor.execute(query, type)
        result = cursor.fetchall()
        return result

    def out_partner_from_product(self, product):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"SELECT partner_name FROM partner_products_import WHERE product_name = %s "
        cursor.execute(query, product)
        result = cursor.fetchall()
        return result


    def show_history_bypartner(self, partner):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM partner_products_import WHERE partner_name = %s"
        cursor.execute(query, partner)
        objects = cursor.fetchall()
        column_description = cursor.description
        return objects, column_description

    def out_product_history(self):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = f"SELECT DISTINCT product_name FROM partner_products_import "
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    def show_history_byproduct(self, partner):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM partner_products_import WHERE product_name = %s"
        cursor.execute(query, partner)
        objects = cursor.fetchall()
        column_description = cursor.description
        return objects, column_description

    def filter_date(self, start, end):
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            database="files"
        )
        cursor = connection.cursor()
        query = "SELECT * FROM partner_products_import WHERE date BETWEEN %s AND %s"
        cursor.execute(query, (start, end))
        objects = cursor.fetchall()
        column_description = cursor.description
        return objects, column_description