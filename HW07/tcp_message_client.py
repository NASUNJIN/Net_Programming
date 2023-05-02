from socket import *

port = 9999
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.connect(('', port))

while True:
    msg = input('Enter the message(\"send mboxId message" or \"received mboxId\"): ')

    if msg == 'quit':
        sock.send(msg.encode())
        break
    
    else:
        sock.send(msg.encode())
        data = sock.recv(BUFF_SIZE)
        print(data.decode())

sock.close()