# 用while循环计算1-100间所有偶数的和

# 记录累加之和
total = 0
# 循环开始数字从1开始
i = 1
# 循环数字到100
while i <= 100:
    # 若循环的数字取余2=0为偶数
    if i % 2 == 0:
        # 偶数累加
        total = total + i
    i = i + 1
print(f"累加之和为{total}")