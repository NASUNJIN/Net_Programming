total_sum = 0

# 1부터 1000까지
for num in range(1, 1001):
    str_num = str(num)
    # digit : 0 ~ 9 사이의 숫자
    digit_sum = 0

    for digit in str_num:
        digit_sum += int(digit)
    total_sum  += digit_sum

print(total_sum)