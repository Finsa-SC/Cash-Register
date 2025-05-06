import sqlite3

lst = ["Quit", "Add", "Update", "Delete"]

conn = sqlite3.connect('all_menu.db')
c = conn.cursor()

c.execute("""
CREATE TABLE IF NOT EXISTS menu(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL,
    stock INTEGER)
""")
conn.commit()

def show():
    c.execute("SELECT * FROM menu")
    rows = c.fetchall()
    for row in rows:
        print(row)
    for i, li in enumerate(lst):
        print(f"{i}. {li}")

def add(name: str, categories: str, price: int, stock:int):
    c.execute("INSERT INTO menu (name, category, price, stock) VALUES (?, ?, ?, ?)",
              (name, categories, price, stock))
    conn.commit()

def update(name: str, categories: str, price: int, stock:int, ids: int):
    c.execute("UPDATE menu SET name = ?, category = ?, price = ?, stock = ? WHERE id = ?",
              (name, categories, price, stock, ids))
    conn.commit()

def delete(ids:int):
    c.execute("DELETE FROM menu WHERE id = ?",
              (ids, ))
    conn.commit()

show()
ind = input("Input number: ")
if ind.isdigit():
    index = int(ind)
    if index == 1:
        name = input("Name: ")
        category = input("Categories: ")
        price = int(input("Price: "))
        stock = int(input("Stock: "))
        add(name, category, price, stock)
    elif index == 2:
        show()
        ids = int(input("ID: "))
        name = input("Name: ")
        category = input("Categories: ")
        price = int(input("Price: "))
        stock = int(input("Stock: "))
        update(name, category, price, stock, ids)
    elif index == 3:
        show()
        ids = int(input("ID: "))
        delete(ids)
