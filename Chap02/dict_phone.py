d = [
    {'name':'Todd', 'phone':'555-1414', 'email':'todd@mail.net'},
    {'name':'Helga', 'phone':'555-1618', 'email':'helga@mail.net'},
    {'name':'Princess', 'phone':'555-3141', 'email':''},
    {'name':'LJ', 'phone':'555-2718', 'email':'lj@mail.net'}
]

# 전화번호가 8로 끝나는 사용자 이름 출력
print("전화번호가 8로 끝나는 사용자 이름:")
for user in d:
    # .endswith(): 문자열이 특정 문자열로 끝나는지 여부를 확인하는 파이썬 문자열 메소드
    if user['phone'].endswith('8'):
        print(user['name'])

# 이메일이 없는 사용자 이름 출력
print("\n이메일이 없는 사용자 이름:")
for user in d:
    if not user['email']:
        print(user['name'])

# 사용자 이름으로 전화번호와 이메일 출력
name = input("\n사용자 이름 입력: ")
for user in d:
    if user['name'] == name:
        print("전화번호:", user['phone'])
        print("이메일:", user['email'] or '이메일이 없습니다.')
        break
else:
    print("해당하는 이름이 없습니다.")
