import socket

port = 9999
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('', port))
sock.listen(1)

mbox_index = {}

while True:
    conn, addr = sock.accept()
    print(f"Connected by {addr}")

    while True:
        data = conn.recv(BUFF_SIZE)
        
        check, mboxID, *msg = data.decode().split()
        msg = " ".join(msg) # 문자열 합치기 (띄워쓰기)
        
        if not data:
            break

        if data.decode() == 'quit':
            break

        if check == 'send':
            if mboxID not in mbox_index:
                mbox_index[mboxID] = []

            # append(x) : 새로운 요소를 맨 끝에 객체로 추가
            # insert(i, x) : i위치에 x 삽입 가능 값 x 는 객체로 추가
            mbox_index[mboxID].append(msg)
            conn.sendall("OK".encode())

        elif check == 'receive':
            # mboxID가 mbox_index에 없거나
            # mbox_index에 mboxID가 존재하지만 메시지가 없을 경우
            if (mboxID not in mbox_index) or (not bool(mbox_index[mboxID])):
                conn.sendall("No messages".encode())
            else:
                # mbox_index의 mboxID의 첫번째 메시지 전달 후 삭제
                conn.sendall(mbox_index[mboxID].pop(0).encode())

    conn.close()
    sock.close()