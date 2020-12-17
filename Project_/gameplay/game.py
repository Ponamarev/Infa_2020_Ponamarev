import gameplay.gameobjects
import gameplay.world
import tkinter
import math


class Game:
    def __init__(self, canvas, root):
        self.canv = canvas
        self.root = root
        self.world = gameplay.world.World()
        self.root.bind('<KeyPress-Return>', self.pressing, add='')
        self.root.bind('<KeyRelease-Return>', self.unpressing)
        self.player = gameplay.gameobjects.Player(self.canv, self.root, [50, 50])
        # self.enemy = gameplay.gameobjects.Enemy(self.canv, [100, 100])
        # self.world.active_things.extend([self.player, self.enemy])
        self.draw_world()
        self.pressed = False

    def react(self, event=tkinter.NONE):
        if self.pressed:
            self.canv.move("rect", 5, 0)
            self.root.after(50, self.react)

    def draw_world(self):
        self.rect = self.canv.create_rectangle(10, 10, 60, 60, fill='yellow', tag="rect")

    def unpressing(self, event=tkinter.NONE):
        self.pressed = False

    def pressing(self, event=tkinter.NONE):
        if not self.pressed:
            self.pressed = True
            self.react()

    def draw_interface(self):
        pass
        
    def update(self, time):
        self.root.bind('<KeyPress-Return>', self.pressing, add='')
        self.root.bind('<KeyRelease-Return>', self.unpressing)
        # self.world.update(time)
        self.draw_interface()

        return self

    def give_param(self):
        return 'string'
