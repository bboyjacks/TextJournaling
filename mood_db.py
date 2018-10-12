from sqlalchemy import create_engine
import datetime

class MoodDB:

	def __init__(self):
		self.db_uri = 'sqlite:///mood_sms.db'
		self.engine = create_engine(self.db_uri)
	
	def get_moods(self, phone_number):
		moods = self.engine.execute("SELECT type, star, time FROM users INNER JOIN mood ON users.id = mood.user_id AND users.phone_number = " + str(phone_number))
		mood_list = {'moods': []}
		for mood in moods:
			mood_obj = {}
			mood_obj['type'] = mood[0]
			mood_obj['star'] = mood[1]
			mood_obj['time'] = self.__time_parser(mood[2])
			mood_list['moods'].append(mood_obj)
		return mood_list

	def __time_parser(self, mood_time):
		dt = datetime.datetime.utcfromtimestamp(mood_time)
		dt_today = datetime.datetime.now()

		if (dt.day == dt_today.day):
			return dt_today.strftime('%I %p Today')
		else:
			return dt.strftime('%I %p on %m/%d/%Y')
	
	def get_diaries(self, phone_number):
		diaries = self.engine.execute("SELECT post, time FROM users INNER JOIN diary ON users.id = diary.user_id AND users.phone_number = " + str(phone_number))
		diary_list = {'diaries': []}
		
		for diary in diaries:
			diary_obj = {}
			diary_obj['post'] = diary[0]
			diary_obj['time'] = self.__time_parser(diary[1])
			diary_list['diaries'].append(diary_obj)
		return diary_list

	def set_diary(self, phone_number, message):
		user_id_sql_result = self.engine.execute("SELECT id FROM users WHERE phone_number = " + str(phone_number))
		user_id_fetch_result = user_id_sql_result.fetchall()
		user_id = user_id_fetch_result[0][0]
		sql_command = "INSERT INTO diary (user_id, post, time) "
		sql_command += "values (" + str(user_id) + ", '" + message + "'," + str(int(datetime.datetime.now().timestamp())) + ")"

		self.engine.execute(sql_command)
	
	def set_mood(self, phone_number, mood_type, star):
		user_id_sql_result = self.engine.execute("SELECT id FROM users WHERE phone_number = " + str(phone_number))
		user_id_fetch_result = user_id_sql_result.fetchall()
		user_id = user_id_fetch_result[0][0]
		sql_command = "INSERT INTO mood (user_id, type, star, time) "
		sql_command += "values (" + str(user_id) + ", '" + mood_type + "'," + str(star) + "," + str(int(datetime.datetime.now().timestamp())) + ")"

		self.engine.execute(sql_command)