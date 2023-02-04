import os
from twilio.rest import Client
from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/', methods=['POST'])
def sendMsg():
    if request.method == 'POST':
        toNum = request.form['toNum']
        msg = request.form['msg']
        account_sid = os.environ[AC644186d0c45f4f77efeeff235a316d00]
        auth_token = os.environ[074f2d8473c2f7687f673b33db0fc4e8]
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
                body=msg,
                from_='+18883148923',
                to=toNum
            )

        print(message.sid)
	return;