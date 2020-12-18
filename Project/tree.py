from tkinter import Tk, Canvas, Frame, BOTH
import math
from random import *


class Tree():
    def __init__(self, canv):
        self.canv = canv
        self.size = 2 * randrange(100, 200, 1) / 100 + 1

    def draw(self):
        self.trunk(100, 100)
        self.leaves(100, 100)

    def trunk(self, x, y):
        self.canv.create_polygon(
            x, y, x - 10 * self.size, y + 150 * self.size, x + 10 * self.size, y + 150 * self.size,
            fill='brown4', outline='black'
        )

    def leaves(self, x, y):
        for i in range(200):
            x0 = x - 30 * self.size + randint(1, 60) * self.size
            y0 = y + randint(1, 90) * self.size
            r0 = randint(10, 20) * self.size
            color = ["dark green", "dark olive green",
                     "forest green", "green4", "chartreuse4"]
            self.canv.create_oval(
                x0 - r0, y0 - r0, x0 + r0, y0 + r0,
                fill=color[randint(0, 4)], outline=color[randint(0, 4)]
            )


def main():
    root = Tk()
    ex = Example()
    root.geometry("500x500+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()
