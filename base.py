import sqlite3

connection = sqlite3.connect("oderman.db")

cursor = connection.cursor()

cursor.execute("""CREATE TABLE orders
                (id INTEGER PRIMARY KEY, name_pizza TEXT, user_name TEXT, address TEXT, phone TEXT)""")

connection.commit()
connection.close()