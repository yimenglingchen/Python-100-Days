# 输入圆的半径计算计算周长和面积

radius = float(input("请输入圆的半径："))
pai = 3.14159
perimeter = radius * pai * 2
area = radius * radius * pai
print(f'圆的周长：{perimeter:.2f},圆的面积：{area:.2f}')