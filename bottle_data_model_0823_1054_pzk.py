# 代码生成时间: 2025-08-23 10:54:12
#!/usr/bin/env python

# Importing necessary libraries
from bottle import route, run, request, response
import sqlite3
import json

# Database setup
DB_PATH = 'data.db'

# Connect to the database
def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

# Model for storing data
class DataModel:
    def __init__(self, db_path='skeleton.db'):
        self.db_path = db_path

    def create_table(self):
        """Create a table to store data if it doesn't exist."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS data (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                email TEXT
            )''');
            conn.commit()

    def add_data(self, name, age, email):
        """Add a new entry to the data table."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('INSERT INTO data (name, age, email) VALUES (?, ?, ?)', (name, age, email))
            conn.commit()
            return cursor.lastrowid

    def get_all_data(self):
        """Retrieve all entries from the database."""
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM data')
            rows = cursor.fetchall()
            return [dict(row) for row in rows]

    def delete_data(self, data_id):
        "