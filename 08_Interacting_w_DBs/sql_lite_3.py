##################
### SQL Lite 3 ###
##################

# DB Steps
# connect, create cursor object, apply query, commit changes, close connection

import sqlite3

def create_table():
    conn = sqlite3.connect("lite.db") # Step One
    cur = conn.cursor() # Step Two
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") # Step Three
    conn.commit() # Step Four
    conn.close() # Step Five

def insert_data(item, quantity, price):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("INSERT INTO store VALUES (?, ?, ?)", (item, quantity, price))
    conn.commit() 
    conn.close() 

def view():
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def remove_item(item):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("DELETE FROM store WHERE item=?",(item,)) # You need this extra comma
    conn.commit()
    conn.close()

def update_quantity(item, quant, price):
    conn = sqlite3.connect("lite.db") 
    cur = conn.cursor() 
    cur.execute("UPDATE store SET quantity = ?, price=? WHERE item=?",(quant, price, item)) 
    conn.commit()
    conn.close()
    
# insert_data("Coffee Cup", 10, 25)
# remove_item("Wine Glass")
# update_quantity( 20, 50, 'Coffee Cup',)
# update_quantity('Coffee Cup', 3, 5)
print(view())