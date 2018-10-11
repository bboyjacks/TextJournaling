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
			mood_obj['time'] = self.__time_parser__(mood[2])
			mood_list['moods'].append(mood_obj)
		return mood_list

	def __time_parser__(self, mood_time):
		dt = datetime.datetime.utcfromtimestamp(mood_time)
		dt_today = datetime.datetime.now()

		if (dt.day == dt_today.day):
			return dt_today.strftime('%I %p Today')
		else:
			return dt.strftime('%I %p on %m/%d/%Y')