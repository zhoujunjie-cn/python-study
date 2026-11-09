# C=(F-32)/1.8 华转摄
# F=C*1.8+32 摄转华
t = input("请输入带单位温度，如25C或77F：")
# 取出字符串最后一个字符作为温度单位
unit = t[-1]
# 截取除最后一位外的所有字符，转为浮点数作为温度数值
n = float(t[:-1])
if unit == "C" or unit == "c":
    F = n * 1.8 + 32
    # 格式化输出，保留两位小数
    print(f"华氏度为{F:.2f}F.")
elif unit == "F" or unit == "f":
    C = (n - 32) / 1.8
    print(f"摄氏度为{C:.2f}C.")
else:
    print("输入格式错误")