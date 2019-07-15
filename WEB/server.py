# @time:  2019/7/15 15:12
# @author: WZG
# encoding: utf-8

from wsgiref.simple_server import make_server
from WEB.ser import application


httpd = make_server('', 10002, application)
print('Serving HTTP on port 10002')

httpd.serve_forever()
