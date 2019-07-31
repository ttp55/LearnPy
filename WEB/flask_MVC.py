# @time:  2019/7/15 15:27
# @author: WZG
# encoding: utf-8

from flask import Flask
from flask import request, render_template
from WEB import db
from tkinter import messagebox
import threading


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
    sql = ('insert into users value(%s,%s);' % (uu, pp))
    for i in range(len(db.con())):
        if uu == db.con()[i][0]:
            messagebox.showinfo('用户已被注册')
            return render_template('signup.html')
    db.ins(sql)
    messagebox.showinfo('注册成功！')
    return render_template('form.html')


if __name__ == '__main__':
    app.run()
