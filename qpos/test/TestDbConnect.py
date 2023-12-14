import sqlite3
from contextlib import closing
from qpos.db import DEFAULT_DB, conn

"""
Run tests in a module: 
    pytest -s test_mod.py

Run tests in a directory:
    pytest -s test/
"""
class TestDbConnect:
    def test_direct_connect(self):
        con = sqlite3.connect(DEFAULT_DB)
        rows = con.cursor().execute("SELECT 3").fetchall()
        assert rows[0][0] == 3
        con.close()

    def test_get_connection(self):
        with closing(conn()) as connection:
            with closing(connection.cursor()) as cursor:
                rows = cursor.execute("SELECT 3").fetchall()
                assert rows[0][0] == 3
