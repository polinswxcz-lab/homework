from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", page="home")


@app.route("/about")
def about():
    return render_template("index.html", page="about")


@app.route("/skills")
def skills():
    return render_template("index.html", page="skills")


@app.route("/contact")
def contact():
    return render_template("index.html", page="contact")


@app.route("/temperature/<int:t>")
def temperature(t):

    if t < 0:
        return "Мороз"

    elif 0 <= t <= 20:
        return "Прохолодно"

    elif 20 < t < 30:
        return "Тепло"

    else:
        return "Спека"


@app.route("/math/<operation>/<int:a>/<int:b>")
def math(operation, a, b):

    if operation == "add":
        return str(a + b)

    elif operation == "sub":
        return str(a - b)

    elif operation == "mul":
        return str(a * b)

    elif operation == "div":
        if b == 0:
            return "Ділення на нуль неможливе"
        return str(a / b)

    else:
        return "Невідома операція"


if __name__ == "__main__":
    app.run(debug=True)