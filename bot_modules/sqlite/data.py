import sqlite3
import aiogram

connect = sqlite3.connect(__file__ + '/../data/data.db')

cursor = connect.cursor()

cursor.execute('CREATE TABLE IF NOT EXISTS admins(email TEXT, username TEXT, number INTEGER, password TEXT, id INTEGER PRIMARY KEY)')


connect.commit()
connect.close()