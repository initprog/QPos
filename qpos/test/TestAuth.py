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
    str1 = utils.hash_password('admin')
    print(str1)
    print(len(str1))

  def test_generate_nanoid(self):
    pk = utils.generate_nanoid()
    assert len(pk) == 18
    print(pk)

  def test_authentication(self):
    valid = utils.authenticate('admin', 'admin')
    assert valid == 1
    valid = utils.authenticate('admin', 'secret')
    assert valid == 0
    
