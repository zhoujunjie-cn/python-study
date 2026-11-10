# 输入一个字符串，判断是否是回文对称
word = input("请输入要判断的字符串")
if word == word[::-1]:
    print(f'"{word}"是回文')
else:
    print(f'"{word}"不是回文')

# 将用户输入的10个字符串反转后转换成大写，然后记录在列表中并将内容遍历输出
word = input("请输入10个小写字母：")
s = word[::-1].upper()
print(s)
