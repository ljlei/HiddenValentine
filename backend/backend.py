import config, classes
from flask import Flask, request, render_template, flash, redirect
from twilio.rest import Client
from backend.classes import Valentine

# Your Account SID from twilio.com/console
account_sid = "AC6278b718883836facee2f0615967fe89"
# Your Auth Token from twilio.com/console
auth_token  = config.api_key

client = Client(account_sid, auth_token)

app = Flask(__name__, template_folder="templateFiles")

@app.route("/", methods=['GET', 'POST'])
def main_page():
    form = Valentine()
    if form.validate_on_submit():
        pass
    student = {'student' : 'UCI Student'}
    return render_template('test.html', student=student)

@app.route("/about")
def about():
    return "We're cool."

@app.route("/send_message", methods=["POST"])
def send_message():
    # Retrieve data from the request
    recipient = request.form.get("recipient")
    message = request.form.get("message")

    message = client.messages.create(
        recipient="+19097644355",
        from_="+19093513871",
        message="Hello from Python!")

    return "Message sent!"

if __name__ == "__main__":
    app.run(debug=True)

