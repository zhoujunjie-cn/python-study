# 输入半径计算圆的面积和周长
def circle_area_len(r):
    return 3.14*r**2,2*3.14*r # 面积，周长
r=float(input("请输入圆的半径:"))
ex = circle_area_len(r)
print(f"半径为{r}的圆的面积和周长为:{ex}")