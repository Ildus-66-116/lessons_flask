from flask import Flask
from models_02 import db

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///mydatabase.db"
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@hostname/database_name'
db.init_app(app)


@app.route("/")
def index():
    return "Hi!"


if __name__ == "__main__":
    app.run(debug=True)
