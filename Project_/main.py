import tkinter
from datetime import datetime
import menu
import graphic


FPS = 40
wight_of_screen = 1280
height_of_screen = 720

root = tkinter.Tk()
root.geometry('{}x{}'.format(str(wight_of_screen), str(height_of_screen)))
root.resizable(False, False)
root.title("BEA")
root.config(cursor="none")
canv = tkinter.Canvas(
    width=wight_of_screen,
    height=height_of_screen,
    bg='green',
    highlightthickness=0
)
canv.pack()
ag = graphic.Aggregator()
ag.canv = canv
menu = menu.Menu(canv, root, wight_of_screen, height_of_screen)
t = datetime.now()
menu.time = t


def update():
    """
    updating game state and redrawing screen
    """
    dt = (datetime.now() - menu.time)
    dt = dt.microseconds / 1000
    menu.time = datetime.now()
    graphic.rubbing()
    menu.update(dt)
    dt -= FPS
    if dt < 0:
        dt = 0

    root.after(int(dt) + 1, update)


update()
root.mainloop()
