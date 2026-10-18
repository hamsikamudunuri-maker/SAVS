from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/updates")
def updates():
    return render_template("updates.html")

@app.route("/schools")
def schools():
    return render_template("schools.html")

@app.route("/join")
def join():
    return render_template("join.html")

if __name__ == "__main__":
    app.run(debug=True)
