from src.models.settings.db_connection_handler import db_connection_handler
from src.models.repositories.user_repository import UserRepository
from src.controllers.login_creator import LoginCreator
from src.view.login_creator_view import LoginCreatorView

def login_creator_composer():
  conn = db_connection_handler.get_connection()
  model = UserRepository(conn=conn)
  controller = LoginCreator(user_repository=model)
  view = LoginCreatorView(controller=controller)

  return view
