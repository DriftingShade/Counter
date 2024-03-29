from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "you can run but you cant hide"


@app.route("/")
def index():
    if "count" not in session:
        session["count"] = 0
    session["count"] += 1
    return render_template("index.html", count=session["count"])


@app.route("/addtwo")
def addtwo():
    session["count"] += 1
    return redirect("/")


@app.route("/reset")
def reset():
    session["count"] = 0
    return redirect("/")


@app.route("/addcustom")
def addcustom():
    if "custom" not in session:
        session["custom"] = 0
    session["count"] += session["custom"]
    return redirect("/")


# I ALMOST got this working, I just can't quite figure it out!!!  I will play with it some more.


if __name__ == "__main__":
    app.run(debug=True)
