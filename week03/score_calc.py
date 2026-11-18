def calc_score(score_list):
    """
    计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分
    :param score_list: 分数列表
    :return: 最高分，最低分，平均分
    """
    max_s = max(score_list)
    min_s = min(score_list)
    avg_s = round(sum(score_list) / len(score_list), 1)
    return max_s, min_s, avg_s

# 改成手动输入
# 输入用逗号隔开，例如：589,609,605
input_str = input("请输入成绩，用英文逗号隔开：")
# 分割字符串，转成数字列表
s_list = [int(x) for x in input_str.split(',')]

max_s, min_s, avg_s = calc_score(s_list)
print(f"最高分：{max_s}，最低分：{min_s}，平均分：{avg_s}")