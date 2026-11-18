# 案例3：定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分(保留1位小数)，并返回。
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

s_list = [589, 609, 605, 643, 677, 455, 477, 489, 503]
# 调用函数，接收返回的三个结果
max_s, min_s, avg_s = calc_score(s_list)

# 打印看看结果
print("最高分：", max_s)
print("最低分：", min_s)
print("平均分：", avg_s)