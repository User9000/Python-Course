import sqlite3



#this function creates a database "lite.db"
#this function also creates a table named "store"
#inserts the first item

def create_table():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER,price REAL)")
    cur.execute("INSERT INTO store VALUES('Wine glass', 8, 10.5)")
    conn.commit()
    conn.close()
#this function is used to insert a new item
def insert(item,quantity,price):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()   
    cur.execute("INSERT INTO store VALUES(?,?,?)",(item,quantity,price))
    conn.commit()
    conn.close()


def delete(item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()   
    cur.execute("DELETE FROM store WHERE item=?",(item,))
    conn.commit()
    conn.close()

def update(quantity,price,item):
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()   
    cur.execute("UPDATE store SET quantity=?, price=? WHERE item=?",(quantity,price, item))
    conn.commit()
    conn.close()

#this call of a function inserts coffee cups into the database
#insert("Coffe cup",10,5)

#this function is used to view all items in table store
#by returning the variable rows.

def view():
    conn=sqlite3.connect("lite.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM store")
    rows=cur.fetchall()
    conn.close()
    return rows

print(view())

#delete("Wine glass")
update(11,6,"Water Glass")

print(view())

