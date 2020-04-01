import sqlite3

def create_table():

    #1 Create Database
    conn = sqlite3.connect("lite.db")
    #2 Create Cursor to Database
    curr =conn.cursor()

    #3 Create Table and columns 
    curr.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL);")
    # Commit to DB and close the connection
    conn.commit()
    conn.close()

def insert(item,quantity,price):
    #1 Create Database
    conn = sqlite3.connect("lite.db")
    #2 Create Cursor to Database
    curr =conn.cursor()
    # Insert data to table 
    curr.execute("INSERT INTO store VALUES (?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()


def view():
      #1 Create Database
    conn = sqlite3.connect("lite.db")
    #2 Create Cursor to Database
    curr =conn.cursor()
    # Insert data to table 
    curr.execute("SELECT * FROM store")
    rows = curr.fetchall()
    conn.close()
    return rows

def delete(item):
    conn = sqlite3.connect("lite.db")
    curr =conn.cursor()
    curr.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()


def update(quantity, price, item):
    conn=sqlite3.connect("lite.db")
    curr = conn.cursor()
    curr.execute("UPDATE store SET quantity=?, price=? WHERE item=?", (quantity, price, item))
    conn.commit()
    conn.close()

update(15,15,'Water')
#delete('Coffee')
print(view())