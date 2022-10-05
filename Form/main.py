from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/form', methods=['POST', 'GET'])
def form():
    if request.method=='POST':
        print(request.form["name"])
    return render_template('form.html')

app.run(host='localhost', port=5000)