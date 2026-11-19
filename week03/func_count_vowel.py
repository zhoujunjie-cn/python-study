# 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
def count_aeiou(s):
    """
    统计字符串中元音字母的个数
    :param s: 字符串
    :return: 元音字母的个数
    """
    num = 0
    for w in s:
        if w in "aeiouAEIOU":
            num += 1
    return num

print(count_aeiou("Hello Python Hello World OK"))