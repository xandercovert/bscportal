from twilio.rest import Client
import os
import sys
import db

# Set ENV variables from twilio.env
os.system("source ./twilio.env")

# Your Account SID from twilio.com/console
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
print(account_sid, file=sys.stderr)

# Your Auth Token from twilio.com/console
auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)


allAthletes = db.get_all_athletes()

numbers = []
for i in allAthletes:
    a =  {
        'cell': i[4], 
        'lastName': i[2]
        }

    if not a in numbers:
        numbers.append(a)

for i in numbers:
    cell = '+1' + i['cell']
    print(cell)

    lastName = i['lastName']
    print(lastName)

    message = client.messages.create(
    to=cell, 
    from_="+13124719264",
    body="Check in your kids for Saturday, Sunday, and Wednesday's practice! bscportal.herokuapp.com/family/" + lastName + ". Thanks!")

    print(message.sid)

message = client.messages.create(
    to="+17163614799", 
    from_="+13124719264",
    body="Messages Sent!")

print(message.sid)