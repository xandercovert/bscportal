from sys import stderr
import mysql.connector
from mysql.connector import errorcode
import os
import sys


def connect():

    database = mysql.connector.connect(user='trqiusemyygmrj5a',
                                       password='zyss3c6bn16f0h59',
                                       host='j21q532mu148i8ms.cbetxkdyhwsb.us-east-1.rds.amazonaws.com',
                                       database='jn9jzqsjtw954bwf'
                                       )

    return database

def get_athlete(athletelname):
    inputCommand = "SELECT athlete_id, fname, lname, email, cell FROM athletes WHERE lname = (%s) "
    try:
        conn = connect()
        statement = conn.cursor(prepared=True)
        statement.execute(inputCommand, (athletelname,))
        rs = statement.fetchall()
        statement.close()
        conn.close()

        return rs

def get_all_athletes():
    inputCommand = "SELECT * FROM athletes"
    try:
        conn = connect()
        statement = conn.cursor(prepared=True)
        x = ()
        statement.execute(inputCommand, (x,))
        rs = statement.fetchall()
        statement.close()
        conn.close()

        return rs