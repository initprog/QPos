import hashlib
import sqlite3
from contextlib import closing
from qpos.db import DEFAULT_DB, conn

def hash_password(pwd):
  # encode the password as bytes
  pwd_bytes = pwd.encode('utf-8')

  # use SHA-256 hash function to create hash object
  hash_obj = hashlib.sha256(pwd_bytes)
  
  # return hexadecimal representation of the hash object
  return hash_obj.hexdigest()

def authenticate(userid, pwd):
  with closing(conn()) as connection:
    with closing(connection.cursor()) as cursor:
      row = cursor.execute(f"SELECT userId, password FROM teammember WHERE userId={userid}").fetchone()
      if row != None:
        if row[1] == hash_password(pwd): return True
  return False
