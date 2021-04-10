import sqlite3
from Guest import Guest

class InterfaceDB(object):

    def __init__(self):
        pass

    def selectGuests(self):

        db = sqlite3.connect('Guests.db')
        cur = db.cursor()
        datas = cur.execute("SELECT * FROM guest")
        #
        listDB = []
        #
        for i in datas:
            print(i)
            listDB.append(i)
        db.close()
        #
        return listDB
        #
    def addGuest(self, guest):
        db = sqlite3.connect('Guests.db')
        cur = db.cursor()

        cur.execute(f"INSERT INTO guest (name, surname, phone) VALUES ('{guest.getName()}', '{guest.getSurname()}', '{guest.getPhone()}')")

        db.commit()
        db.close()

    def updateGuest(self, id, guest):
        db = sqlite3.connect('Guests.db')
        cur = db.cursor()

        cur.execute(f"UPDATE guest SET name = '{guest.getName()}', surname = '{guest.getSurname()}' , phone = '{guest.getPhone()}'  WHERE id = '{id}'")

        db.commit()
        db.close()

    def deleteGuest(self, id):
        db = sqlite3.connect('Guests.db')
        cur = db.cursor()

        cur.execute(f"DELETE FROM guest WHERE id = '{id}'")

        db.commit()
        db.close()

    

