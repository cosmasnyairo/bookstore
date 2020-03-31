import sqlite3

con = sqlite3.connect('bookstore.db')
cur = con.cursor()


def connecttodb():
    cur.execute(
        "CREATE TABLE IF NOT EXISTS books(id INTEGER PRIMARY KEY,title text,author text,year integer,isbn integer)")
    con.commit()


def insertrecord(title, author, year, isbn):
    cur.execute("INSERT INTO books VALUES(NULL,?,?,?,?)",
                (title, author, year, isbn))
    con.commit()


def fetchall():
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    return rows


def search(title="", author="", year="", isbn=""):
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",
                (title, author, year, isbn))
    rows = cur.fetchall()
    return rows


def updaterecord(bookid, title="", author="", year="", isbn=""):
    cur.execute(
        "UPDATE books SET title=?,author=?,year=?,isbn=? WHERE id=?",
        (title, author, year, isbn, bookid))
    con.commit()


def deleterecord(bookid):
    cur.execute("DELETE FROM books WHERE id=?", (bookid,))
    con.commit()

#insertrecord('Everything is F','M. Manson',2019,138212352)
# updaterecord(3,title='Everything is F',author='M. Manson',year=2019,isbn=13918397192)
# deleterecord(3)
print(fetchall())
connecttodb()
con.close()
