from flask import Flask, request, session, redirect, url_for
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
        mail = request.form['email']
        with open('https://raw.githubusercontent.com/SegundoP/Web-Wanabot/master/mails.txt', 'a+') as f:
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


# Definir la ruta para la página de inicio de sesión
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Recibir los datos del formulario de inicio de sesión
        username = request.form["username"]
        password = request.form["password"]

        # Verificar si las credenciales son válidas
        # Aquí debes buscar en la base de datos al usuario correspondiente y verificar
        # si la contraseña proporcionada coincide con la contraseña encriptada en la base de datos.
        # En este ejemplo, asumimos que el usuario y la contraseña son válidos.
        if username == "example_user" and password == "example_password":
            return redirect(url_for("formulario"))
        else:
            # Si las credenciales no son válidas, redirigir al usuario a la página de inicio de sesión con un mensaje de error
            error_message = "Usuario o contraseña incorrectos"
            return render_template("login.html", error_message=error_message)
    else:
        # Mostrar la página de inicio de sesión
        return render_template("login.html")


# Definir la ruta para el formulario
@app.route("/formulario", methods=["GET", "POST"])
def formulario():
    if request.method == "POST":
        # Recibir los datos del formulario
        codigo_proveedor = request.form["codigo_proveedor"]
        fecha = request.form["fecha"]
        moneda = request.form["moneda"]
        codigo_item = request.form["codigo_item"]
        cantidad = request.form["cantidad"]
        precio = request.form["precio"]

        # Enviar un POST request a la API
        response = request.post("https://example.com/api", json={
            "codigo_proveedor": codigo_proveedor,
            "fecha": fecha,
            "moneda": moneda,
            "codigo_item": codigo_item,
            "cantidad": cantidad,
            "precio": precio
        })

        # Verificar si el POST request fue exitoso
        if response.status_code == 200:
            # Mostrar un mensaje de confirmación al usuario
            success_message = "El formulario ha sido enviado exitosamente"
            return render_template("formulario.html", success_message=success_message)
        else:
            # Si el POST request no fue exitoso, mostrar un mensaje de error al usuario
            error_message = "Ha ocurrido un error al enviar el formulario"
            return render_template("formulario.html", error_message=error_message)
    else:
        # Mostrar el formulario
        return render_template("formulario.html")


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
def projectRPA():
    return render_template("projectRPA.html")

@app.route('/projectDashboards.html')
def projectDash():
    return render_template("projectDashboards.html")

@app.route('/projectPurchaseOrders.html')
def projectPO():
    return render_template("projectPurchaseOrders.html")

@app.route('/projectInvoices.html')
def projectBilling():
    return render_template("projectInvoices.html")

@app.route('/projectAPIs.html')
def projectAPIs():
    return render_template("projectAPIs.html")

if __name__ == "__main__":
    app.run(debug=True)
