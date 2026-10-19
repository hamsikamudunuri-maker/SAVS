from flask import Flask, render_template, redirect, request

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

@app.route("/credits")
def credits():
    return render_template("credits.html")

# Google Forms for each school branch
school_forms = {
    "OSC": "https://docs.google.com/forms/d/e/1FAIpQLScif8yzQzDsvwyRpCiEosFfdebD3dl_jTzhMX7Rukc3v3e5Qw/viewform"
}

@app.route("/join")
def join():
    selected_school = request.args.get("school")

    if selected_school:
        form_url = school_forms.get(selected_school)

        if form_url:
            return redirect(form_url)

    return render_template("join.html")

if __name__ == "__main__":
    app.run(debug=True)
