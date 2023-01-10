from flask import Flask, request, session
from flask import render_template
from flask_babel import Babel, get_locale, lazy_gettext
import smtplib
# import requests

OWN_EMAIL = "pythontest@gmail.com"
OWN_PASSWORD = "pythonudemy"

app = Flask(__name__)
babel = Babel(app)

app.config['LANGUAGES'] = {
    'en': 'English',
    'es': 'Español'
}
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/', methods=['GET', 'POST'])
def home():
    try:
        mailRegistration()
    finally:
        return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def mailRegistration():
    if request.method == "POST":
        mail = request.form["email"]
        with open('mails.txt', 'a+') as f:
            f.write(mail + '\n')
        mail = ''
        # return render_template("index.html")

@app.route('/translate')
def translate():
    return lazy_gettext('Hello World')


# @app.route('/contact.html')
# def contact():
#     return render_template("contact.html")

# @app.route('/contact.html', methods=["POST"])
# def contact():
#     data = request.form
#     send_email(data["name"], data["email"], data["phone"], data["message"])
#     return render_template("contact.html", msg_sent=True)

@app.route("/contact.html", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, "cristian.miguens@wanabot.com", email_message)



# @app.route("/contact.html", methods=["GET", "POST"])
# def contact():
#     if request.method == "POST":
#         data = request.form
#         print(data["name"])
#         print(data["email"])
#         print(data["subject"])
#         print(data["message"])
#         return render_template("contact.html", msg_sent=True)
#     return render_template("contact.html", msg_sent=False)

@app.route('/projectRPA.html')
def project():
    return render_template("projectRPA.html")


if __name__ == "__main__":
    app.run(debug=True)
