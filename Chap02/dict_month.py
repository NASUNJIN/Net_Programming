# days = {'January':31, 'February':28, 'March':31, 'April':30,
#         'May':31, 'June':30, 'July':31, 'August':31,
#         'September':30, 'October':31, 'November':30,'December':31}

# month = input("Enter a month: ")
# # 해당 월의 일수 출력
# if month in days:
#     print(f"The number of days in {month} is {days[month]}.")
# else:
#     print("Invalid month.")

# # 알파벳 순서로 모든 월 출력
# for month in sorted(days):
#     print(month)

# # 일수가 31일 월 모두 출력
# for month in days:
#     if days[month] == 31:
#         print(month)

# # 월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력하라
# for month, day in sorted(days.items(), key=lambda x: x[1]):
#     print(f"{month}: {day}")
    
# # 사용자가 월을 3자리만 입력하면 월의 일수를 출력하라 (Jan, Feb 등)
# month = input("Enter a month (3-letter abbreviation): ").capitalize()[:3]
# for m, d in days.items():
#     if m[:3] == month:
#         print(f"{m} has {d} days.")
#         break
# else:
#     print("Invalid month.")

days = {'January':31, 'February':28, 'March':31, 'April':30,
        'May':31, 'June':30, 'July':31, 'August':31,
        'September':30, 'October':31, 'November':30,
        'December':31}

# 사용자가 월을 입력하면 해당 월에 일수를 출력
month = input("Enter a month: ")
print(f"{month} has {days.get(month.capitalize(), 'invalid month')} days")

# 알파벳 순서로 모든 월을 출력
print(sorted(days.keys()))

# 일수가 31인 월을 모두 출력
print([month for month, days in days.items() if days == 31])

# 월의 일수를 기준으로 오름차순으로 (key-value) 쌍을 출력
print(sorted(days.items(), key=lambda x: x[1]))

# 사용자가 월을 3자리만 입력하면 월의 일수를 출력
month_abbrev = input("Enter a month abbreviation (e.g. Jan, Feb): ")
month_full = {k[:3]: v for k, v in days.items()}
print(f"{month_abbrev} has {month_full.get(month_abbrev.capitalize(), 'invalid month abbreviation')} days")
