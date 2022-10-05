
from flask import Flask, render_template, request
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["data"]
table = mydb["Box"]
app = Flask(__name__)



@app.route('/cbox', methods=['GET', 'POST'])
def cbox():
    if request.method == 'POST':
        d = dict()
        if request.form.get('HTML'):
            d['HTML'] = 'HTML'
        if request.form.get('CSS'):
            d['CSS'] = 'CSS'
        table.insert_one(d)
    return render_template("checkbox.html", **locals())


if __name__ == '__main__':
    app.run()
