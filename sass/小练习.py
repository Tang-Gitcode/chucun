import turtle  # 导入海龟绘图模块


def draw_rect(num):
    for i in range(1, num + 1):
        turtle.left(5)
        turtle.width(3)  # 画笔粗细
        turtle.color("orange")  # 画笔颜色为橙色
        turtle.forward(200)  # 画一条200像素的线
        turtle.right(90)  # 顺时针旋转90°
        turtle.color("red")  # 画笔颜色为红色
        turtle.forward(100)  # 画一条100像素的线
        turtle.right(90)  # 顺时针旋转90°
        turtle.color("green")  # 画笔颜色为绿色
        turtle.forward(200)  # 画一条200像素的线
        turtle.right(90)  # 顺时针旋转90°
        turtle.color("purple")  # 画笔颜色为紫色
        turtle.forward(100)  # 画一条100像素的线

turtle.speed(0) #速度
turtle.ht()  # 隐藏海龟光标可以提升速度
draw_rect(100)
turtle.done()  # 海龟绘图程序的结束语句（开始主循环）