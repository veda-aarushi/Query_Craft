# backend/seed_db.py
from app import app, db, Problem

with app.app_context():
    problems = [
        Problem(
            title="List All Employees",
            prompt="Write a SQL query to list all employees.",
            schema="employees(id INTEGER, name TEXT, department_id INTEGER, salary INTEGER)",
            solution="SELECT name FROM employees;",
            hint="Use SELECT name FROM employees."
        ),
        Problem(
            title="Find High Salaries",
            prompt="List employees earning > 80000.",
            schema="employees(id INTEGER, name TEXT, department_id INTEGER, salary INTEGER)",
            solution="SELECT name FROM employees WHERE salary > 80000;",
            hint="Use WHERE clause."
        ),
        Problem(
            title="Departments List",
            prompt="Retrieve all departments.",
            schema="departments(id INTEGER, name TEXT)",
            solution="SELECT name FROM departments;",
            hint="Simple SELECT from departments."
        )
    ]

    db.session.bulk_save_objects(problems)
    db.session.commit()
    print("✅ Problems seeded into database!")
