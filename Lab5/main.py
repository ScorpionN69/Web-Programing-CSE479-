import pymongo
from flask import Flask, render_template, request

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mydatabase"]
student = mydb["Student"]

app = Flask(__name__)


@app.route('/input', methods=['GET', 'POST'])
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


if __name__ == '__main__':
    app.run()
