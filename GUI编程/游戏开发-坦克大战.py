"""坦克大战的开发"""


from tkinter import *


class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master)            # super()代表的是父类的定义而不是父类对象
        self.master = master
        self.pack()
        self.createWidget()


if __name__ == "__main__":
    root = Tk()
    root.title("记事本")
    root.geometry("400x300+200+300")
    app = Application(master=root)
    root.mainloop()
