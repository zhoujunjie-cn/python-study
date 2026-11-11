# 1.计算每个学生的总分，各科平均分，一并输出
# 2.统计各科成绩的最低分，最高分，平均分，并输出
# 3.查找成绩优秀（平均分大于90）的学生，并输出
students = (
    ("S001","王林",85,92,78),
    ("S002","李慕婉",92,88,95),
    ("S003","十三",78,85,82),
    ("S004","曾牛",88,79,91),
    ("S005","周铁",95,96,89),
    ("S006","王卓",76,82,77),
    ("S007","红蝶",89,91,94),
    ("S008","徐立国",75,69,82),
    ("S009","许木",86,89,98),
    ("S010","通天",66,59,72)
)
# 1. 计算每个学生的总分、各科平均分，然后一并输出出来
print("学号\t\t姓名\t\t总分\t\t平均分")
# 方式一：
# for s in students:
#     n = s[2]+s[3]+s[4] # 总分
#     avg = n/3 # 平均分
#     print(f"{s[0]} \t {s[1]} \t {n} \t {avg:.1f}")
# 方式二：元组解包
for id,name,chinese,math,english in students:
    n = chinese+math+english # 总分
    avg = n/3 # 平均分
    print(f"{id} \t {name} \t {n} \t {avg:.1f}")

# 2.统计各科成绩的最低分，最高分，平均分，并输出
# 2.1获取各科成绩列表
chinese_score = [s[2] for s in students]
math_score = [s[3] for s in students]
english_score = [s[4] for s in students]
# 2.2统计各科成绩最低分，最高分，平均分
print(f"语文最低分{min(chinese_score)},最高分{max(chinese_score)},平均分{sum(chinese_score)/len(chinese_score)}")
print(f"数学最低分{min(math_score)},最高分{max(math_score)},平均分{sum(math_score)/len(math_score)}")
print(f"英语最低分{min(english_score)},最高分{max(english_score)},平均分{sum(english_score)/len(english_score)}")

# 3.查找成绩优秀（平均分大于90）的学生，并输出
# 方式一：
# for s in students:
#     n = s[2] + s[3] + s[4]  # 总分
#     avg = n / 3
#     if avg > 90:
#         print(f"学号{s[0]},名字{s[1]},平均分为{avg:.1f}")
# 方式二：元组解包
for id,name,chinese,math,english in students:
    n = chinese + math + english  # 总分
    avg = n / 3
    if avg > 90:
        print(f"学号{id},名字{name},平均分为{avg:.1f}")