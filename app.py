from flask import Flask, render_template, request, flash
from modules.usuario import registro
from dotenv import load_dotenv
load_dotenv()
app = Flask(__name__)
app.secret_key = 'your_secret_key'

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        apellido = request.form.get("Apellido")
        corro = request.form.get("Correo")
        contrasenia = request.form.get("Contrasenia")
        confirmacion = request.form.get("Confirmar")
        ocupacion = request.form.get("Ocupacion")

        if not nombre or not apellido or not corro or not contrasenia or not confirmacion or not ocupacion:
            flash("Error: Todos los campos son requeridos")

        if contrasenia != confirmacion:
            flash("Error: Las contraseñas no coinciden")
        getRegister = registro(nombre, apellido, corro, ocupacion, contrasenia)    
        print("register: ")
        print(getRegister)

    return render_template("register.html")


if __name__ == "__main__":
    app.run(debug=True)

