from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC46cb74ed3bd9bb509a2d6b378dc49542"
# Your Auth Token from twilio.com/console
auth_token  = "dd13d4535eb91011f9c96e83d5c917d0"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17163614799", 
    from_="+13124719264",
    body="Hello from Python!")

print(message.sid)
