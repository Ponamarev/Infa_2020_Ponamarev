from tkinter import Tk, Canvas, Frame, BOTH
import math


class Example(Frame):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)

        def wall(x, y, k):
            canvas.create_rectangle(
                x - 60*k, y + 30*k, x + 60*k, y + 150*k,
                fill='saddle brown', outline='black'
            )
            for i in range(30, 150, 10):
                canvas.create_line(
                    x - 60 * k, y + i * k, x + 60 * k, y + i * k,
                )

        def roof(x, y, k):
            canvas.create_polygon(
                x, y, x + 65*k, y + 30*k,
                x - 65*k, y + 30*k,
                fill='firebrick1', outline='black'
            )
            canvas.create_oval(
                x - 8*k, y + 7*k, x + 8*k, y + 23*k,
                fill='grey', outline='black'
            )
            canvas.create_oval(
                x - 6 * k, y + 9 * k, x + 6 * k, y + 21 * k,
                fill='light blue', outline='black'
            )

        def window(x, y, k):
            canvas.create_rectangle(
                x - 20*k, y + 70*k, x + 20*k, y + 110*k,
                fill='grey', outline='black'
            )
            canvas.create_rectangle(
                x - 16 * k, y + 74 * k, x - 2 * k, y + 88 * k,
                fill='light blue', outline='black'
            )
            canvas.create_rectangle(
                x - 16 * k, y + 92 * k, x - 2 * k, y + 106 * k,
                fill='light blue', outline='black'
            )
            canvas.create_rectangle(
                x + 2 * k, y + 74 * k, x + 16 * k, y + 88 * k,
                fill='light blue', outline='black'
            )
            canvas.create_rectangle(
                x + 2 * k, y + 92 * k, x + 16* k, y + 106 * k,
                fill='light blue', outline='black'
            )

        wall(150, 100, 2)
        window(150, 100, 2)
        roof(150, 100, 2)

        canvas.pack(fill=BOTH, expand=1)


def main():
    root = Tk()
    ex = Example()
    root.geometry("500x500+300+300")
    root.mainloop()


if __name__ == '__main__':
    main()