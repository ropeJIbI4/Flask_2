from flask import Flask, request, redirect, make_response, render_template, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    name = request.form["name"]
    email = request.form["email"]
    response = make_response(render_template("welcome.html", name=name))
    response.set_cookie("name", name)
    response.set_cookie("email", email)
    return response


@app.route("/logout")
def logout():
    response = make_response(redirect(url_for("index")))
    response.set_cookie("name", "", expires=0)
    response.set_cookie("email", "", expires=0)
    return response


if __name__ == "__main__":
    app.run()
