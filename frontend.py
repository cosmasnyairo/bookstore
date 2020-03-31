# libraries
from tkinter import *

# files
import backend


def get_selected_row(event):
    try:
        global selected_tuple
        index = list1.curselection()[0]
        selected_tuple = list1.get(index)
        e1.delete(0, END)
        e1.insert(END, selected_tuple[1])
        e2.delete(0, END)
        e2.insert(END, selected_tuple[2])
        e3.delete(0, END)
        e3.insert(END, selected_tuple[3])
        e4.delete(0, END)
        e4.insert(END, selected_tuple[4])
    except IndexError:
        pass


def fetch_command():
    list1.delete(0, END)
    for row in backend.fetchall():
        list1.insert(END, row)


def search_command():
    list1.delete(0, END)
    for row in backend.search(title_value.get(), author_value.get(), year_value.get(), isbn_value.get()):
        list1.insert(END, row)


def insert_command():
    backend.insertrecord(title_value.get(), author_value.get(),
                         year_value.get(), isbn_value.get())
    list1.delete(0, END)
    list1.insert(END, (title_value.get(), author_value.get(),
                       year_value.get(), isbn_value.get()))
    fetch_command()
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)


def delete_command():
    backend.deleterecord(selected_tuple[0])
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)
    e4.delete(0, END)

    fetch_command()


def update_command():
    backend.updaterecord(selected_tuple[0], title_value.get(), author_value.get(),
                         year_value.get(), isbn_value.get())

    fetch_command()


window = Tk()

window.wm_title('Book Store')
window.resizable(False, False)

l1 = Label(window, text='Title')
l1.grid(row=1, column=1, padx=5, pady=5)

title_value = StringVar()
e1 = Entry(window, textvariable=title_value, width=30)
e1.grid(row=1, column=2, padx=5, pady=5)

l2 = Label(window, text='Author')
l2.grid(row=1, column=3, padx=5, pady=5)

author_value = StringVar()
e2 = Entry(window, textvariable=author_value, width=30)
e2.grid(row=1, column=4, padx=5, pady=5)


l3 = Label(window, text='Year')
l3.grid(row=3, column=1, padx=5, pady=5)

year_value = StringVar()
e3 = Entry(window, textvariable=year_value, width=30)
e3.grid(row=3, column=2, padx=5, pady=5)


l4 = Label(window, text='ISBN')
l4.grid(row=3, column=3, padx=5, pady=5)

isbn_value = StringVar()
e4 = Entry(window, textvariable=isbn_value, width=30)
e4.grid(row=3, column=4, padx=5, pady=5)

list1 = Listbox(window, height=6, width=60)
list1.grid(row=4, column=1, rowspan=5, columnspan=8, padx=10, pady=10)

sb1 = Scrollbar(window)
sb1.grid(row=4, column=5,  rowspan=5)

# link listbox to scrollbar
list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

# bind function to widget event
list1.bind('<<ListboxSelect>>', get_selected_row)

b1 = Button(window, text='Fetch all records', width=20, command=fetch_command)
b1.grid(row=9, column=2, padx=5, pady=5)

b2 = Button(window, text='Search record', width=20, command=search_command)
b2.grid(row=9, column=3, padx=5, pady=5)

b3 = Button(window, text='Add record', width=20, command=insert_command)
b3.grid(row=9, column=4, padx=5, pady=5)
width = 20
b4 = Button(window, text='Update record', width=20, command=update_command)
b4.grid(row=10, column=2, padx=5, pady=5)

b5 = Button(window, text='Delete record', width=20, command=delete_command)
b5.grid(row=10, column=3, padx=5, pady=5)

b5 = Button(window, text='Close', width=20, command=window.destroy)
b5.grid(row=10, column=4, padx=5, pady=5)

window.mainloop()
