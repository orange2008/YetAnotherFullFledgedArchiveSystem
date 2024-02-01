#!/usr/bin/env python3
import sqlite3
import time
import string
import random
import uuid

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
            pagecount INTEGER,
            original INTERGER,
            cryptokeyuuid TEXT NULL,
            hashsum TEXT NULL,
            hashalgorithm TEXT NULL,
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
              cryptokeyuuid TEXT NULL,
              algorithm TEXT NULL,
              timestamp TEXT
        )
    ''')
    c.execute('''
        CREATE TABLE IF NOT EXISTS ffas_cryptokey (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              keyuuid TEXT NOT NULL,
              keytext TEXT NOT NULL,
              algorithm TEXT NOT NULL,
              api TEXT,
              timestamp TEXT
        )
    ''')
    conn.commit()
    conn.close()

def random_generator(length: int):
    return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(int(length)))


def paper_store(barcode: str, name: str, description: str, pagecount: int, original: int, cryptokeyuuid: str, hashsum: str, hashalgorithm: str):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    timestamp = time.ctime(time.time())
    c.execute("INSERT INTO ffas_paper (barcode, name, description, pagecount, original, cryptokeyuuid, hashsum, hashalgorithm, timestamp) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (barcode, name, description, pagecount, original, cryptokeyuuid, hashsum, hashalgorithm, timestamp))
    conn.commit()
    conn.close()
    return True

def crypto_store(keytext, algorithm="aes256", api="gpg"):
    conn = sqlite3.connect("db.sqlite3")
    c = conn.cursor()
    timestamp = time.ctime(time.time())
    keyuuid = uuid.uuid4()
    keyuuid = str(keyuuid)
    c.execute("INSERT INTO ffas_cryptokey (keyuuid, keytext, algorithm, api, timestamp) VALUES (?, ?, ?, ?, ?)", (keyuuid, keytext, algorithm, api, timestamp))
    conn.commit()
    conn.close()
    return keyuuid # Need to return keyUUID