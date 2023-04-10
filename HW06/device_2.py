from socket import *
import random

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9999))
sock.listen()
user, addr = sock.accept()

while True:
    msg = user.recv(1024).decode()

    if msg == 'Request':

        Heartbeat = random.randint(40, 140)
        Steps = random.randint(2000, 6000)
        Cal = random.randint(1000, 4000)

        msg = f"Heartbeat={Heartbeat}, Steps={Steps}, Cal={Cal}"
        
        user.send(msg.encode())
    elif msg == 'quit':
        sock.close()
        break
    else:
        print("error!")
