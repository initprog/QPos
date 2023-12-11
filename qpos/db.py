# POS database classes
# Code for DB initialization settings when the program is initially run
# See: https://medium.com/opex-analytics/database-connections-in-python-extensible-reusable-and-secure-56ebcf9c67fe

import os, sqlite3, logging
from sqlite3 import Error
from contextlib import closing

DEFAULT_DB = os.path.realpath("data/pos.sqlite")

class SqliteDb:
    """
    Sqlite database context manager that uses optional environment variable for connection string.
    Context manager is used for managing resources used by the program. After completion of usage, 
    it has to release memory and terminate connections between files. 
    """
    
    def __init__(self, connection_string=os.environ.get("CONN", DEFAULT_DB)):
        self.connection_string = connection_string
        self.connector = None    
        
    def __enter__(self):
        """
        This method is automatically called when starting a "with" block.
        """
        self.connector = sqlite3.connect(self.connection_string)
        return self    

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Take care of releasing the resources occupied with the current code snippet.
        This method will always be executed

        Parameters:
            self: instance of the class
            exc_type: Exception type
            exc_val: Exception value; like divide_by_zero, floating_point_error, etc.
            exc_tb: Exception traceback with information needed to solve the exception.
        """
        if exc_tb is None:
            self.connector.commit()
            logging.debug("commited")
        else:
            self.connector.rollback()
            logging.debug("rollback")
        self.connector.close()
        logging.debug("close db connection")

def dbcall(func):
    """
    Database decorator (wrapper function)
    """
    def with_connection_(*args, **kwargs):
        conn_str = os.environ.get("CONN", DEFAULT_DB)
        cnn = sqlite3.connect(conn_str)
        try:
            rv = func(cnn, *args, **kwargs)
        except Exception:
            cnn.rollback()
            logging.error("Database connection error")
            raise
        else:
            cnn.commit()
        finally:
            cnn.close()        
        return rv
    return with_connection_


def dbcontextlib():
    """
    Using closing method from contextlib module
    """
    with closing(sqlite3.connect(DEFAULT_DB)) as connection:
        with closing(connection.cursor()) as cursor:
            rows = cursor.execute("SELECT 1").fetchall()
            print(rows)


'''
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
'''

def test_direct_connect():
    con = sqlite3.connect(DEFAULT_DB)
    res = con.execute("SELECT * FROM Product")
    for t in res:
        print(t)

test_direct_connect()

@dbcall
def test_wrapper(*arg):
    cur = arg[0].cursor()
    if len(arg) == 2:
        res = cur.execute(arg[1])
    else:
        res = cur.execute(arg[1], arg[2])
    for t in res:
        print(t)

#test_wrapper("SELECT * FROM Product")
#test_wrapper("SELECT * FROM Product WHERE name=?", ('Fried Chicken (+9,000)',))

def test_ctx():
    with SqliteDb() as db:
        cursor = db.connector.cursor()
        rows = cursor.execute("SELECT * FROM Product WHERE name=?", ('Fried Chicken (+9,000)',))
        for t in rows:
            print(t)

#test_ctx()