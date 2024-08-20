from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__)
app.config["SECRET_KEY"] = (
    b"a552cc79063c38bb5cf59769256b7a8c47ec9b98decd4eda60c2561c1f5b7eff"
)
csrf = CSRFProtect(app)


@app.route("/")
def index():
    return "Hi!"


@app.route("/form", methods=["GET", "POST"])
@csrf.exempt  # без секретного ключа данные не защищены
def my_form():
    return "No CSRF protection"


if __name__ == "__main__":
    app.run(debug=True)
