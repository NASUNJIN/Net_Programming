import socket
import threading
import time

clients= [] # 클라이언트 목록

def serverTask(conn, addr):
    while True:
        data = conn.recv(1024)

        # 'quit' 수신 시 해당 클라이언트를 목록에서 삭제
        if 'quit' in data.decode():
            if conn in clients:
                print(addr, 'exited')
                clients.remove(conn)
                continue

        print(time.asctime() + str(addr) + ':' + data.decode())

        # 모든 클라이언트에게 전송
        for client in clients:
            if client != conn:  # 나를 제외한 모든 사람
                client.send(data)
        
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 2500))
s.listen(10)

print('Server Started')

while True:
    conn, addr = s.accept()
    clients.append(conn)
    print('new clinet', addr)
    th = threading.Thread(target=serverTask, args=(conn, addr))
    th.start()


