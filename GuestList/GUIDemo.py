import tkinter as tk

from InterfaceDB import InterfaceDB
from Guest import Guest


def select_list_of_guest():
    listDB = interfaceDB.selectGuests()
    list_box.delete(0, tk.END) 
    
    list_box.insert(tk.END,"ID | NAME | SURNAME | PHONE_NUMBER")
    for guest in listDB:
    
        list_box.insert(tk.END, f"{guest}")

def add_to_list():
    guest = Guest(entry_name.get(), entry_surname.get(), entry_phone.get())
    print(entry_name.get(), entry_surname.get(), entry_phone.get())
    interfaceDB.addGuest(guest)

def update_list():
    list_from_the_list = str(list_box.get(tk.ANCHOR))
    list_from_the_list = list_from_the_list.split(',')
    id = list_from_the_list[0][1:]

    guest = Guest(entry_name_update.get(), entry_surname_update.get(), entry_phone_update.get())
    print(entry_name_update.get(), entry_surname_update.get(), entry_phone_update.get())
    interfaceDB.updateGuest(id, guest)

def remove_from_list():
    list_from_the_list = str(list_box.get(tk.ANCHOR))
    list_from_the_list = list_from_the_list.split(',')
    id = list_from_the_list[0][1:]
    interfaceDB.deleteGuest(id)

##########################################
window = tk.Tk()
window.geometry("640x480")

interfaceDB = InterfaceDB()

########################################
list_box = tk.Listbox(window)
list_box.pack(ipadx=70, ipady=100, side=tk.LEFT)

select_list_of_guest()

##########################################

entry_name = tk.Entry(window)
entry_name.pack()
entry_surname = tk.Entry(window)
entry_surname.pack()
entry_phone = tk.Entry(window)
entry_phone.pack()
##########################################
button_add = tk.Button(window, text = 'Add guest',
                          command = lambda:[add_to_list() ,select_list_of_guest()])

button_add.pack()


##########################################

entry_name_update = tk.Entry(window)
entry_name_update.pack()
entry_surname_update = tk.Entry(window)
entry_surname_update.pack()
entry_phone_update = tk.Entry(window)
entry_phone_update.pack()
##########################################
button_update = tk.Button(window, text = 'Update guest',
                          command = lambda:[update_list() ,select_list_of_guest()])

button_update.pack()

##########################################
button_delete = tk.Button(window, text = 'Delete guest',
                          command = lambda:[remove_from_list() ,select_list_of_guest()])

button_delete.pack()
##########################################
window.mainloop()