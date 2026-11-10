# num_list1 = [1,2,3,4,5]
# num_list2 = [3,4,5,6,7,8]
# for num in num_list2:
#     num_list1.append(num)
# # 解包(将列表这一类容器解包成一个个独立的元素) num_list=[*num_list1,*num_list2]
# # 组包(将多个值合并到一个容器)
# # num_list = num_list1+num_list2
# print(num_list1)
# new_list = []
# for num in num_list1:
#     if num not in new_list:
#         new_list.append(num)
# print(new_list)

# 生成 1-20 的平方列表
num_list = []
for i in range(1, 21):
    num_list.append(i**2)
print(num_list)

# 列表推导式 按照一定规则快速生成一个列表，语法格式[要插入的值for i in 序列/列表]
# [要插入的值for i in 序列/列表 if 条件]
num_list2 = [i**2 for i in range(1, 21)]
print(num_list2)

# 从一个数字列表中提取所有偶数，计算其平方组成一个新列表
num_list3 = [1,2,3,4,5,6,7,8]
new_list = [i**2 for i in num_list3 if i%2==0]
print(new_list)