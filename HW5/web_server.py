from socket import *

s = socket()
s.bind(('', 80))
s.listen(10)

while True:
    c, addr = s.accept()
    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    filename = req[0].split()[1].split('/')[1]  # 공백 + '/'으로 분류

    if filename == 'index.html':
        f = open(filename, 'r', encoding='utf-8')
        mimeType = 'text/html'
        data = f.read()
        # HTTP 헤더 전송
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(data.encode('euc-kr'))

    elif filename == 'iot.png':
        f = open(filename, 'rb')
        mimeType = 'image/png'
        data = f.read()
        # HTTP 헤더 전송
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(data)

    elif filename == 'favicon.ico':
        f = open(filename, 'rb')
        mimeType = 'image/x-icon'
        data = f.read()
        # HTTP 헤더 전송
        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: ' + mimeType.encode() + b'\r\n')
        c.send(b'\r\n')
        c.send(data)

    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<HTML><HEAD><TITLE>Not Found</TITLE></HEAD>')
        c.send(b'<BODY>Not Found</BODY></HTML>')

    c.close()