import sqlite3

conn = sqlite3.connect('nyondo_stock.db')

def search_product_safe(name):
    # Use parameterized query with ? placeholder
    query = "SELECT * FROM products WHERE name LIKE ?"
    rows = conn.execute(query, (f"%{name}%",)).fetchall()
    print(f"Query: {query} with value {name}")
    print(f"Result: {rows}\n")
    return rows

def login_safe(username, password):
    # Use parameterized query with ? placeholders
    query = "SELECT * FROM users WHERE username=? AND password=?"
    row = conn.execute(query, (username, password)).fetchone()
    print(f"Query: {query} with values ({username}, {password})")
    print(f"Result: {row}\n")
    return row

# --- Tests (all should return [] or None) ---
print("Test 1:", search_product_safe("' OR 1=1--"))
print("Test 2:", search_product_safe("' UNION SELECT id,username,password,role FROM users--"))
print("Test 3:", login_safe("admin'--", "anything"))
print("Test 4:", login_safe("' OR '1'='1", "' OR '1'='1"))
