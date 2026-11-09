# C=(F-32)*1.8 华转摄
# F=C*1.8+32 摄转华
t = input("请输入带单位温度，如25C或77F：")
unit = t[-1]
n = float(t[:-1])
if unit == "C":
    F = n * 1.8 + 32
    print(f"华氏度为{F:.2f}F.")
elif unit == "F":
    C = (n - 32) * 1.8
    print(f"摄氏度为{C:.2f}C.")
else:
    print("输入格式错误")