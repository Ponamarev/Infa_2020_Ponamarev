import tkinter
import math


class Aggregator(object):
    canv = None
    figures = []
    old_figures = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Aggregator, cls).__new__(cls)
        return cls.instance

    def add(self, figure):
        self.figures += [figure]

    def __init__(self):
        pass
        

def rubbing():
    ag = Aggregator()
    
    for fig in ag.old_figures:
        ag.canv.delete(fig)
    
    ag.old_figures = ag.figures
    ag.figures = []
    
    
def draw_start_page(current_line, timers):
    back1 = hex(int(math.sin(timers[1] * math.pi / 5000) * 32 + 0xA0))
    back2 = hex(int(math.cos(timers[1] * math.pi * 3 / 5000) * 50 + 80))
    head0 = int(20 * math.cos(timers[1] * math.pi / 2500))
    head1 = hex(int(math.sin(timers[1] * math.pi * 4 / 5000) * 32 + 0xC0))
    head2 = hex(int(math.cos(timers[1] * math.pi * 6 / 5000) * 50 + 0x90))
    awesome_not_grey = "#" + head1[2] + head1[3] + head2[2] + head2[3] + "80"
    awesome_grey = "#" + back1[2] + back1[3] + back2[2] + back2[3] + "60"
    ag = Aggregator()
    canv = ag.canv
    c = ["#8080FF"] * 4
    c[current_line] = "#FF30FF"
    ag.add(
        canv.create_rectangle(
            (0, 0, 1280, 720),
            fill=awesome_grey
        )
    )
    ag.add(
        canv.create_text(
            550 - head0,
            100, text="B",
            justify=tkinter.CENTER,
            font="Impact 100",
            fill=awesome_not_grey
        )
    )
    ag.add(
        canv.create_text(
            640,
            100,
            text="E",
            justify=tkinter.CENTER,
            font="Impact 100",
            fill=awesome_not_grey
        )
    )
    ag.add(
        canv.create_text(
            730 + head0,
            100,
            text="A",
            justify=tkinter.CENTER,
            font="Impact 100",
            fill=awesome_not_grey
        )
    )
    ag.add(
        canv.create_text(
            640,
            300,
            text="Новая игра",
            justify=tkinter.CENTER,
            font="Impact 40",
            fill=c[0]
        )
    )
    ag.add(
        canv.create_text(
            640,
            350,
            text="Загрузить игру",
            justify=tkinter.CENTER,
            font="Impact 40",
            fill=c[1]
        )
    )
    ag.add(
        canv.create_text(
            640,
            400,
            text="Настройки",
            justify=tkinter.CENTER,
            font="Impact 40",
            fill=c[2]
        )
    )
    ag.add(
        canv.create_text(
            640,
            450,
            text="Выход",
            justify=tkinter.CENTER,
            font="Impact 40",
            fill=c[3]
        )
    )
    if timers[0] > 0:
        ag.add(
            canv.create_text(
                200,
                70,
                text="Прикол пока не реализован  :<",
                justify=tkinter.CENTER,
                font="Impact 16",
                fill="#FF2060"
            )
        )


def draw_pause_page(current_line):
    ag = Aggregator()
    canv = ag.canv
    c = ["#8080FF"] * 4
    c[current_line] = "#FF30FF"
    ag.add(
        canv.create_rectangle(
            (0, 0, 1280, 720),
            fill="#FFE4E1"
        )
    )
    ag.add(
        canv.create_text(
            650,
            100, text="Пауза",
            justify=tkinter.CENTER,
            font="Impact 100",
            fill="#BC8F8F"
        )
    )
    ag.add(
        canv.create_text(
            640,
            300,
            text="Вернуться",
            justify=tkinter.CENTER,
            font="Impact 40",
            fill=c[0]
        )
    )
    ag.add(
        canv.create_text(
            640,
            350,
            text="Сохранение",
            justify=tkinter.CENTER,
            font="Impact 40",
            fill=c[1]
        )
    )
    ag.add(
        canv.create_text(
            640,
            400,
            text="Выход",
            justify=tkinter.CENTER,
            font="Impact 40",
            fill=c[2]
        )
    )
