from src.models.repositories.user_repository import UserRepository
from src.models.settings.db_connection_handler import db_connection_handler
from unittest.mock import Mock

class MockCursor:
  def __init__(self):
    self.execute = Mock()
    self.fetchone = Mock()

class MockConnection:
  def __init__(self):
    self.cursor = Mock(return_value=MockCursor())
    self.commit = Mock()

def test_registry_user():
  db_connection_handler.connect()
  conn = db_connection_handler.get_connection()
  repo = UserRepository(conn)

  username = 'test'
  password = '1234'

  #repo.registry_user(username=username, password=password)
  
def test_unit_registry_user():
  mock_connection = MockConnection()
  repo = UserRepository(mock_connection)

  username = 'unit test'
  password = 'abcd'

  repo.registry_user(username=username, password=password)

  cursor = mock_connection.cursor.return_value

  assert 'INSERT INTO users' in cursor.execute.call_args[0][0]
  assert '(username, password)' in cursor.execute.call_args[0][0]
  assert 'VALUES' in cursor.execute.call_args[0][0]
  assert cursor.execute.call_args[0][1] == (username, password)

  mock_connection.commit.assert_called_once()

def test_get_user_by_username():
  username = 'unit test'

  mock_connection = MockConnection()
  repo = UserRepository(mock_connection)

  repo.get_user_by_username(username=username)

  cursor = mock_connection.cursor.return_value

  assert 'SELECT id, username, password' in cursor.execute.call_args[0][0]
  assert 'FROM users' in cursor.execute.call_args[0][0]
  assert 'WHERE username = ?' in cursor.execute.call_args[0][0]
  assert cursor.execute.call_args[0][1] == (username,)
  cursor.fetchone.assert_called_once()
  