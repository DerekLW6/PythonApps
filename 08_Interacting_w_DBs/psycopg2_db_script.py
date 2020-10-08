##################
#### Psycopg2 ####
##################

# DB Steps
# connect, create cursor object, apply query, commit changes, close connection

import psycopg2

def create_table():
    conn = psycopg2.connect("dbname='dmoney' user= 'postgres' password= 'CHARLIErock6' host= 'localhost' port = '5432' ") # Step One
    cur = conn.cursor() # Step Two
    cur.execute("CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)") # Step Three
    conn.commit() # Step Four
    conn.close() # Step Five

def insert_data(item, quantity, price):
    conn = psycopg2.connect("dbname='dmoney' user= 'postgres' password= 'CHARLIErock6' host= 'localhost' port = '5432' ") 
    cur = conn.cursor() 
    cur.execute("INSERT INTO store VALUES ('%s', '%s', '%s')" % (item, quantity, price))
    conn.commit() 
    conn.close() 

def view():
    conn = psycopg2.connect("dbname='dmoney' user= 'postgres' password= 'CHARLIErock6' host= 'localhost' port = '5432' ") 
    cur = conn.cursor() 
    cur.execute("SELECT * FROM store")
    rows = cur.fetchall()
    conn.close()
    return rows

def remove_item(item):
    conn = psycopg2.connect("dbname='dmoney' user= 'postgres' password= 'CHARLIErock6' host= 'localhost' port = '5432' ") 
    cur = conn.cursor() 
    cur.execute("DELETE FROM store WHERE item=?",(item,)) # You need this extra comma
    conn.commit()
    conn.close()

def update_quantity(item, quant, price):
    conn = psycopg2.connect("dbname='dmoney' user= 'postgres' password= 'CHARLIErock6' host= 'localhost' port = '5432' ") 
    cur = conn.cursor() 
    cur.execute("UPDATE store SET quantity = ?, price=? WHERE item=?",(quant, price, item)) 
    conn.commit()
    conn.close()
    
# create_table()
insert_data("Coffee Cup", 10, 25)
insert_data("Wine Glass", 5, 30)
# remove_item("Wine Glass")
# update_quantity( 20, 50, 'Coffee Cup',)
# update_quantity('Coffee Cup', 3, 5)
# print(view())