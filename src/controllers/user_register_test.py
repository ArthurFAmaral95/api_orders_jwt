from src.controllers.user_register import UserRegister

class MockUserRepository:
  def __init__(self) -> None:
    self.registry_use_attributes = {}

  def registry_user(self, username, password) -> None:
    self.registry_use_attributes['username'] = username
    self.registry_use_attributes['password'] = password


def test_registry():
  repository = MockUserRepository()
  controller = UserRegister(repository)

  username = 'test'
  password = '123abc'

  response = controller.registry(username=username, password=password)
  
  assert response['type'] == 'User'
  assert response['username'] == username

  assert repository.registry_use_attributes['username'] == username
  assert repository.registry_use_attributes['password'] is not None
  assert repository.registry_use_attributes['password'] != password