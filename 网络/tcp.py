# @Time : 2019/5/27 10:21
# @Author : WZG
# --coding:utf-8--
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.243.69', 18084))
s.send(b'GET / HTTP/1.1\r\nHost: 192.168.243.69.\r\nConnection: close\r\n\r\n')
buffer = []
while True:
    d = s.recv(1024)
    if d:
        buffer.append(d)
    else:
        break
data = b''.join(buffer)

s.close()
header, html = data.split(b'\r\n\r\n', 1)
print(header.decode('utf-8'))
with open('airport.html', 'wb') as f:
    f.write(html)

