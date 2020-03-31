from tkinter import *

window = Tk()

l1 = Label(window, text='Title')
l1.grid(row=1, column=1,padx=5, pady=5)

title_value=StringVar()
e1=Entry(window,textvariable=title_value, width=30)
e1.grid(row=1, column=2,padx=5, pady=5)

l2 = Label(window, text='Author')
l2.grid(row=1, column=3,padx=5, pady=5)

author_value=StringVar()
e2=Entry(window,textvariable=author_value, width=30)
e2.grid(row=1, column=4,padx=5, pady=5)


l3 = Label(window, text='Year')
l3.grid(row=3, column=1,padx=5, pady=5)

year_value=StringVar()
e3=Entry(window,textvariable=year_value, width=30)
e3.grid(row=3, column=2,padx=5, pady=5)


l4 = Label(window, text='ISBN')
l4.grid(row=3, column=3,padx=5, pady=5)

isbn_value=StringVar()
e4=Entry(window,textvariable=isbn_value, width=30)
e4.grid(row=3, column=4,padx=5, pady=5)

list1=Listbox(window,height=6,width=80)
list1.grid(row=4, column=1, rowspan =5,columnspan=8,padx=10, pady=10)

sb1=Scrollbar(window)
sb1.grid(row=4,column=5,  rowspan =5)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

b1=Button(window, text='Fetch all records',width=20)
b1.grid(row=9, column=2,padx=5, pady=5)

b2=Button(window, text='Search record',width=20)
b2.grid(row=9, column=3,padx=5, pady=5)

b3=Button(window, text='Add record',width=20)
b3.grid(row=9, column=4,padx=5, pady=5)
width=20
b4=Button(window, text='Update record',width=20)
b4.grid(row=10, column=2,padx=5, pady=5)

b5=Button(window, text='Delete record',width=20)
b5.grid(row=10, column=3,padx=5, pady=5)

b5=Button(window, text='Close',width=20)
b5.grid(row=10, column=4,padx=5, pady=5)

window.mainloop()
