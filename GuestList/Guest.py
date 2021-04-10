import sqlite3

class Guest(object):
    
    #class_id = 0 #TODO zrobic tak, ze po wyjsciu i wejsc do programu liczyl nie od nowa!

    def __init__(self, name, surname, phone):
        #Guest.class_id+= 1
        #self.__id = Guest.class_id
        self.__name = name
        self.__surname = surname
        self.__phone = phone

    def maxIndex(self):
        db = sqlite3.connect('Guests.db')
        cur = db.cursor()

        id = str(cur.execute(f"SELECT MAX(id) from guest;"))
        print("Co to jest!: " + id)
        db.commit()
        db.close()
        return id

    #def getId(self):
        #return self.__id

    def getName(self):
        return self.__name

    def getSurname(self):
        return self.__surname

    def getPhone(self):
        return self.__phone

    #def setName(self, id):
        #self.__id = id

    def setName(self, name):
        self.__name = name

    def setSurname(self, surname):
        self.__surname = surname

    def setPhone(self, phone):
        self.__phone = phone
