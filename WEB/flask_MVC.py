# @time:  2019/7/15 15:27
# @author: WZG
# encoding: utf-8

from flask import Flask
from flask import request, render_template
from WEB import db
import re


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


@app.route('/signup', methods=["POST"])
def signup_form():
    return render_template('signup.html', username=request.form['username'])


@app.route('/signup1', methods=["POST"])
def signup():
    db.con()
    uu = request.form['username']
    pp = request.form['password']
    pp1 = request.form['password1']
    sql = ('insert into users(user, pass) values(%s, %s);' % (uu, pp))
    if pp != pp1:
        return render_template('signup.html', message='两次输入密码的不一致！')
    elif re.match(r'^[0-9a-zA-Z]+$', pp) is None or re.match(r'^[0-9a-zA-Z]+$', pp1) is None:
        return render_template('signup.html', message='密码必须为数字和字母！')

    for i in range(len(db.con())):
        if uu == db.con()[i][0]:
            return render_template('signup.html', message='用户已被注册！')
    try:
        db.ins(sql)
        return render_template('form.html', message='注册成功！')
    except Exception as e:
        print(e)


if __name__ == '__main__':
    app.run()
