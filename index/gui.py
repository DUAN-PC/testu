
import tkinter,time
w,we,top,r,ay,by=(None,)*6
def run():
    global w,we,top,ay,by
    top = tkinter.Tk()
    top.geometry("900x200")
    stre=tkinter.StringVar()
    text1=tkinter.Label(text="请输入题目的个数")
    text1.place(x=100,y=10)
    w=tkinter.Entry(top,bg="#0f9b7a",width=45,textvariable=stre.set("请输入要生成多少道算术题"))
    w.place(x=300,y=10)
    text2=tkinter.Label(text="请输入数字的范围是多少以内")
    text2.place(x=100,y=50)
    we=tkinter.Entry(top,bg="#0f9b7a",width=45)
    we.place(x=300,y=50)
    def next():
        global w,we,top,r,ay,by
        try:
            e=int(w.get())
            e=int(we.get())
        except:
            top.destroy()
            exit(0)
        ay=w.get()
        by=we.get()
        r=tkinter.Toplevel(top)
        text2=tkinter.Label(r,text="提交成功")
        text2.pack()
        def exr():
            global r,top
            r.destroy()
            top.destroy()
        r.after(5*1000,exr)
        r.mainloop()
        
    b=tkinter.Button(top,height=2,width=5,text="确定",command=next)
    b.place(x=300+140,y=90)
    top.mainloop()
    return [int(ay),int(by)];