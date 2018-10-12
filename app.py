# Filename: app.py
# Author: Lester Dela Cruz
# Github: bboyjacks
# Description: This app receives a message from phone
# and records them in a database then shows them in 
# a UI
from flask import Flask, render_template, request
from mood_db import MoodDB
from twilio import twiml
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
mood_db = MoodDB()

test_phone_number = 8053198724

@app.route('/')
def home():
    moods = mood_db.get_moods(test_phone_number)
    diaries = mood_db.get_diaries(test_phone_number)
    return render_template('home.html', moods=moods, diaries=diaries)

@app.route('/sms', methods=['POST'])
def text_recv():
    number = request.form['From']
    message_body = request.form['Body']
    number = number[2:]

    if "Anxiety:" in message_body:
        parsed_text = message_body.split(' ')
        mood_db.set_mood(number, "Anxiety", int(parsed_text[1]))
    elif "Happiness:" in message_body:
        parsed_text = message_body.split(' ')
        mood_db.set_mood(number, 'Happiness', int(parsed_text[1]))
    elif "Motivation:" in message_body:
        parsed_text = message_body.split(' ')
        mood_db.set_mood(number, 'Motivation', int(parsed_text[1]))
    else:
        mood_db.set_diary(int(number), message_body)
    resp = MessagingResponse()
    resp.message("Your thoughts are saved")

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)