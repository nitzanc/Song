import sqlite3

def query_db():
    db = sqlite3.connect("test.db")
    cursor = db.cursor()
    result = cursor.execute("select artist, title from entries")
    data = result.fetchall()
    cursor.close()
    db.close()
    return data

def insert_db(title, artist):
    db = sqlite3.connect("test.db")
    cursor = db.cursor()
    cursor.execute("insert into entries (title, artist) values (?, ?);",
                   [title, artist])
    db.commit()
    cursor.close()
    db.close()
