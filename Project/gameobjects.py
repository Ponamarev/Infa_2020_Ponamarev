import tkinter
import math
import gameplay.graphic_human

# abstract class (using in this module only)
class ActiveObject(object):
    def __init__(self, canvas, tag, coords):
        self.canv = canvas
        self.tag = tag
        self.coords = coords
        self.heet_box = None
    
    def update(self):
        return self

    def draw_self(self):
        pass


class Player(ActiveObject):
    def __init__(self, canvas, root, coords=[150, 150], tag="player"):
        super().__init__(canvas, tag, coords)
        self.speed = 5
        self.health_points = 100
        self.experience_points = 0
        self.controlers_but = ['w', 'a', 's', 'd']
        self.dict_controlers_but = {'w': (0, 1),  'a': (-1, 0),
                                    's': (0, -1), 'd': (1, 0)}
        self.root = root
        self.root.bind('<KeyPress-space>', self.pressing('space'))
        for key in self.controlers_but:
            self.root.bind(key, self.pressing)
        for key in self.controlers_but:
            self.root.bind(key, self.unpressing(key))
        self.pressed_but = None
        self.delta_x = 0
        self.delta_y = 0
        x = self.coords[0]
        y = self.coords[1]
        self.current_mode = 0
        k = 100
        self.id = self.canv.create_rectangle(
            x, y, x + k, y + 2*k,
            fill='red',
            outline='green',
            tag=self.tag
        )

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
            velocity_x = self.speed * way[0]
            velocity_y = self.speed * way[1]
            self.canv.move(self.tag, velocity_x, velocity_y)
        self.root.after(50, self.step)
    
    def attack(self):
        pass

    def draw(self):
        """
        Рисует игрока.
        :return:
        """
        pass


class Enemy(ActiveObject):
    def __init__(self, canvas, coords=[50, 50], tag="enemy"):
        super().__init__(canvas, tag, coords)
