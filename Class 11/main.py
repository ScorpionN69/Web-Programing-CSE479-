import pymongo
from flask import Flask, render_template, request

app = Flask(__name__)

client = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = client["mydatabase"]
data = mydb["dummy"]


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        d = dict()
        name = request.form["name"]
        d["name"] = name
        if "value1" in request.form.keys():
            value1 = request.form["value1"]
            d["value1"] = value1
        if "value2" in request.form.keys():
            value2 = request.form["value2"]
            d["value2"] = value2
        if "value3" in request.form.keys():
            value3 = request.form["value3"]
            d["value3"] = value3
        print(d)
        data.insert_one(d)
    return render_template("index.html", **locals())


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
