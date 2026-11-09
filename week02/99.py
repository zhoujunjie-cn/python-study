# print("*")：自带换行效果
# print("*",end="")end表示每一次输出以什么表示结束，默认\n
# m,n 长方形
m = int(input("长"))
n = int(input("宽"))
for i in range(n):
    for x in range(m):
        print("*", end="")
    print()