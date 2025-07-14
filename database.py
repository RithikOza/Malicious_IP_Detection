import sqlite3
from datetime import datetime

conn = sqlite3.connect('alerts.db')
cur = conn.cursor()

cur.execute("""CREATE TABLE IF NOT EXISTS blocked_ips (
    ip TEXT, 
    timestamp TEXT
)""")
conn.commit()

def log_block(ip):
    cur.execute("INSERT INTO blocked_ips VALUES (?, ?)", (ip, str(datetime.now())))
    conn.commit()
