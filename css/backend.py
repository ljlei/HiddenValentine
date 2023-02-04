from flask import Flask, request
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6278b718883836facee2f0615967fe89"
# Your Auth Token from twilio.com/console
auth_token  = "263d249a42d34e18293b58fceeb1cdd2"

client = Client(account_sid, auth_token)

app = Flask(__name__)

@app.route("/")
def test():
    return "Test"

@app.route("/about")
def about():
    return "We're cool."

@app.route("/send_message", methods=["POST"])
def send_message():
    # Retrieve data from the request
    recipient = request.form.get("recipient")
    message_body = request.form.get("body")

    message = client.messages.create(
        to="+19097644355", 
        from_="+19093513871",
        body="Hello from Python!")

    return "Message sent"

if __name__ == "__main__":
    app.run()

