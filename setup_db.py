import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('users.db')
c = conn.cursor()

# Create the users table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, 
              username TEXT UNIQUE NOT NULL, 
              email TEXT UNIQUE NOT NULL, 
              password TEXT NOT NULL)''')
