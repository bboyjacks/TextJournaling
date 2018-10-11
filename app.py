# Filename: app.py
# Author: Lester Dela Cruz
# Github: bboyjacks
# Description: This app receives a message from phone
# and records them in a database then shows them in 
# a UI
from flask import Flask, render_template
from mood_db import MoodDB

app = Flask(__name__)
mood_db = MoodDB()

@app.route('/')
def hello_world():
    moods = mood_db.get_moods()
    for mood in moods:
        print(mood)
    return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)