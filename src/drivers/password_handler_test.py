from src.drivers.password_handler import PasswordHandler

def test_encrypt():
  senha = 'abc123'
  password_handler = PasswordHandler()

  hashed_password = password_handler.encrypt_password(password=senha)
  

  password_checked = password_handler.check_password(password=senha, hashed_password=hashed_password)
  assert password_checked
  