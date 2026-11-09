import random

random_num = random.randint(1, 100)
while True:
    n = int(input("请输入一个数字"))
    if n > random_num:
        print("猜大了")
    elif n < random_num:
        print("猜小了")
    else:
        print("猜对啦")
        break
print(f"随机生成的数是{random_num}")
