from socket import *
import argparse

s = socket(AF_INET, SOCK_STREAM)

# ArgumentParser 객체 생성 : 
# 명령행을 파이썬 데이터로 파싱하는데 필요한 모든 정보를 담고 있음
parser = argparse.ArgumentParser()
# addr_argument() : 인자 추가하기 메소드 호출
parser.add_argument('-s', default='localhost')
parser.add_argument('-p', type=int, default=2500)
# parse_args() : 메소드를 통해 인자 파싱
args = parser.parse_args()

s.connect((args.s, args.p))
print('connected to ', args.s, args.p)

while True:
    msg = input("Message to send: ")
    if msg == 'q':
        break
    s.send(msg.encode())
    data = s.recv(1024)
    if not data:
        break
    print('Recived message: ', data.decode())

s.close()