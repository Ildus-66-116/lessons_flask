from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hi"


@app.route("/for/")
def poems():
    context = {
        "poem": [
            "Вот не думал, не гадал,",
            "Программистом взял и стал.",
            "Хитрый знает он язык,",
            "Он к другому не привык.",
        ]
    }
    # txt = """<h1>Стихотворение</h1>\n<p>""" + '<br/>'.join(poem) + '</p>'
    return render_template("show_for.html", **context)


if __name__ == "__main__":
    app.run(debug=True)
