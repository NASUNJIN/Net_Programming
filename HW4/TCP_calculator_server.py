from socket import *

s = socket(AF_INET, SOCK_STREAM)
s.bind(('', 9999))
s.listen(3)
print('waiting...')

while True:
    client, addr = s.accept()
    print('connection from', addr)
    while True:
        data = client.recv(1024)  # bytes객체로 식 받음

        if not data:
            break

        data_str = data.decode()       # 문자열로 변경
        space = data_str.replace(" ", "")  # 공백이 있을 시 없앰

        # 계산
        if (space.find('+') != -1):
            cal = space.split('+')
            cal[0] = int(cal[0])
            cal[1] = int(cal[1])
            result = cal[0] + cal[1]
        elif (space.find('-') != -1):
            cal = space.split('-')
            cal[0] = int(cal[0])
            cal[1] = int(cal[1])
            result = cal[0] - cal[1]
        elif (space.find('*') != -1):
            cal = space.split('*')
            cal[0] = int(cal[0])
            cal[1] = int(cal[1])
            result = cal[0] * cal[1]
        elif (space.find('/') != -1):
            cal = space.split('/')
            cal[0] = float(cal[0])
            cal[1] = float(cal[1])
            result = round(cal[0] / cal[1], 1)
        else :
            print("error")     

        result_str = str(result)

        client.send(result_str.encode())

    client.close()