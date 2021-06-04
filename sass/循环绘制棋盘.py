#测试用循环+海龟绘图绘制一个棋盘

#加载海龟绘图模块
import turtle


width = 30
num = 18

#定义x,y轴长度
x1 = [(-300, 300), (-300+width*num, 300)]
y1 = [(-300, 300), (-300, 300-width*num)]

#绘制速度
turtle.speed(10)


#循环绘制线条
for i in range(0, 19):
    # 绘制线条
    turtle.penup()
    turtle.goto(x1[0][0], x1[0][1]-30*i)
    turtle.pendown()
    turtle.goto(x1[1][0], x1[1][1]-30*i)


#箭头向右偏转90°
turtle.right(90)
for i in range(0, 19):
    # 绘制线条
    turtle.penup()
    turtle.goto(y1[0][0]+30*i, y1[0][1])
    turtle.pendown()
    turtle.goto(y1[1][0]+30*i, y1[1][1])


#使箭头消失
turtle.hideturtle()
#窗口保持
turtle.done()