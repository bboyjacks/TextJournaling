from sqlalchemy import create_engine
import datetime

class MoodDB:

	def __init__(self):
		self.db_uri = 'sqlite:///mood_sms.db'
		self.engine = create_engine(self.db_uri)
	
	def get_moods(self):
		moods = self.engine.execute("SELECT type, star, time FROM users INNER JOIN mood ON users.id = mood.user_id")
		mood_list = {'moods': []}
		for mood in moods:
			mood_obj = {}
			mood_obj['type'] = mood[0]
			mood_obj['star'] = mood[1]
			mood_obj['time'] = datetime.datetime.utcfromtimestamp(mood[2]/1000)
			mood_list['moods'].append(mood_obj)
		return mood_list