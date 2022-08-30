from flask import *
import pymongo

db_client = pymongo.MongoClient("mongodb://localhost:27017/")
db = db_client["user"]

app = Flask(__name__)
app.config["SECRET_KEY"]="sidfhgbauidfui"

@app.route('/', methods=['GET', 'POST','DELETE'])
def fuc():
    name=""
    if request.method =='POST':
        session.pop('name',None)
    else:
        name = session["name"]
    return render_template("3.html",**locals())


@app.route("/login", methods=['POST','GET'])
def home():
    users = list(db.user_info.find())
    f = False
    if request.method == 'POST':
        username = request.form["name"]
        pass1 = request.form["Password"]

        for x in users:
            if x['username']==username and x['password']==pass1:
                f = True
                session["name"]=username
                return redirect(url_for('fuc'))

    return render_template("2.html",**locals())

@app.route('/reg', methods=['GET', 'POST','DELETE'])
def index():
    usr = True
    passs = True
    mail = True
    if request.method == 'POST':
        username = request.form["name"]
        pass1 = request.form["Password"]
        pass2 = request.form["Confirm Password"]
        mail = request.form["email"]

        if len(username)<8:
            usr = False
        elif pass1!=pass2:
            passs = False
        elif '@' not in mail:
            mail = False
        else:
            user = dict()
            user["username"]=username
            user["password"]=pass1
            user["email"]=mail
            db.user_info.insert_one(user)
    return render_template("1.html",**locals())


if __name__ == '__main__':
    app.run()
