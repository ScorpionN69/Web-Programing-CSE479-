import pymongo
from flask import Flask, render_template, request, redirect

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mydatabase"]
user = mydb["User"]

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html", **locals())


@app.route('/registration', methods=["GET", "POST"])
def reg():
    if request.method == 'POST':
        uname = request.form["name"]
        gen = request.form["gender"]
        dist = request.form["district"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        email = request.form["email"]
        allOk = 1
        passMsg = 0
        unameMsg = 1
        emailMsg = 0
        msg = ""
        if  pass1 != pass2:
            passMsg = 1
            allOk = 0
        elif len(uname)<8:
            unameMsg = 0
            allOk =0
        elif "@" not in email:
            emailMsg = 1
            allOk = 0
        else:
            if allOk == 1:
                data = {"uname": uname, "gender": gen, "district": dist, "pass": pass2, "email": email}
                user.insert_one(data)
                print(gen)
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
            return redirect("/")
        else:
            msg = 1
    return render_template("login.html", **locals())


if __name__ == '__main__':
    app.run()
