# POS database classes
# Code for DB initialization settings when the program is initially run

import sqlite3
from sqlite3 import Error
from contextlib import closing
from qpos.db import conn

class DummyData:
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
        
        with closing(conn()) as connection:
            with closing(connection.cursor()) as cursor:
                cursor.execute(sql1)
                cursor.execute(sql2)
                cursor.execute(sql3)
                cursor.execute(sql4)
                connection.commit()

DummyData()