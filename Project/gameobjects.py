import tkinter
import math
import gameplay.graphic_human

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

    def update(self):
        return self

    def image_self(self):
        pass


class Player(ActiveObject):
    def __init__(self, canvas, root, coords = [150, 150], tag="player"):
        """
        Это конструктор класса игрока.
        :param canvas: Холст, на котором рисуется игрок.
        :param root: Окно, на котором рисуется игра.
        :param coords:
        :param tag:
        """
        super().__init__(canvas, tag, coords)
        self.speed = 5
        self.health_points = 100
        self.experience_points = 0
        self.controlers_but = ['w', 'a', 's', 'd']
        self.dict_controlers_but = {'w': (0, 1),  'a': (-1, 0),
                                    's': (0, -1), 'd': (1, 0)}
        self.root = root
        self.pressed_but = None
        # [delta_x, delta_y, attack, interaction]
        deltas = [0, 0, False, False]
        self.x = self.coords[0]
        self.y = self.coords[1]
        self.current_mode = 0
        self.id = gameplay.graphic_human.PlayerImage(root, canvas)
        self.root.bind('<KeyPress-space>', self.pressing('space'))
        for key in self.controlers_but:
            self.root.bind(key, self.pressing)
        for key in self.controlers_but:
            self.root.bind(key, self.unpressing(key))

    def pressing(self,  event=tkinter.NONE):
        """
        Обрабатывает нажатие клавиш.
        :param key: Нажатая клавиша.
        :param event: События Tkinter.
        :return: None
        """
        key = 'w'
        # TODO не работает, нужно починить.
        self.pressed_but = key
        if key in self.controlers_but:
            self.step()

    def unpressing(self, event=tkinter.NONE):
        self.pressed_but = None

    def step(self, event=tkinter.NONE):
        if self.pressed_but in self.controlers_but:
            way = self.dict_controlers_but.get(self.pressed_but)
            self.x += self.speed * way[0]
            self.y += self.speed * way[1]
        self.id.draw_human()
        self.root.after(50, self.step)
    
    def attack(self):
        pass

    def draw(self):
        """
        Рисует игрока.
        :return:
        """
        self.id.x, self.id.y = self.x, self.y
        self.id.draw_human()


class Enemy(ActiveObject):
    def __init__(self, canvas, coords=[50, 50], tag="enemy"):
        super().__init__(canvas, tag, coords)
