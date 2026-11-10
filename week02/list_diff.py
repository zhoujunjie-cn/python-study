# 给定两个列表 A、B，输出只在 A 里出现、只在 B 里出现、两边都出现的三个结果
A = [1, 2, 3, 4, 5]
B = [3, 4, 5, 6, 7]
C = [num for num in A if num not in B]
print("只在A：",C)
D = [num for num in B if num not in A]
print("只在B：",D)
E = [num for num in A if num in B]
print("两边都有：",E)