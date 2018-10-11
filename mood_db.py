from sqlalchemy import create_engine

class MoodDB:

	def __init__(self):
		self.db_uri = 'sqlite:///mood_sms.db'
		self.engine = create_engine(self.db_uri)
	
	def get_moods(self):
		return self.engine.execute("SELECT type, star, time FROM users INNER JOIN mood ON users.id = mood.user_id")
