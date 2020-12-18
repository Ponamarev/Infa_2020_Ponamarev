from tkinter import Tk, Canvas, Frame, BOTH
import math
from random import *

class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        k = 2*random() + 1

        def trunk(x, y):
            canvas.create_polygon(
                x, y, x-10*k, y + 150*k, x + 10*k, y+150*k,
                fill='brown4', outline='black'
            )

        def leaves(x, y):
            for i in range(200):
                x0 = x - 30*k + randint(1, 60)*k
                y0 = y + randint(1, 90)*k
                r0 = randint(10, 20)*k
                color = ["dark green", "dark olive green",
                         "forest green", "green4", "chartreuse4"]
                canvas.create_oval(
                    x0 - r0, y0 - r0, x0 + r0, y0 + r0,
                    fill=color[randint(0, 4)], outline=color[randint(0, 4)]
                )

        trunk(100, 100)
        leaves(100, 100)

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("500x500+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()