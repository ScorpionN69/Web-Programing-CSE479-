import pymongo
from flask import Flask, render_template, request

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mydatabase"]
student = mydb["Student"]
user = mydb["User"]

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form["name"]
        mark = request.form["mark"]
        data = {"name": name, "mark": mark}
        student.insert_one(data)
        for i in student.find():
            print(i)
    return render_template("index.html", **locals())


@app.route('/delete', methods=['GET', 'POST'])
def delete():
    if request.method == 'POST':
        name = request.form["name"]
        student.delete_many({"name": name})
    return render_template("delete.html", **locals())


@app.route('/find', methods=['GET', 'POST'])
def find():
    if request.method == 'POST':
        name = request.form["name"]
        sum = 0
        for i in student.find({"name": name}):
            sum += int(i["mark"])
    return render_template("find.html", **locals())


@app.route('/registration', methods=["GET", "POST"])
def reg():
    if request.method == 'POST':
        name = request.form["name"]
        pass1 = request.form["pass1"]
        pass2 = request.form["pass2"]
        msg =""
        if pass1 == pass2:
            data = {"name": name, "pass": pass2}
            user.insert_one(data)
            msg += "Successfully Registered"
        else:
            msg += "Password Didn't Match"
    return render_template("registration.html", **locals())



if __name__ == '__main__':
    app.run()


