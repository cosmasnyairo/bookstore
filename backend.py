import sqlite3

def connecttodb():
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    con.commit()
    con.close()


def insertrecord(title, author, year, isbn):
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",
                (title, author, year, isbn))
    con.commit()
    con.close()


def fetchall():
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    con.close()
    return rows


def search(title="", author="", year="", isbn=""):
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    con.close()
    return rows


def updaterecord(bookid, title="", author="", year="", isbn=""):
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute(
        "UPDATE books SET title=?,author=?,year=?,isbn=? WHERE id=?",
        (title, author, year, isbn, bookid))
    con.commit()
    con.close()


def deleterecord(bookid):
    con = sqlite3.connect('bookstore.db')
    cur = con.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (bookid,))
    con.commit()
    con.close()


#insertrecord('Everything is F','M. Manson',2019,138212352)
# updaterecord(3,title='Everything is F',author='M. Manson',year=2019,isbn=13918397192)
# deleterecord(3)
