from src.models.settings.db_connection_handler import db_connection_handler

def test_connection_to_db():
  #assert db_connection_handler.get_connection() is None

  db_connection_handler.connect()

  conn = db_connection_handler.get_connection()
  pragma_status = conn.execute("PRAGMA foreign_keys;").fetchone()[0]
  
    
  assert conn is not None
  assert pragma_status == 1
 