from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/database_name'
db = SQLAlchemy(app)


@app.route("/")
def index():
    return "Hi!"


if __name__ == "__main__":
    app.run(debug=True)
