from flask import *
import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = db_client["student1"]

app = Flask(__name__)

@app.route("/show", methods=['POST','GET'])
def home():
    stu = list(db.student1_info.find())
    return render_template("table.html", **locals())

@app.route('/input', methods=['GET', 'POST','DELETE'])
def index():
    if request.method == 'POST':

        id = request.form["id"]
        username = request.form["name"]
        age = request.form["age"]
        phone = request.form["phone"]
        address = request.form["address"]


        student = dict()
        student['id'] = id
        student['name'] = username
        student['age'] = age
        student['phone'] = phone
        student['address'] = address

        db.student1_info.insert_one(student)

    return render_template("home.html",**locals())


if __name__ == '__main__':
    app.run()

