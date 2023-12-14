from qpos import utils

"""
Run tests in a module: 
    pytest -s test_mod.py

Run tests in a directory:
    pytest -s test/
"""
class TestAuth:
  def test_hashing(self):
    str1 = utils.hash_password('secret-password')
    str2 = utils.hash_password('secret-password')
    assert str1 == str2
    print(str1)
    print(len(str1))