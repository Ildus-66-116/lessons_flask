from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = b"a67608193315986f06ef33c81b9ff8c1ad9da138248193da26555df7634f071d"


@app.route("/")
def index():
    return "<h1>Hello world!</h1>"


@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Проверка данных формы
        if not request.form["name"]:
            flash("Введите имя!", "danger")
            return redirect(url_for("form"))
        # Обработка данных формы
        flash("Форма успешно отправлена!", "success")
        return redirect(url_for("form"))
    return render_template("form.html")


if __name__ == "__main__":
    app.run(debug=True)
