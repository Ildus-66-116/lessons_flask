from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hi"


@app.route("/index/")
def html_index():
    return render_template("task_5.html")


@app.route("/index/catalog/catalog.html")
def html_catalog():
    return render_template("/catalog/catalog.html")


if __name__ == "__main__":
    app.run(debug=True)
