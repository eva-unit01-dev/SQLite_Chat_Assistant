import sqlite3
from datetime import datetime

def create_database():
    # Connect to SQLite database (creates it if it doesn't exist)
    conn = sqlite3.connect('company.db')
    cursor = conn.cursor()

    # Create Employees table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Department TEXT NOT NULL,
        Salary INTEGER NOT NULL,
        Hire_Date DATE NOT NULL
    )
    ''')

    # Create Departments table
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY,
        Name TEXT NOT NULL,
        Manager TEXT NOT NULL
    )
    ''')

    # Insert sample data into Employees
    employees_data = [
        (1, 'Alice', 'Sales', 50000, '2021-01-15'),
        (2, 'Bob', 'Engineering', 70000, '2020-06-10'),
        (3, 'Charlie', 'Marketing', 60000, '2022-03-20')
    ]

    cursor.executemany('''
    INSERT OR REPLACE INTO Employees (ID, Name, Department, Salary, Hire_Date)
    VALUES (?, ?, ?, ?, ?)
    ''', employees_data)

    # Insert sample data into Departments
    departments_data = [
        (1, 'Sales', 'Alice'),
        (2, 'Engineering', 'Bob'),
        (3, 'Marketing', 'Charlie')
    ]

    cursor.executemany('''
    INSERT OR REPLACE INTO Departments (ID, Name, Manager)
    VALUES (?, ?, ?)
    ''', departments_data)

    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()