import sqlite3
from sqlite3 import *

conn = sqlite3.connect('../pos.sqlite')
c = conn.cursor()
c.execute("""SELECT * FROM Sale""")
conn.commit()
print(c.fetchall())
conn.close()

