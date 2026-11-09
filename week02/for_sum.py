# 用for循环计算1-100之间奇数之和
total = 0
for i in range(1, 101):
    if i % 2 == 1:
        total += i
print(f"1-100间的奇数累加之和为{total}")

# 简化
total = 0
for i in range(1, 101, 2):
        total += i
print(f"1-100间的奇数累加之和为{total}")

# 用for循环计算100-500间3的倍数之和
total = 0
for i in range(100, 501):
    if i % 3 == 0:
        total += i
print(f"1-100间的奇数累加之和为{total}")