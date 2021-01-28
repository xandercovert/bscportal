from sys import stderr
import mysql.connector
from mysql.connector import errorcode
import os
import sys


def connect():

    database = mysql.connector.connect(user='ipopqe3ojfodhxqh',
                                       password='thsqkh5u8z0o4duk',
                                       host='z5zm8hebixwywy9d.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                       database='zjcv0ume6hjfv1ze'
                                       )

    return database

def get_athlete(athletelname):
    inputCommand = "SELECT athlete_id, fname, lname, email, cell, checkedin FROM athletes WHERE lname = (%s) "
   
    conn = connect()
    statement = conn.cursor()
    statement.execute(inputCommand, (athletelname,))
    rs = statement.fetchall()
    statement.close()
    conn.close()

    return rs

def get_athlete_by_id(athletelname):
    inputCommand = "SELECT athlete_id, fname, lname, email, cell, checkedin FROM athletes WHERE athlete_id = (%s) "
   
    conn = connect()
    statement = conn.cursor()
    statement.execute(inputCommand, (athletelname,))
    rs = statement.fetchone()
    statement.close()
    conn.close()

    return rs

def get_all_athletes():
    inputCommand = "SELECT athlete_id, fname, lname, email, cell, saturday, sunday, wednesday, checkedin FROM athletes"
    
    conn = connect()
    statement = conn.cursor()
    x = ()
    statement.execute(inputCommand)
    rs = statement.fetchall()
    statement.close()
    conn.close()

    return rs

def get_athlete_days(athletelname):
    inputCommand = "SELECT saturday, sunday, wednesday FROM athletes WHERE athlete_id = (%s) "
   
    conn = connect()
    statement = conn.cursor()
    statement.execute(inputCommand, (athletelname,))
    rs = statement.fetchone()
    statement.close()
    conn.close()

    return rs

def set_athlete_days(saturday, sunday, wednesday, checkedin, athletelname):
    inputCommand = "UPDATE athletes SET saturday = %s, sunday = %s, wednesday = %s, checkedin = %s WHERE athlete_id = (%s) "
   
    conn = connect()
    statement = conn.cursor()
    statement.execute(inputCommand, (saturday, sunday, wednesday, checkedin, athletelname,))
    conn.commit()
    statement.close()
    conn.close()

    return True

def reset_athlete_attendance():
    inputCommand = "UPDATE athletes SET saturday = %s, sunday = %s, wednesday = %s, checkedin = %s "
   
    conn = connect()
    statement = conn.cursor()
    statement.execute(inputCommand, (0, 0, 0, 0,))
    conn.commit()
    statement.close()
    conn.close()

    return True