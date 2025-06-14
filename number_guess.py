import random

number = random.randint(1, 100)
guess = -1
while guess != number:
    guess = int(input("猜一個 1~100 的數字："))
    if guess > number:
        print("太大了！")
    elif guess < number:
        print("太小了！")
    else:
        print("恭喜猜對了！")