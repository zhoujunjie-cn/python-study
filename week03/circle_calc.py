# 输入半径计算圆的面积和周长
def circle_area_len(r):
    return round(3.14*r**2,1),round(2*3.14*r,1) # 面积，周长
r=float(input("请输入圆的半径:"))
area,perimeter = circle_area_len(r)
print(f"半径为{r}的圆的面积为:{area},周长为:{perimeter}")