import tkinter
from settings import *
import math


class House(PassiveObject):
    def __init__(self, canvas, tag, coords):
        super().__init__(canvas, tag, coords)
        self.canv = canvas
        self.wall_obj = self.canv.create_rectangle(0, 0, 0, 0, fill='saddle brown', outline='black')
        self.lines_of_walls_endings = []
        for i in range(30, 150, 10):
            self.lines_of_walls_endings.append(self.canv.create_line(0, 0, 0, 0))
        self.roof_endings = self.canv.create_polygon(0, 0, 0, 0, fill='firebrick1', outline='black')
        self.roofs_window_endings = self.canv.create_oval(0, 0, 0, 0, fill='grey', outline='black')
        self.roofs_window = self.canv.create_oval(0, 0, 0, 0, fill='light blue', outline='black')
        self.house_window = self.canv.create_rectangle(0, 0, 0, 0, fill='grey', outline='black')
        self.window_endings = []
        for i in range(4):
            self.window_endings.append(self.canv.create_rectangle(0, 0, 0, 0, fill='light blue', outline='black'))
        self.draw()

    def draw(self):

        self.wall(150, 100, 2)
        self.window(150, 100, 2)
        self.roof(150, 100, 2)

    def wall(self, x, y, k):
        self.canv.coords(self.wall_obj,
                      x - 60 * k, y + 30 * k, x + 60 * k, y + 150 * k
                      )
        for i in range(30, 150, 10):
            self.canv.coords(self.lines_of_walls_endings[i // 10 - 3],
                          x - 60 * k, y + i * k, x + 60 * k, y + i * k,
                          )

    def roof(self, x, y, k):
        self.canv.coords(self.roof_endings,
            x, y, x + 65 * k, y + 30 * k,
                  x - 65 * k, y + 30 * k,
        )
        self.canv.coords(self.roofs_window_endings,
            x - 8 * k, y + 7 * k, x + 8 * k, y + 23 * k,
        )
        self.canv.coords(self.roofs_window,
            x - 6 * k, y + 9 * k, x + 6 * k, y + 21 * k,
        )

    def window(self, x, y, k):
        self.canv.coords(self.house_window,
            x - 20 * k, y + 70 * k, x + 20 * k, y + 110 * k,
        )
        self.canv.coords(self.window_endings[0],
            x - 16 * k, y + 74 * k, x - 2 * k, y + 88 * k,
        )
        self.canv.coords(self.window_endings[1],
            x - 16 * k, y + 92 * k, x - 2 * k, y + 106 * k,
        )
        self.canv.coords(self.window_endings[2],
            x + 2 * k, y + 74 * k, x + 16 * k, y + 88 * k,
        )
        self.canv.coords(self.window_endings[3],
            x + 2 * k, y + 92 * k, x + 16 * k, y + 106 * k,
        )


def main():
    root = tkinter.Tk()
    canv = tkinter.Canvas(
        width=wight_of_screen,
        height=height_of_screen,
        bg='green',
        highlightthickness=0
    )
    canv.pack()
    ex = House(canv)
    root.geometry("500x500+300+300")
    ex.draw()
    root.mainloop()


if __name__ == '__main__':
    main()
