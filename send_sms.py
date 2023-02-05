

import twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6278b718883836facee2f0615967fe89"
# Your Auth Token from twilio.com/console
auth_token  = "263d249a42d34e18293b58fceeb1cdd2"

client = Client(account_sid, auth_token)

def text():
    message = client.messages.create(
        to="+19097644355", 
        from_="+19093513871",
        body="Hello from Python!")

# print(message.sid) If sid of message is needed.