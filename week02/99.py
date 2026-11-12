# 99乘法表，嵌套循环
# 第一个数是列，第二个数是行，外层循环控制行，第二个数
for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}x{i}={j * i}", end="\t")
    print()