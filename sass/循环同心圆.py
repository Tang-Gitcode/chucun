#练习用海龟绘图运用循环绘制同心圆


#导入海龟绘图模块
import turtle

#画笔颜色
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black", "white", "pink"]
#画笔宽度
turtle.width("8")
#画笔速度
turtle.speed(1)

for i in range(1):
    turtle.pencolor(colors[ i % 9])  #画笔颜色持续变化
    turtle.circle(25+i*50)  # 画指定半径的圆
    turtle.penup()    # 抬笔
    turtle.goto(0, -(i*50+50))  #光标移动到指定坐标
    turtle.pendown()    #落笔

#光标消失
turtle.hideturtle()
#窗口保持
turtle.done()
