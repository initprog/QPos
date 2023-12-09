# POS database classes
# Code for DB initialization settings when the program is initially run

import sqlite3
from sqlite3 import Error

class POSDB:
    def createConnection(self):
        conn = None
        try:
            conn = sqlite3.connect("pos.sqlite")
            return conn
        except Error as e:
            print(e)
        return conn

    def createTable(self, conn, createTableSql):
        try:
            c = conn.cursor()
            c.execute(createTableSql)
        except Error as e:
            print(e)

    def __init__(self):
        sqlCreateTable_Product = """CREATE TABLE IF NOT EXISTS Product (
                                        NoProduct INTEGER PRIMARY KEY AUTOINCREMENT,
	                                    Name varchar(255) NOT NULL,
	                                    Price integer DEFAULT 0,	
                                        Category varchar(255) DEFAULT 'Etc'
	                                    CHECK (Price >= 0)
	                                );"""
        sqlCreateTable_Sale = """CREATE TABLE IF NOT EXISTS Sale (
                                    NoSale INTEGER PRIMARY KEY AUTOINCREMENT,
	                                Date date NOT NULL,
                                	Time time NOT NULL,
                                	Price integer NOT NULL,
                                	Payment varchar(255) NOT NULL,
                                	CHECK (Price >= 0)
                                );"""
        sqlCreateTable_DetailedSale = """CREATE TABLE IF NOT EXISTS DetailedSale (
                                	ID INTEGER PRIMARY KEY AUTOINCREMENT,
	                                NoSale integer FOREIGNKEY REFERENCES Sale(NoSale),
	                                Product varchar(255) NOT NULL,
	                                No integer NOT NULL,
	                                Price integer NOT NULL,
	                                CHECK (No >=1 AND Price >= 0)
                                );"""
        sqlCreateTable_Management = """CREATE TABLE IF NOT EXISTS Management (
	                                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
	                                        DateTime datetime NOT NULL,
	                                        Total integer NOT NULL,
                                        	CHECK (Total >= 0)
                                        );"""
        conn = self.createConnection()
        
        if conn is not None:
            self.createTable(conn, sqlCreateTable_Product)
            self.createTable(conn, sqlCreateTable_Sale)
            self.createTable(conn, sqlCreateTable_DetailedSale)
            self.createTable(conn, sqlCreateTable_Management)
        else:
            print("Error. Cannot establish connection to the database.")

#POSDB()
