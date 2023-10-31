from main import encrypt_this


def test_encrypt_Hello():
  assert encrypt_this('Hello') == '72olle'

def test_encrypt_world():
  assert encrypt_this('good') == '103doo'

def test_encrypt_hello_world():
  assert encrypt_this('hello world') == '104olle 119drlo'

def test_encrypy_teste():
  assert encrypt_this('teste') == '116este'