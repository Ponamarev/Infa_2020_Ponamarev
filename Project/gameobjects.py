import tkinter
import math
import Models.graphic_human
import Models.tree
from settings import *


# abstract class (using in this module only)
class ActiveObject(object):
    def __init__(self, canvas, tag, coords):
        """
        Это конструктор класса живых объектов.
        :param canvas: Окно, на котором рисуется игра.
        :param tag: Тэг к которому присваевается живой обьект.
        :param coords: Координаты объекта [x, y].
        """
        self.canv = canvas
        self.tag = tag
        self.coords = coords
        self.hit_box = None
        self.damage_hitbox = None
        self.health_points = 100
        self.damage = None
        self.exp_plus = None

    def update(self):
        return self

    def image_self(self):
        pass


class PassiveObject(object):
    def __init__(self, canvas, tag, coords):
        """
        Это конструктор класса живых объектов.
        :param canvas: Окно, на котором рисуется игра.
        :param tag: Тэг к которому присваевается живой обьект.
        :param coords: Координаты объекта [x, y].
        """
        self.canv = canvas
        self.tag = tag
        self.coords = coords
        self.damage_hitbox = None
        self.health_points = 100
        self.exp_plus = None
        self.x = coords[0]
        self.y = coords[1]

    def update(self):
        return self

    def image_self(self):
        """
        Рисует обьект.
        :return: None
        """
        pass


class Player(ActiveObject):
    def __init__(self, canvas, root, coords=[150, 150], tag="player"):
        """
        Это конструктор класса игрока.
        :param canvas: Холст, на котором рисуется игрок.
        :param root: Окно, на котором рисуется игра.
        :param coords: координаты опроной точки.
        :param tag: тэг для обрщения.
        """
        super().__init__(canvas, tag, coords)
        self.speed = 5
        self.health_points = 100
        self.experience_points = 0
        self.controlers_but = ['w', 'a', 's', 'd', 'ц', 'ф', 'ы', 'в']
        self.dict_controlers_but = {'w': (0, -1), 'a': (-1, 0),
                                    's': (0, 1), 'd': (1, 0),
                                    'ц': (0, -1), 'ф': (-1, 0),
                                    'ы': (0, 1), 'в': (1, 0)}
        self.interaction_but = ['t', 'f', 'е', 'а']
        self.dict_interaction_but = {'w': (0, -1), 'a': (-1, 0),
                                    's': (0, 1), 'd': (1, 0),
                                    'ц': (0, -1), 'ф': (-1, 0),
                                    'ы': (0, 1), 'в': (1, 0)}
        self.root = root
        self.pressed_but = None
        # [delta_x, delta_y, attack, interaction]
        deltas = [0, 0, False, False]
        self.is_move = False
        self.x = self.coords[0]
        self.y = self.coords[1]
        self.current_mode = 0
        self.id = Models.graphic_human.PlayerImage(root, canvas)
        self.root.bind('<KeyPress-space>', self.pressing)
        self.ent = tkinter.Entry(self.root)
        self.ent.bind_all('<KeyPress>', self.pressing)
        self.ent.bind_all('<KeyRelease>', self.unpressing)
        self.ent.focus_set()

    def pressing(self, event=tkinter.NONE):
        """
        Обрабатывает нажатие клавиш.
        :param event: События Tkinter.
        :return: None
        """
        if event.char in self.controlers_but:
            self.pressed_but = event.char
            if not self.is_move:
                self.step()

    def unpressing(self, event=tkinter.NONE):
        """
        Обрабатывает отжатие кнопки.
        :param event: События Tkinter.
        :return: None
        """
        if self.pressed_but in self.controlers_but:
            self.is_move = False
        self.pressed_but = None

    def step(self, event=tkinter.NONE):
        """
        Обрабатывает перемещения игрока.
        :param event: События Tkinter.
        :return: None
        """
        if self.pressed_but in self.controlers_but:
            self.is_move = True
            self.id.animate_on = 1
            way = self.dict_controlers_but.get(self.pressed_but)
            self.x += self.speed * way[0]
            self.y += self.speed * way[1]
            self.root.after(100, self.step)
        self.image_self()

    def attack(self):
        """
        Ответчает за атаку.
        :return:  None
        """
        pass

    def image_self(self):
        """
        Рисует игрока.
        :return:  None
        """
        self.id.x, self.id.y = self.x, self.y
        self.id.animate_move()


class House(PassiveObject):
    def __init__(self, canvas, tag, coords):
        """
        Это класс дома.
        :param canvas: Холст, на котором рисуется игра.
        :param coords: координаты опроной точки.
        :param tag: тэг для обрщения.
        """
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

    def image_self(self):
        """
        Рисует обьект.
        :return: None
        """
        self.wall(self.x, self.y, player_size / 1.5)
        self.window(self.x, self.y, player_size / 1.5)
        self.roof(self.x, self.y, player_size / 1.5)

    def wall(self, x, y, k):
        """
        Обновляет координаты объектов.
        :param x и y: новая опорная точка.
        :param k: Коэфицент расширения.
        :return:  None
        """
        self.canv.coords(self.wall_obj,
                      x - 60 * k, y + 30 * k, x + 60 * k, y + 150 * k
                      )
        for i in range(30, 150, 10):
            self.canv.coords(self.lines_of_walls_endings[i // 10 - 3],
                          x - 60 * k, y + i * k, x + 60 * k, y + i * k,
                          )

    def roof(self, x, y, k):
        """
        Обновляет координаты объектов.
        :param x и y: новая опорная точка.
        :param k: Коэфицент расширения.
        :return:  None
        """
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
        """
        Обновляет координаты объектов.
        :param x и y: новая опорная точка.
        :param k: Коэфицент расширения.
        :return:  None
        """
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


class Enemy(ActiveObject):
    def __init__(self, canvas, coords=[50, 50], tag="enemy"):
        super().__init__(canvas, tag, coords)


def __test__():
    root = tkinter.Tk()
    canv = tkinter.Canvas(
        width=wight_of_screen,
        height=height_of_screen,
        bg='green4',
        highlightthickness=0
    )
    canv.pack()
    ex = Player(canv, root, coords=[150, 150])
    root.geometry("500x500+300+300")
    ex.image_self()
    ex1 = House(canv, root, coords=[330, 80])
    ex1.image_self()
    root.mainloop()


if __name__ == '__main__':
    __test__()
