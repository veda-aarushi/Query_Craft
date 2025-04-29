# backend/load_problems_from_csv.py
import sqlite3
import csv

conn = sqlite3.connect("problems.db")
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS problems (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT,
  prompt TEXT,
  schema TEXT,
  solution TEXT,
  hint TEXT
)
''')

with open("problems.csv", newline='', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        cursor.execute('''
        INSERT INTO problems (title, prompt, schema, solution, hint)
        VALUES (?, ?, ?, ?, ?)
        ''', (row["title"], row["prompt"], row["schema"], row["solution"], row["hint"]))

conn.commit()
conn.close()
print("✅ Problems loaded from CSV into problems.db")
