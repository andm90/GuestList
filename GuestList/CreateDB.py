import sqlite3

db = sqlite3.connect('Guests.db')

cur = db.cursor()

cur.execute('''CREATE TABLE guest
               (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, surname TEXT, phone TEXT)''')

db.close()