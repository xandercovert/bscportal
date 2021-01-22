from twilio.rest import Client
import os
import sys

# Set ENV variables from twilio.env
os.system("source ./twilio.env")

# Your Account SID from twilio.com/console
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
print(account_sid, file=sys.stderr)

# Your Auth Token from twilio.com/console
auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17163614799", 
    from_="+13124719264",
    body="Hello from Python!")

print(message.sid)
