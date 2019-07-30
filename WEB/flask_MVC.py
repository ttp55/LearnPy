# @time:  2019/7/15 15:27
# @author: WZG
# encoding: utf-8

from flask import Flask
from flask import request, render_template
from WEB import db


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=["POST"])
def signin():
    db.con()
    while True:
        for i in range(len(db.con())):
            if request.form['username'] == db.con()[i][0] and request.form['password'] == db.con()[i][1]:
                return render_template('signin-ok.html', username=db.con()[i][0])
        return render_template('form.html', message='Bad username or password', username=request.form['username'])


if __name__ == '__main__':
    app.run()
