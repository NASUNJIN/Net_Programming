from random import randint

money = 50

while money > 0 and money < 100:
    guess = input('choose 1 or 2: ')
    coin = randint(1, 2)

    if  guess == str(coin):
        print("O")
        money += 9
    else:
        money -= 10
        print("X")
    print(f'money: {money}$')

if money >= 100:
    print("WINNER")
else:
    print("GAMEOVER")