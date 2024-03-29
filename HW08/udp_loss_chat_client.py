from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('-> ')
    reTx = 0
    while reTx < 4:
        # 메시지 붙여놓고 보내는것
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), ('localhost', port))
        sock.settimeout(2) # timeout 2초

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:
            reTx += 1
            continue
        else:
            break
    
    sock.settimeout(None)
    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        if random.random() <= 0.5:
            continue
        else:
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break



