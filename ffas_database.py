#!/usr/bin/env python3
import sqlite3
import time

# Initialize the database
def init_db(dbtype):
    if dbtype.lower() == "sqlite3":
        conn = sqlite3.connect("db.sqlite3") # We use SQLite3
    else:
        print("Currently only SQLite3 is available.")
        return False
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS ffas_paper (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            barcode TEXT,
            name TEXT,
            description TEXT,
            digital INTEGER,
            original INTERGER,
            cryptokey INTEGER,
            algorithm INTEGER,
            timestamp TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS ffas_digital (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              uuid TEXT,
              name TEXT,
              description TEXT,
              storage TEXT,
              originalfilename TEXT,
              cryptokey INTEGER NULL,
              algorithm INTEGER NULL,
              timestamp TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS ffas_cryptokey (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              keyuuid TEXT NOT NULL,
              algorithm TEXT NOT NULL,
              api TEXT,
              timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()
