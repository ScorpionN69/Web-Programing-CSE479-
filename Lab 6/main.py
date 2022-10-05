import pymongo
from flask import Flask, render_template, request, redirect, session

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mydatabase"]
user = mydb["User"]

app = Flask(__name__)
app.config['SECRET_KEY'] = "12345678"


@app.route('/', methods=["GET", "POST"])
def index():
    name = ""
    if request.method == 'POST':
        session.pop("name", None)
    if "name" in session.keys():
        name = session["name"]
    else:
        name = "unknown"
    return render_template("index.html", **locals())


@app.route('/registration', methods=["GET", "POST"])
def reg():
    passMsg = 0
    unameMsg = 0
    if request.method == 'POST':
        uname = request.form["name"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        email = request.form["email"]
        allOk = 1
        passMsg = 0
        unameMsg = 0
        emailMsg = 0
        msg = ""
        if pass1 != pass2 or pass1 == "" or pass2 == "":
            pass1 = ""
            pass2 = ""
            passMsg = 1
            allOk = 0
        elif len(uname) < 8:
            uname = ""
            unameMsg = 1
            allOk = 0
        elif '@' not in email:
            email = ""
            emailMsg = 1
            allOk = 0
        else:
            if allOk == 1:
                data = {"uname": uname, "pass": pass2}
                user.insert_one(data)
                msg += "Successfully Registered"
                return render_template("reg_ok.html", **locals())
    return render_template("registration.html", **locals())


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        uname = request.form["name"]
        pass1 = request.form["pass"]
        find = list(user.find({"uname": uname, "pass": pass1}))
        msg = 0
        if bool(find):
            session["name"] = uname
            return redirect("/")
        else:
            msg = 1
    return render_template("login.html", **locals())


if __name__ == '__main__':
    app.run()
