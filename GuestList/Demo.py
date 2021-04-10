from InterfaceDB import InterfaceDB
from Guest import Guest



if __name__ == "__main__":
    interfaceDB = InterfaceDB()

    def listOfAllGuests():
        interfaceDB.selectGuests()

    def addAGuest():
        name = input("Write a name: ")
        surname = input("Write a surname: ")
        phone = input("Write a phone number: ")

        guest = Guest(name, surname, phone)
        interfaceDB.addGuest(guest)

    def updateGuest():
        interfaceDB.selectGuests()

        id = input("Which person want to update? Chose id: ")
        name = input("Write a name: ")
        surname = input("Write a surname: ")
        phone = input("Write a phone number: ")

        guest = Guest(name, surname, phone)

        interfaceDB.updateGuest(id, guest)


    def deleteGuest():
        interfaceDB.selectGuests()
        
        id = input("Which person want to delete? Chose id: ")
        interfaceDB.deleteGuest(id)
    
    while(True):
        print("""
        1. List of all guests
        2. Add a guest
        3. Change the data of guest
        4. Remove a guest
        """)
        option = input("Please, chose the option from 1 to 4, or q/Q = quit\n")
        if option == "1":
            listOfAllGuests()

        elif option == "2":
            addAGuest()

        elif option == "3":
            updateGuest()

        elif option == "4":
            deleteGuest()

        elif option[0].lower() == "q":
            break
        else: #TODO wyrzucmy tu wyjatek :)
            print("THIS OPTION DOES NOT EXIST!")

