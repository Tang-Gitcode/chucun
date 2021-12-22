"""圣诞树"""

#定时执行任务命令
import schedule
import time
import turtle

def fun_timer():
 
    global timer
    # 定义圣诞树的绿叶函数
    def tree(d, s):
        if d <= 0:
            return
        turtle.forward(s)
        tree(d - 1, s * .8)
        turtle.right(120)
        tree(d - 3, s * .5)
        turtle.right(120)
        tree(d - 3, s * .5)
        turtle.right(120)
        turtle.backward(s)
    
    
    
    
    n = 100
    """ 设置绘图速度
    'fastest' :  0
    'fast'    :  10
    'normal'  :  6
    'slow'    :  3
    'slowest' :  1
    """
    turtle.speed('fastest') # 设置速度
    
    
    turtle.left(90)
    turtle.forward(3 * n)
    turtle.color("orange", "yellow")
    turtle.left(126)
    
    
    
    
    # turtle.begin_fill()
    for i in range(5):
        turtle.forward(n / 5)
        turtle.right(144)
        turtle.forward(n / 5)
        turtle.left(72)
        turtle.end_fill()
    turtle.right(126)
    turtle.color("dark green")
    turtle.backward(n * 4.8)
    
    
    # 执行函数
    tree(15, n)
    turtle.backward(n / 5)


    # 窗口保持
    # turtle.done()

schedule.every(10).minutes.do(fun_timer)        # minutes 分钟


while True:
    schedule.run_pending()          # run_pending()执行所有可以执行的任务

