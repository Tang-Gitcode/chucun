"""测试Radiobutton组件的基本用法，使用面向对象的方式"""

from tkinter import *
from tkinter import messagebox


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)            # super()代表的是父类的定义而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()

    def createWidget(self):
        """创建登录界面的组件"""
        self.lable01 = Label(self, text="用户名")
        self.lable01.pack()

        # StringVar变量绑定到指定的组件
        # StringVar变量发生变化，组件内容也变化
        # 组件内容发生变化，StringVar的值也发生变化
        v1 = StringVar()
        self.entry01 = Entry(self, textvariable=v1)
        self.entry01.pack()
        print(v1.set("admin"))
        print(self.entry01.get())

        # 添加密码框组件
        self.lable02 = Label(self, text="密码")
        self.lable02.pack()

        v2 = StringVar()
        self.entry02 = Entry(self, textvariable=v2)
        self.entry02.pack()

        Button(self, text="登录", command=self.login).pack()

    def login(self):
        messagebox.showinfo("尚学堂学习系统", "登录成功！欢迎开始学习")


if __name__ == "__main__":
    root = Tk()
    root.title("登录")
    root.geometry("400x130+200+300")
    app = Application(master=root)
    root.mainloop()



