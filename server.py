from flask import Flask, request, session
from flask import render_template
from flask_babel import Babel, get_locale, lazy_gettext

app = Flask(__name__)
babel = Babel(app)

app.config['LANGUAGES'] = {
    'en': 'English',
    'es': 'Español'
}
app.config['SECRET_KEY'] = 'your-secret-key'

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        language = request.form['language']
        if language in app.config['LANGUAGES']:
            session['language'] = language
    return render_template('index.html', LANGUAGES=app.config['LANGUAGES'], get_locale=get_locale)

@app.route('/translate')
def translate():
    return lazy_gettext('Hello World')


@app.route('/contact.html')
def contact():
    return render_template("contact.html")


@app.route('/project.html')
def project():
    return render_template("project.html")


if __name__ == "__main__":
    app.run(debug=True)
