from tkinter import *

class BowlingWindow:
    def __init__(self, win):
        self.lbl1 = Label(win, text='First Game')
        self.lbl2 = Label(win, text='Second Game')
        self.lbl3 = Label(win, text='Third Game')
        self.lbl4 = Label(win, text='Series')
        self.lbl5 = Label(win, text='Average')
        self.t1 = Entry()
        self.t2 = Entry()
        self.t3 = Entry()
        self.t4 = Entry()
        self.t5 = Entry()
        self.lbl1.place(x=75, y=50)
        self.t1.place(x=175, y=50)
        self.lbl2.place(x=75, y=80)
        self.t2.place(x=175, y=80)
        self.lbl3.place(x=75, y=110)
        self.t3.place(x=175, y=110)
        self.lbl4.place(x=75, y=180)
        self.t4.place(x=175, y=180)
        self.lbl5.place(x=75, y=210)
        self.t5.place(x=175, y=210)
        self.b1 = Button(win, text='Compute', command=self.compute_button)
        self.b1.place(x=175, y=150)

    def compute_button(self):
        self.t4.delete(0, 'end')
        self.t5.delete(0, 'end')
        num1 = int(self.t1.get())
        num2 = int(self.t2.get())
        num3 = int(self.t3.get())
        result, average = self.calculate(num1, num2, num3)
        self.t4.insert(END, str(result))
        self.t5.insert(END, str(int(average)))

    def calculate(self, num1, num2, num3):
        a = num1+num2+num3
        b = (num1 + num2 + num3)/3
        return a, b

window = Tk()
mywin = BowlingWindow(window)
window.title('Bowling Calculator')
window.geometry("450x300+10+10")
window.mainloop()
