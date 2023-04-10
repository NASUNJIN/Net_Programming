from socket import *
import time

sock_1 = socket(AF_INET,SOCK_STREAM)
sock_1.connect(('localhost',9000))

sock_2 = socket(AF_INET,SOCK_STREAM)
sock_2.connect(('localhost',9999))

f = open('data.txt','w')

while True:
    msg = input('Input Device Number: ')
    if msg == 'quit':
        sock_1.send(b'quit')
        sock_2.send(b'quit')
        break
    elif msg == '1':
        sock_1.send(b'Request')
        data = sock_1.recv(1024).decode()
        f = open('data.txt','a')
        f.write(f"{time.strftime('%c', time.localtime(time.time()))} Device1: {data}\n")
    elif msg == '2':
        sock_2.send(b'Request')
        data = sock_2.recv(1024).decode()
        f = open('data.txt','a')
        f.write(f"{time.strftime('%c', time.localtime(time.time()))} Device2: {data}\n")

    else: # 그 외 값 (예외처리)
        print("You entered wrong value!")
        print("Please enter \"1\", \"2\" or \"quit!\"")

sock_1.close()
sock_2.close()
f.close()
