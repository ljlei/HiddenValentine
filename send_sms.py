# import os
# from twilio.rest import Client
# from flask import Flask
# from flask import request

# app = Flask(__name__)

# #@app.route('/', methods=['POST'])
# def sendMsg():
#     if request.method == 'POST':
#         toNum = request.form['toNum']
#         msg = request.form['msg']
#         account_sid = os.environ[AC644186d0c45f4f77efeeff235a316d00]
#         auth_token = os.environ[074f2d8473c2f7687f673b33db0fc4e8]
#         client = Client(account_sid, auth_token)

#         message = client.messages.create(
#             body=msg,
#             from_='+18883148923',
#             to=toNum
#         )

#         print(message.sid)
#         return;'

import twilio
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6278b718883836facee2f0615967fe89"
# Your Auth Token from twilio.com/console
auth_token  = "047c628720d6233389dafdbb49cb7eb2"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+19097644355", 
    from_="+19093513871",
    body="Hello from Python!")

print(message.sid)