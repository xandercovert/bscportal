from flask import Flask, render_template, url_for, redirect, flash, request, jsonify
import sys
import os
import time
import secrets
import db
import forms

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you_killed_my_father_prepare_to_die'
port = int(os.environ.get("PORT", 5000))

@app.route('/')
@app.route('/home')
def home():

    allAthletes = db.get_all_athletes()

    athletes = []
    for i in allAthletes:
        a =  {'lastName': i[2] }

        if not a in athletes:
            athletes.append(a)
            
        print(a, file=sys.stderr)


    return render_template('home.html', athletes = athletes)

@app.route('/family/<string:lastName>')
def family(lastName):
    allAthletes = db.get_athlete(lastName)

    print(lastName, file=sys.stderr)
    

    athletes = []
    for i in allAthletes:
        a = {
            'athleteID': i[0],
            'firstName': i[1],
            'lastName': i[2],
            'email': i[3],
            'phone': i[4],
            'checkedin': i[5]

        }
        athletes.append(a)

    print(athletes, file=sys.stderr)

    return render_template('family.html', athletes = athletes)

@app.route('/checkin/<int:id>', methods=['GET', 'POST'])
def athleteCheck(id):

    athlete = db.get_athlete_by_id(id)
    print(athlete, file=sys.stderr)

    a = {
            'athleteID': athlete[0],
            'firstName': athlete[1],
            'lastName': athlete[2],
            'email': athlete[3],
            'phone': athlete[4],
            'checkedin': athlete[5]

        }
    
    form = forms.AttendanceForm()

    if form.validate_on_submit() :
        print ("VALID", file=sys.stderr)
        print (form.saturday.data, file=sys.stderr)
        print (form.sunday.data, file=sys.stderr)
        print (form.wednesday.data, file=sys.stderr)

        saturday = form.saturday.data
        sunday = form.sunday.data
        wednesday = form.wednesday.data
        checkedin = True

        db.set_athlete_days(saturday, sunday, wednesday, checkedin, id)

        return redirect(url_for('family', lastName=athlete[2]))

    return render_template('checkin.html', title="Register Attendance", form=form, athlete=a)

@app.route('/attending')
def attending():

    allAthletes = db.get_all_athletes()

    athletes = []
    for i in allAthletes:
        
        a = {
            'athleteID': i[0],
            'firstName': i[1],
            'lastName': i[2],
            'email': i[3],
            'phone': i[4],
            'saturday': i[5],
            'sunday': i[6],
            'wednesday': i[7],
            'checkedin': i[8],

        }

        

        if i[5] : a['saturday'] = "X"
        else : a['saturday'] = " "

        if i[6] : a['sunday'] = "X"
        else : a['sunday'] = " "

        if i[7] : a['wednesday'] = "X"
        else : a['wednesday'] = " "

        if i[8] : a['checkedin'] = "X"
        else : a['checkedin'] = " "

        athletes.append(a)
        print(a, file=sys.stderr)


    return render_template('attending.html', athletes = athletes)

@app.route('/admin')
def admin():

    return render_template('admin.html')

@app.route('/admin/resetattendance')
def resetAttendance():

    db.reset_athlete_attendance()

    return redirect(url_for('admin'))

    


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)