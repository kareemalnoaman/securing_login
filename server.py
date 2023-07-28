import _mysql_connector
import hashlib

import mysql.connector

conn = mysql.connector.Connect("userdata.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS userdata(
id INTEGER PRIMARY KEY,
username VARCHAR(255) NOT NULL,
password VARCHAR(255) NOT NULL
)""")
