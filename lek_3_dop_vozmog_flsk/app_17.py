from flask import Flask, render_template, request
from flask_wtf.csrf import CSRFProtect
from forms_3 import LoginForm, RegistrationForm

app = Flask(__name__)
app.config["SECRET_KEY"] = (
    b"a552cc79063c38bb5cf59769256b7a8c47ec9b98decd4eda60c2561c1f5b7eff"
)
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return "Hi!"


@app.route("/data/")
def data():
    return "Your data!"


@app.route("/login/", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST" and form.validate():
        # Обработка данных из формы
        pass
    return render_template("login.html", form=form)


@app.route("/register/", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if request.method == "POST" and form.validate():
        # Обработка данных из формы
        email = form.email.data
        password = form.password.data
        print(email, password)
    return render_template("register.html", form=form)


if __name__ == "__main__":
    app.run(debug=True)
