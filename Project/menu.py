import tkinter
import graphic
import gameplay.game
import os

saves_directory = "saves\\"

class MenuPage:
    def __init__(self, canvas, root, numlines, wight_of_screen, height_of_screen, time=0):
        self.weight = wight_of_screen
        self.height = height_of_screen
        self.canv = canvas
        self.root = root
        self.numlines = numlines
        # keys using for react
        self.using_keys = [
            "<Up>",
            "<Down>",
            "<Return>"
        ]
        self.current_line = 0
        self.go = -1
        self.time = time

    def react(self, event):
        if event.keysym == "Down":
            self.current_line += 1
            if self.current_line > self.numlines - 1:
                self.current_line = 0

        if event.keysym == "Up":
            self.current_line -= 1
            if self.current_line < 0:
                self.current_line = self.numlines - 1

        if event.keysym == "Return":
            self.go = self.current_line


class PausePage(MenuPage):
    def __init__(self, canvas, root, wight_of_screen, height_of_screen):
        super().__init__(canvas, root, 3, wight_of_screen, height_of_screen)
        self.root.bind('<Key>', tkinter.NONE, add='')
        self.root.bind('<Escape>', self.activation, add='')
        self.game = gameplay.game.Game(self.canv, self.root, wight_of_screen, height_of_screen)
        self.state = False

    def update(self, time):
        if self.state:
            graphic.draw_pause_page(self.current_line)
            if self.go == 0:
                self.desactivation()

            elif self.go == 1:
                savelist = os.listdir(saves_directory)
                save_num = str(len(savelist) + 1)
                new_save = open(saves_directory + save_num + ".txt", 'w+')
                text = self.game.give_param()
                new_save.write(text)
                new_save.close()

            elif self.go == 2:
                start_menu = StartPage(self.canv, self.root, self.weight, self.height)
                return start_menu

        else:
            self.game = self.game.update(time)

        self.go = -1
        return self

    def activation(self, event=tkinter.NONE):
        self.state = True
        self.current_line = 0
        self.root.bind('<Escape>', self.desactivation, add='')
        for key in self.using_keys:
            self.root.bind(key, self.react, add='')

    def desactivation(self, event=tkinter.NONE):
        self.state = False
        self.root.bind('<Key>', tkinter.NONE, add='')
        self.root.bind('<Escape>', self.activation, add='')


class StartPage(MenuPage):
    def __init__(self, canvas, root, wight_of_screen, height_of_screen):
        super().__init__(canvas, root, 4, wight_of_screen, height_of_screen)
        self.timers = [0, 0]
        for key in self.using_keys:
            self.root.bind(key, self.react, add='')

    def update(self, time):
        for i in range(len(self.timers)):
            self.timers[i] -= time
            if self.timers[i] < 0:
                self.timers[i] = 0
        
        if self.timers[1] == 0:
            self.timers[1] = 10000

        if not self.go == -1:
            if self.go == 3:
                self.root.quit()
            
            if self.go == 0:
                pause_page = PausePage(self.canv, self.root, self.weight, self.height)
                return pause_page
            
            self.go = -1
            self.timers[0] = 3000

        graphic.draw_start_page(self.current_line, self.timers)
        return self
        

class Menu:
    def __init__(self, canv, root, wight_of_screen, height_of_screen):
        self.current_state = StartPage(canv, root, wight_of_screen, height_of_screen)

    def update(self, time):
        self.current_state = self.current_state.update(time)
