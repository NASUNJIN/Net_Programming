import socket

port = 9999
BUFF_SIZE = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', port))

mbox_index = {}

while True:
    data, addr = sock.recvfrom(BUFF_SIZE)

    if data.decode() == 'quit':
        break
    
    check, mboxID, *msg = data.decode().split()
    msg = " ".join(msg) # 문자열 합치기 (띄워쓰기)

    if check == 'send':
        if mboxID not in mbox_index:
            mbox_index[mboxID] = []

        # append(x) : 새로운 요소를 맨 끝에 객체로 추가
        # insert(i, x) : i위치에 x 삽입 가능 값 x 는 객체로 추가
        mbox_index[mboxID].append(msg)

        sock.sendto("OK".encode(), addr)

    elif check == 'recive':
        # mboxID가 mbox_index에 없거나
        # mbox_index에 mboxID가 존재하지만 메시지가 없을 경우
        if (mboxID not in mbox_index) or (not bool(mbox_index[mboxID])):
            sock.sendto("No messages".encode(), addr)
        else:
            # mbox_index의 mboxID의 첫번째 메시지 전달 후 삭제
            sock.sendto(mbox_index[mboxID].pop(0).encode(), addr)

sock.close()



        

