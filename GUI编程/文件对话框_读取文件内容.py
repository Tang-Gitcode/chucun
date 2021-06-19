"""文件对话框获取文件"""

from tkinter import *
from tkinter.filedialog import *

root = Tk()
root.geometry("400x100")


def test1():
    d = askopenfilename(title="上传文件", initialdir="d:", filetypes=[("视频文件", ".mp4")])

    show["text"] = d


Button(root, text="选择编辑的视频文件", command=test1).pack()
 
show = Label(root, width=10, height=3, bg="green")
show.pack()


root.title("选择文件")
root.mainloop()


