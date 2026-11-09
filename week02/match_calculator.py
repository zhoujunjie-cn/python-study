# 练习：使用match-case实现简易四则运算
# 功能：根据输入计算两个数的加减乘除
num1=int(input("请输入第一个数："))
x=input("请输入运算符（+ - * /）：")
num2=int(input("请输入第二个数："))
match x:
    case "+" :
        print(f"{num1} + {num2} =",num1+num2)
    case "-" :
        print(f"{num1} - {num2} =",num1-num2)
    case "*" :
        print(f"{num1} * {num2} =",num1*num2)
    case "/" :
        print(f"{num1} / {num2} =",num1/num2)
    case _:
        print("操作不支持")