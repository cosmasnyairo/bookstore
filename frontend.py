# libraries
from tkinter import *
# files
from backend import Database

db = Database('bookstore.db')


class Window(object):
    def __init__(self, window):
        self.window = window
        window.wm_title('Book Store')
        window.resizable(False, False)

        labeltitle = ['Title', 'Author', 'Year', 'ISBN']
        labelrows = [1, 1, 3, 3]
        labelcolums = [1, 3, 1, 3]

        for lt, lr, lc in zip(labeltitle, labelrows, labelcolums):
            label = Label(window, text=lt)
            label.grid(row=lr, column=lc, padx=5, pady=5)

        self.title_value = StringVar()
        self. e1 = Entry(window, textvariable=self.title_value, width=30)
        self.e1.grid(row=1, column=2, padx=5, pady=5)

        self.author_value = StringVar()
        self.e2 = Entry(window, textvariable=self.author_value, width=30)
        self. e2.grid(row=1, column=4, padx=5, pady=5)

        self.year_value = StringVar()
        self.e3 = Entry(window, textvariable=self.year_value, width=30)
        self.e3.grid(row=3, column=2, padx=5, pady=5)

        self.isbn_value = StringVar()
        self.e4 = Entry(window, textvariable=self.isbn_value, width=30)
        self.e4.grid(row=3, column=4, padx=5, pady=5)

        self.list1 = Listbox(window, height=6, width=60)
        self.list1.grid(row=4, column=1, rowspan=5,
                        columnspan=8, padx=10, pady=10)

        sb1 = Scrollbar(window)
        sb1.grid(row=4, column=5,  rowspan=5)

        # link listbox to scrollbar
        self.list1.configure(yscrollcommand=sb1.set)
        sb1.configure(command=self.list1.yview)

        # bind function to widget event
        self.list1.bind('<<ListboxSelect>>', self.get_selected_row)

        commands = [self.fetch_command, self.search_command, self.insert_command,
                    self.update_command, self.delete_command, self.window.destroy]
        buttontitle = ['Fetch all records', 'Search record',
                       'Add record', 'Update record', 'Delete record', 'Close']
        buttonrows = [9, 9, 9, 10, 10, 10]
        buttoncolumns = [2, 3, 4, 2, 3, 4]

        for (c, bt, br, bc) in zip(commands, buttontitle, buttonrows, buttoncolumns):
            button = Button(window, text=bt, width=20, command=c)
            button.grid(row=br, column=bc, padx=5, pady=5)

    def get_selected_row(self, event):
        try:
            index = self.list1.curselection()[0]
            self.selected_tuple = self.list1.get(index)
            self. e1.delete(0, END)
            self.e1.insert(END, self.selected_tuple[1])
            self. e2.delete(0, END)
            self. e2.insert(END, self.selected_tuple[2])
            self. e3.delete(0, END)
            self. e3.insert(END, self.selected_tuple[3])
            self.e4.delete(0, END)
            self.e4.insert(END, self.selected_tuple[4])
        except IndexError:
            pass

    def fetch_command(self):
        self.list1.delete(0, END)
        for row in db.fetchall():
            self.list1.insert(END, row)

    def search_command(self):
        self.list1.delete(0, END)
        for row in db.search(self.title_value.get(), self.author_value.get(), self.year_value.get(), self. isbn_value.get()):
            self.list1.insert(END, row)

    def insert_command(self):
        db.insertrecord(self.title_value.get(), self.author_value.get(),
                        self.year_value.get(), self.isbn_value.get())
        self.list1.delete(0, END)
        self.list1.insert(END, (self.title_value.get(), self.author_value.get(),
                                self.year_value.get(), self.isbn_value.get()))
        self.fetch_command()
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)

    def delete_command(self):
        db.deleterecord(self.selected_tuple[0])
        self.e1.delete(0, END)
        self.e2.delete(0, END)
        self.e3.delete(0, END)
        self.e4.delete(0, END)
        self.fetch_command()

    def update_command(self):
        db.updaterecord(self.selected_tuple[0], self.title_value.get(), self.author_value.get(),
                        self.year_value.get(), self.isbn_value.get())

        self.fetch_command()


window = Tk()
Window(window)
window.mainloop()
