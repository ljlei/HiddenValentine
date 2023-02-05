import config, time
from flask import Flask, request, render_template, redirect, url_for
from twilio.rest import Client
from classes import Valentine

account_sid = config.account_sid
auth_token  = config.api_key
client = Client(account_sid, auth_token)

app = Flask(__name__, template_folder="templateFiles", static_folder='staticFiles')
app.config['SECRET_KEY'] = config.secret_key

@app.route("/home")
@app.route("/home", methods=['GET', 'POST'])
def main_page():
    form = Valentine()
    if form.validate_on_submit():
        send_message()
        return redirect(url_for('confirmation'))
    return render_template('index.html', form=form)

@app.route("/home")
def home():
    return render_template('index.html')

@app.route("/confirmation", methods=['GET', 'POST'])
def confirmation():
    return render_template('confirmation.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')

def send_message():
    recipient = request.form.get("recipient")
    valentine = request.form.get("valentine")

    confirmation = client.messages.create(
        to=recipient,
        from_=config.twilio_number,
        body=valentine)
    
    print(confirmation)
    
@app.route('/', defaults={'path': '/home'})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")

if __name__ == "__main__":
    app.run(debug=True)