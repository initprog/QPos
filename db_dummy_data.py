# POS database classes
# Code for DB initialization settings when the program is initially run

import sqlite3
from sqlite3 import Error

class DummyData:
    def createConnection(self):
        conn = None
        try:
            conn = sqlite3.connect("pos.sqlite")
            return conn
        except Error as e:
            print(e)
        return conn

    def insert(self, conn, sql):
        try:
            c = conn.cursor()
            c.execute(sql)
            conn.commit()
        except Error as e:
            print(e)

    def __init__(self):
        sql1 = """INSERT INTO Sale
                          ('NoSale', 'Date', 'Time', 'Price', 'Payment') 
                           VALUES 
                          (20191130022001,'2019-11-30','02:20:01',20000,'Cash')"""
        sql2 = """INSERT INTO Sale
                          ('NoSale', 'Date', 'Time', 'Price', 'Payment') 
                           VALUES 
                          (20191130133030,'2019-11-30','13:30:30',32000,'Card')"""
        sql3 = """INSERT INTO Sale
                          ('NoSale', 'Date', 'Time', 'Price', 'Payment') 
                           VALUES 
                          (20191201144110,'2019-12-01','14:41:10',45000,'Card')"""
        sql4 = """INSERT INTO Sale
                          ('NoSale', 'Date', 'Time', 'Price', 'Payment') 
                           VALUES 
                          (20191201153000,'2019-12-01','15:30:00',24000,'Cash')"""
        conn = self.createConnection()
        if conn is not None:
            self.insert(conn, sql1)
            self.insert(conn, sql2)
            self.insert(conn, sql3)
            self.insert(conn, sql4)
        else:
            print("Error. Cannot insert the data.")

DummyData()