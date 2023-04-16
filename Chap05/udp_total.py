import argparse, socket, random
from datetime import datetime

BUFF_SIZE = 1024

def Server(ipaddr, port):   # 서버 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((ipaddr, port))
    print('Waiting in {} ...' .format(sock.getsockname()))

    while True:
        data, addr = sock.recvfrom(BUFF_SIZE)
        # random() : 0부터 1까지
        if random.random() < prob:  # prob : 일정 비율에 따라 메시지에 응답 안보냄
            print('Message from {} is lost.' .format(addr))  # 버리는 것
            continue
        # {lr} : 문자열 처럼 출력해라
        print('{} client message {!r}' .format(addr, data.decode()))
        # 클라이언트에서 받은 메시지의 바이트 수를 계산하여 응답
        text = 'The length is {} bytes.' .format(len(data))
        sock.sendto(text.encode(), addr)

def Client(hostname, port) :  # 클라이언트 함수
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    index = 1   # 보낸 메시지 번호
    time = 0.1  # seconds
    while True:
        # 현재 시간 문자열로 바꾼 후 전송
        data = str(datetime.now())
        sock.sendto(data.encode(), (hostname, port))
        print('({}) Waiting for {} sec' .format(index, time))
        sock.settimeout(time)

        try:
            data, addr = sock.recvfrom(BUFF_SIZE)
        except socket.timeout:  # 기다리는 시간 동안 응답 없음
            time *= 2  # 2배로 증가
            if time > 2.0:  # 최대 2.0
                print('{}th packet is lost' .format(index))
                if index >= sending_counts:
                    break
                index += 1
                time = 0.1
        else:  # 응답 잘 보냄
            print('Server reply: {!r}' .format(data.decode()))
            if index >= sending_counts:
                break
            index += 1
            time = 0.1

if __name__ == '__main__':
    mode = {'c': Client, 's': Server}
    # description : help 치면 나옴
    parser = argparse.ArgumentParser(description='Send and receive UDP packet with setting drop probability')
    # role : 무조건 있어야 함
    parser.add_argument('role', choices=mode, help='which role to tkae between server and client')
    # - : 시작 옵션 >> 엇으면 default
    parser.add_argument('-s', default='localhost', help='server that client sends to')
    parser.add_argument('-p', type=int, default='2500', help='UDP port (default:2500)')
    parser.add_argument('-prob', type=float, default=0, help='dropping probability (0~1)')
    parser.add_argument('-count', type=int, default=10, help='number of sending packets')
    
    args = parser.parse_args()
    prob = args.prob
    sending_counts = args.count

    if args.role =='c':  # client
        mode[args.role](args.s, args.p)
    else:                # server
        mode[args.role]('', args.p)
