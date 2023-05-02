list = [1, 2, 3]

# 두번째 요소를 17로 수정
list[1] = 17
print(list)

list.append(4)
list.append(5)
list.append(6)

# 첫번째 요소 제거
del list[0]
print(list)

# 리스트를 요소 오름차순으로 정렬
list.sort()
print(list)

#리스트 요소 내림차순으로 정렬
list.sort(reverse=True)
print(list)

# 인덱스 3에 25 넣기
list[3] = 25
print(list)