from socket import *
import random

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('', 9000))
sock.listen()
user, addr = sock.accept()

while True:
    msg = user.recv(1024).decode()

    if msg == 'Request':

        Temp = random.randint(0, 40)
        Humid = random.randint(0, 100)
        Iilum = random.randint(70, 150)

        msg = f"Temp={Temp}, Humid={Humid}, Iilum={Iilum}"
        
        user.send(msg.encode())
    elif msg == 'quit':
        sock.close()
        break
    else:
        print("error!")
