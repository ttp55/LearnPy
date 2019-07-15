# @time:  2019/7/15 15:27
# @author: WZG
# encoding: utf-8

from flask import Flask
from flask import request, render_template


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@app.route('/signin', methods=['GET'])
def signin_form():
    return render_template('form.html')


@app.route('/signin', methods=["POST"])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return render_template('signin-ok.html', username='Tom')
    return render_template('form.html', message='Bad username or password', username='username')


if __name__ == '__main__':
    app.run()
