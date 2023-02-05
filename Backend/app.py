import config
from flask import Flask, request, render_template, redirect, url_for
from twilio.rest import Client
from classes import Valentine

account_sid = config.account_sid
auth_token  = config.api_key
client = Client(account_sid, auth_token)

app = Flask(__name__, template_folder="templateFiles", static_folder='staticFiles')
app.config['SECRET_KEY'] = config.secret_key

@app.route("/", methods=['GET', 'POST'])
def main_page():
    form = Valentine()
    if form.validate_on_submit():
        send_message()
    return render_template('test.html', form=form)

@app.route("/about")
def about():
    return "We're cool."

def send_message():
    recipient = request.form.get("recipient")
    valentine = request.form.get("valentine")

    client.messages.create(
        to=recipient,
        from_=config.twilio_number,
        body=valentine)

if __name__ == "__main__":
    app.run(debug=True)

# return redirect('/')