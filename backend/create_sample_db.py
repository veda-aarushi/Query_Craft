import sqlite3

conn = sqlite3.connect("database/sample.db")
c = conn.cursor()

c.execute('''
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    department TEXT,
    salary INTEGER
)
''')

c.executemany('''
INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)
''', [
    ('Alice', 'Engineering', 90000),
    ('Bob', 'Sales', 70000),
    ('Carol', 'HR', 60000)
])

conn.commit()
conn.close()
