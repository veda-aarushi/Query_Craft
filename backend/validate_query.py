# backend/validate_query.py
import sqlite3
import json

def run_user_query(user_query):
    conn = sqlite3.connect("database/sample.db")
    conn.row_factory = sqlite3.Row  # Return dict-style rows
    cur = conn.cursor()
    try:
        cur.execute(user_query)
        rows = cur.fetchall()
        columns = [description[0] for description in cur.description] if rows else []
        return {
            "success": True,
            "columns": columns,
            "rows": [dict(row) for row in rows]
        }
    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
    finally:
        conn.close()
