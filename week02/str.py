# 输入一个字符串，判断是否是回文（）对称
word = str(input("请输入字符串"))
if word[::1]==word[::-1]:
    print(f'"{word}"是回文')
else:
    print(f'"{word}"不是回文')