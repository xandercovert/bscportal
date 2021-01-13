from flask import Flask, render_template, url_for, redirect, flash, request, jsonify
import sys
import os
import time
import secrets
import db

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_killed_my_father_prepare_to_die'
port = int(os.environ.get("PORT", 5000))

@app.route('/')
@app.route('/home')
def home():

    allAthletes = db.get_all_athletes()

    athletes = []
    for i in allAthletes:
        a = {
            'athleteID': i[0],
            'firstName': i[1],
            'lastName': i[2],
            'email': i[3],
            'phone': i[4]

        }
        athletes.append(a)
        print(a, file=sys.stderr)


    return render_template('home.html', athletes = athletes)

@app.route('/checkin/<string:lastName>')
def checkin(lastName):
    allAthletes = db.get_athlete(lastName)

    print(lastName, file=sys.stderr)
    

    athletes = []
    for i in allAthletes:
        a = {
            'athleteID': i[0],
            'firstName': i[1],
            'lastName': i[2],
            'email': i[3],
            'phone': i[4]

        }
        athletes.append(a)

    print(athletes, file=sys.stderr)

    return render_template('checkin.html', athletes = athletes)





if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)