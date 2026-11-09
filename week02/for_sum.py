# 用for循环计算1-100间奇数之和
total = 0
for num1 in range(1, 101):
    if num1 % 2 == 1:
        total += num1
print(f"1-100间的奇数累加之和为{total}")