from socket import *
import random
import time

port = 3333
BUFF_SIZE = 1024

sock = socket(AF_INET, SOCK_DGRAM)
sock.bind(('', port))

while True:
    sock.settimeout(None)   # 소켓의 블로킹 모드 timeout 설정
    while True:             # None일 경우, 무한정 블로킹 됨
        data, addr = sock.recvfrom(BUFF_SIZE)

        if random.random() <= 0.5:  # 0 ~ 1 사이의 값이 나옴 즉 확률 50%
            continue 
        else:  # 메시지 손실 되지 않을 경우 'ack'응답 보냄
            sock.sendto(b'ack', addr)
            print('<- ', data.decode())
            break
    
    msg = input ('-> ')
    reTx = 0
    # 재전송 횟수가 5번 이하일 경우, 메시지 전송
    while reTx < 5:
        resp = str(reTx) + ' ' + msg
        sock.sendto(resp.encode(), addr)
        # 소켓의 timeout 설정, 해당 timeout 내 메시지 수신 못하면 timeout 예외 발생
        sock.settimeout(2)    

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except timeout:  # timeout 발생할 경우
            # 재전송 횟수를 1 증가 시킨 후 재전송
            reTx += 1
            continue
        else:
            break