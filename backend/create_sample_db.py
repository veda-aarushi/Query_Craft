import sqlite3

conn = sqlite3.connect("database/sample.db")
c = conn.cursor()

# Create employees
c.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department_id INTEGER,
    salary INTEGER
)
''')

# Create departments
c.execute('''
CREATE TABLE IF NOT EXISTS departments (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT
)
''')

# Insert departments
c.executemany('''
INSERT INTO departments (name) VALUES (?)
''', [
    ('Engineering',),
    ('HR',),
    ('Sales',)
])

# Insert employees
c.executemany('''
INSERT INTO employees (name, department_id, salary) VALUES (?, ?, ?)
''', [
    ('Alice', 1, 90000),
    ('Bob', 3, 70000),
    ('Carol', 2, 60000),
    ('Dave', 1, 95000)
])

conn.commit()
conn.close()
print("✅ sample.db created with employees and departments")
