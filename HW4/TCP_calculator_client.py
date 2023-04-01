from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 9999))

while True:
    msg = input('Write down the expression to calculate (+, - * /):')
    if msg == 'q':
        break

    s.send(msg.encode())  # 문자열을 bytes객체로 변경 후 전송

    print("Result: ", s.recv(1024).decode())

s.close()