from socket import *

port = 9999
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)

while True:
    msg = input('Enter the message(\"send mboxId message" or \"received mboxId\"): ')

    if msg == 'quit':
        sock.sendto(msg.encode(), ('localhost', port))
        break
    else:
        sock.sendto(msg.encode(), ('localhost', port))
        data, addr = sock.recvfrom(BUFF_SIZE)
        print(data.decode())

sock.close()