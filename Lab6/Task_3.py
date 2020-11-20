from random import randrange as rnd, choice
import tkinter as tk
import math
import time

# print (dir(math))

root = tk.Tk()
fr = tk.Frame(root)
root.title("Пушка")  # Название окна.
root.geometry('800x600')  # Размеры окна.
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)


class ball():
    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.delete = 0
        self.delete_point = 0.7  # Нужна, чтобы пули и пулемета удалялись быстрее.
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.g = 0.18  # Ускорение свободного падения.
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = rnd(1, 10)

    def destroy(self):
        """Проверяет необходимость удаления мяча из списка мячей.
           Возращает 1, если нужно убрать, 0 если не нужно"""
        if self.live == 0 or self.delete == 1:
            canv.delete(self.id)
            return 1
        else:
            return 0

    def set_coords(self):
        """Рисует снаряд"""
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.
        Метод описывает перемещение мяча за один кадр. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x > 750:
            self.vx *= -1

        if self.y - self.vy > 555:
            if self.vy < 0:
                self.vy *= -1

        self.vy -= self.g
        if self.y - self.vy > 556:
            self.vy = 0

        if (self.vx ** 2 + self.vy ** 2) <= self.delete_point ** 2:
            self.delete = 1

        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        self.vx *= 0.995
        self.vy *= 0.995

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.
        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 < (obj.r + self.r) ** 2:
            return True

        else:
            return False


class miniball(ball):
    """
    Этот класс создает снаряды меньшего размера, меньших очков здоровья, но с улучшенными динамическими характеристиками.
    """
    def __init__(self, x, y):
        global point
        self.delete = 0
        self.delete_point = 0.1  # Нужна, чтобы пули и пулемета удалялись быстрее.
        self.x = x
        self.y = y
        self.r = 5
        self.vx = 0
        self.vy = 0
        self.g = 0.09  # Ускорение свободного падения.
        self.color = 'black'
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = rnd(1, 5)
        if point > 0:
            point -= 1


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f3_power = 10
        self.f2_on = 0
        self.f3_on = 0
        self.an = 1

        # Координаты пушки. # Перезаписываются в классе tank.
        self.x = 200
        self.y = 480

        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)

    def fire2_start(self, event):
        """
        Запускает снаряд
        :param event:  Массив событий, созданный pygame.
        :return: меняет переменную, проверка которой запустит выстрел.
        """
        self.f2_on = 1

    def fire3_start(self, event):
        """
        Запускает снаряд
        :param event:  Массив событий, созданный pygame.
        :return: меняет переменную, проверка которой запустит выстрел.
        """
        self.f3_on = 1

    def fire2_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        :param event:  Массив событий, созданный pygame.
        :return: Оканчивает выстрел и спавнит снаряд на месте пушки.
        """
        global balls, bullet
        if self.f2_on == 1:
            bullet += 1
            new_ball = ball(self.x, self.y)
            new_ball.r += 5
            # Зададим скорости снаряду.
            new_ball.vx = self.f2_power * math.cos(self.an) / 3
            new_ball.vy = - self.f2_power * math.sin(self.an) / 3
            balls += [new_ball]
            self.f2_on = 0
            self.f2_power = 10

    def fire3_end(self, event):
        """
        Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        :param event:  Массив событий, созданный pygame.
        :return: Оканчивает выстрел и спавнит снаряд на месте пушки.
        """
        global balls, bullet
        if self.f3_on == 1:
            bullet += 1
            new_ball = miniball(self.x, self.y)
            new_ball.r += 5
            # Зададим скорости снаряду.
            new_ball.vx = self.f3_power * math.cos(self.an) / 3
            new_ball.vy = - self.f3_power * math.sin(self.an) / 3
            balls += [new_ball]
            self.f3_on = 0
            self.f3_power = 10

    def targetting(self, event=0):
        """
        Прицеливание. Зависит от положения мыши.
        :param event:  Массив событий, созданный pygame.
        :return:  Наводит пушку на курсор.
        """
        if event:
            # Получает угол, на который няжно повернуть пушку, чтобы она была направлена на курсор.
            self.an = math.atan((event.y - self.y) / (event.x - self.x))

            # Поворачивает угол относительно вертикали, если курсор левее пушки.
            if (event.x - self.x) / math.fabs(event.x - self.x) == -1:
                self.an = math.atan((event.y - self.y) / (event.x - self.x)) + math.pi
            # Поворачивает пушку с учетом направления танка.
            if 0 < self.an < math.pi / 2:
                self.an = 0
            elif math.pi / 2 <= self.an < math.pi:
                self.an == math.pi
            elif tank.rootate == 1 and math.pi / 2 <= self.an <= 1.5 * math.pi:
                self.an = -1 * math.pi / 2
            elif tank.rootate == -1 and -0.5 * math.pi <= self.an <= 0.5 * math.pi:
                self.an = 1.5 * math.pi

        if self.f2_on or self.f3_on:
            canv.itemconfig(self.id, fill='orange')

        else:
            canv.itemconfig(self.id, fill='black')

        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """
        Увеличавает начальную скорость снаряда, пока зажата мышь, и он еще не запущен
        :return:  Увеличивает переменную power для того вида снарядов, которым ведется выстрел.
        """
        if self.f2_on or self.f3_on:
            if self.f2_power < 50 and self.f2_on:
                self.f2_power += 0.75

            if self.f3_power < 50 and self.f3_on:
                self.f3_power += 1.5

            canv.itemconfig(self.id, fill='orange')

        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.new_target()
        self.colors = ['green', 'yellow', 'orange', 'red']

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 750)
        y = self.y = rnd(200, 500)
        r = self.r = rnd(5, 50)

        self.v_x = rnd(-3, 2) / 2
        self.v_y = rnd(-3, 2) / 2

        self.live = rnd(1, 5)

        color = self.color = ['green', 'green', 'yellow', 'orange', 'red'][self.live]
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points

    def move(self):
        """Отвечает за движение целей."""
        self.x += self.v_x
        self.y += self.v_y

        # Столкновения со стенами.
        if self.y >= 520 or self.y <= 100:
            self.v_y *= -1

        if self.x >= 750 or self.x <= 100:
            self.v_x *= -1

        # Рисуем его на новых координатах.
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        color = ['green', 'green', 'yellow', 'orange', 'red'][self.live]
        canv.itemconfig(self.id, fill=color)


class Background():
    """Класс отвечает за рисование фона."""

    def __init__(self):
        self.id = canv.create_oval(0, 0, 0, 0)

    def green(self):
        """Рисует холмик с травой."""
        self.weight = rnd(70, 130)
        self.height = self.weight / 2

        self.x = rnd(0, 750)
        self.y = rnd(610, 630)
        color = self.color = 'lawn green'
        canv.coords(self.id, self.x - self.weight, self.y - self.height, self.x + self.weight, self.y + self.height)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        """Отвечает за движение."""
        self.x += self.v_x
        self.y += self.v_y


class Sunlight(Background):
    def __init__(self):
        Background.__init__(self)
        self.isDay = 1

    def sun(self):
        """Рисует солнышко."""
        x = self.x = rnd(600, 700)
        y = self.y = rnd(20, 50)
        r = self.r = rnd(20, 50)

        self.v_x = 0.25
        self.v_y = 0

        color = self.color = 'yellow'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def changer_day_night(self):

        # Столкновения со стенами.

        if self.x > 750 or self.x < 150 + self.r:
            self.v_x *= -1
            self.isDay *= -1
            if self.color == 'yellow':
                self.color = 'white'
            else:
                self.color = 'yellow'

        # Рисуем его на новых координатах.
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)
        canv.itemconfig(self.id, fill=self.color)

        # Изменим освещение((

    def set_cords(self):
        canv.coords(self.id, self.x - self.r, self.y - self.r, self.x + self.r, self.y + self.r)


class tank():
    def __init__(self):
        x = self.x = 300
        y = self.y = 550
        self.alpha = 1
        self.vx = 0
        self.rootate = 1
        self.live = 100
        self.r = 30 * self.alpha

        # Гусеница.
        self.guslya = canv.create_oval(0, 0, 0, 0)

        # Зададим фигуры катков:
        self.id_wheel1 = canv.create_oval(0, 0, 0, 0)
        self.id_wheel2 = canv.create_oval(0, 0, 0, 0)
        self.id_wheel3 = canv.create_oval(0, 0, 0, 0)
        self.id_wheel4 = canv.create_oval(0, 0, 0, 0)

        # Зададим фигуры внутренних кружков катков.
        self.id_IN_wheel1 = canv.create_oval(0, 0, 0, 0)
        self.id_IN_wheel2 = canv.create_oval(0, 0, 0, 0)
        self.id_IN_wheel3 = canv.create_oval(0, 0, 0, 0)
        self.id_IN_wheel4 = canv.create_oval(0, 0, 0, 0)

        # Тело танка.
        self.body = canv.create_oval(0, 0, 0, 0)
        # self.id_body = canv.create_rectangle(0, 0, 0, 0)
        self.id_tower = canv.create_oval(0, 0, 0, 0)
        self.id_oval = canv.create_oval(0, 0, 0, 0)

        self.printing(x, y)

    def print_wheel(self, id_wheel, id_IN_wheel, x, y, alpha):
        """
        Рисует колесо танка.

        :param id_wheel: Колесо.
        :param x, y: Координаты опорной точки танка
        :param alpha: Коэфициент расшиения танка.
        :param num: Номер колеса.
        :return: Колесо.
        """
        r = 10 * alpha
        r_IN = r / 3
        canv.coords(id_wheel, x - r, y - r, x + r, y + r)
        canv.itemconfig(id_wheel, fill='green')
        canv.coords(id_IN_wheel, x - r_IN, y - r_IN , x + r_IN, y + r_IN)
        canv.itemconfig(id_IN_wheel, fill='green')

    def print_guslya(self, x, y, distance, alpha):
        canv.coords(self.guslya, x - 2 * distance, y - 15 * alpha, x + 2 * distance, y + 15 * alpha)
        canv.itemconfig(self.guslya, fill='black')

    def print_body(self, x, y, distance, alpha):
        y1 = y - 13 * alpha
        canv.coords(self.body, x - 2 * distance, y1 - 19 * alpha, x + 2 * distance, y1 + 12 * alpha)
        canv.itemconfig(self.body, fill='green')

    def print_tower(self,  x, y, distance, alpha):
        y1 = y - 33 * alpha
        canv.coords(self.id_tower, x - 1 * distance, y1 - 19 * alpha, x + 1 * distance, y1 + 12 * alpha)
        canv.itemconfig(self.id_tower, fill='khaki4')

        x1 = x + distance / 2 + 4 * alpha
        y2 = y1 - 4 * alpha

        g1.y = y2
        g1.x = x1

        r = 13 * alpha
        canv.coords(self.id_oval, x1 - r, y2 - r, x1 + r, y2 + r)
        canv.itemconfig(self.id_oval, fill='khaki2')

    def printing(self, x, y):
        alpha = self.alpha
        distance = 30 * alpha

        # Рисуем катки.
        self.print_wheel(self.id_wheel1, self.id_IN_wheel1, x - 1.5 * distance, y, alpha)
        self.print_wheel(self.id_wheel2, self.id_IN_wheel2, x - 0.5 * distance, y, alpha)
        self.print_wheel(self.id_wheel3, self.id_IN_wheel3, x + 0.5 * distance, y, alpha)
        self.print_wheel(self.id_wheel4, self.id_IN_wheel4, x + 1.5 * distance, y, alpha)

        # Рисуем гусеницу.
        self.print_guslya(x, y, distance, alpha)

        # Рисуем тело танка.
        self.print_body(x, y, distance, alpha)

        # Рисует башню.
        self.print_tower(x, y, distance, alpha)

    def move(self):
        if 100 + self.vx < self.x < 720 + self.vx:
            self.x += self.vx
            alpha = self.alpha
            rootate = self.rootate
            # Посчитаем константы.
            distance = 30 * alpha
            r = 10 * alpha
            r_IN = r / 3
            x = self.x
            y = self.y

            # Обновим координаты.
            canv.coords(self.id_wheel1, x - 1.5 * distance - r, y - r, x - 1.5 * distance + r, y + r)
            canv.coords(self.id_wheel2, x - 0.5 * distance - r, y - r, x - 0.5 * distance + r, y + r)
            canv.coords(self.id_wheel3, x + 0.5 * distance - r, y - r, x + 0.5 * distance + r, y + r)
            canv.coords(self.id_wheel4, x + 1.5 * distance - r, y - r, x + 1.5 * distance + r, y + r)

            canv.coords(self.id_IN_wheel1, x - 1.5 * distance - r_IN, y - r_IN, x - 1.5 * distance + r_IN, y + r_IN)
            canv.coords(self.id_IN_wheel2, x - 0.5 * distance - r_IN, y - r_IN, x - 0.5 * distance + r_IN, y + r_IN)
            canv.coords(self.id_IN_wheel3, x + 0.5 * distance - r_IN, y - r_IN, x + 0.5 * distance + r_IN, y + r_IN)
            canv.coords(self.id_IN_wheel4, x + 1.5 * distance - r_IN, y - r_IN, x + 1.5 * distance + r_IN, y + r_IN)

            canv.coords(self.body, self.x - 2 * distance, self.y - 32 * alpha,
                        self.x + 2 * distance, self.y - 1 * alpha)
            canv.coords(self.guslya, self.x - 2 * distance, self.y - 15 * alpha,
                        self.x + 2 * distance, self.y + 15 * alpha)

            canv.coords(self.id_tower, x - 1 * distance, y - 52 * alpha, x + 1 * distance, y - 21 * alpha)
            r = 13 * alpha
            x1 = x + (distance / 2 + 4 * alpha) * rootate
            y2 = y - 37 * alpha
            canv.coords(self.id_oval, x1 - r, y2 - r, x1 + r, y2 + r)
            # Передвинем пушку.
            g1.x = x + (distance / 2 + 4 * alpha) * rootate

    def move_left(self, event):
        """
        Отвечает за движение танка.
        :param event:  Массив событий, созданный pygame.
        :return: Меняет координаты танка и разворачивает его в сторну движения.
        """
        if event.keysym == 'Left':
            # self.vx -= 1 # Сейчас не используется.
            self.x -= 5
            if self.vx <= 0:
                self.rootate = -1

        if event.keysym == 'Right':
            # self.vx += 1
            self.x += 5
            if self.vx >= 0:
                self.rootate = 1


targs = []  # Массив активных мишеней.
for i in range(10):
    targs.append(target())

dest_targs = []  # Массив мишеней.
for i in range(10):
    dest_targs.append(targs[i])

screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
point = 0  # Счет.
stop = 0  # Проверка на конец игры.

tank = tank()  # Танк.


def new_game(event=''):
    """
    Запускает новую игру.
    :param event: Задаем переменную, в которой по прошествии времени будет лежать массив событий, созданный pygame.
    :return: Игру.
    """
    global gun, targs, screen1, balls, bullet, dest_targs, point, stop
    for i in range(rnd(2, 10, 1)):
        targs[i].new_target()  # Создание цели.

    bullet = 0  # Кол - во попаданий по мишени.
    balls = []  # Массив шаров.
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<Button-3>', g1.fire3_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<ButtonRelease-3>', g1.fire3_end)
    canv.bind('<Motion>', g1.targetting)
    canv.bind_all('<Key>', tank.move_left)
    id_points = canv.create_text(30, 30, text=point, font='28')
    id_Lives  = canv.create_text(56, 50, text=point, font='28')

    time_per_frames = 0.007  # Время между кадрами.
    for targ in targs:
        targ.live = 1  # Кол - во необходимых попаданий в первые мишени.

    # Нарисуем фон.
    # Рисуем траву.
    back = []  # Массив холмиков с травой.
    for i in range(10):
        back.append(Background())
        back[i].green()

    # Рисуем солнышко.
    sun = Sunlight()
    sun.sun()

    while True:
        if stop == 0:
            # Переместим цели.
            for targ in targs:
                targ.move()
            # Передвинем солнышкою
            sun.move()
            sun.set_cords()
            sun.changer_day_night()
            # Передвинем танк.
            tank.move()
            # Обновим счет здоровья.
            canv.itemconfig(id_Lives, text='Здоровье:' + str(tank.live))
            # Обновим счет.
            canv.itemconfig(id_points, text=str(point))
            # Переберем мячи из массива.
            for b in balls:
                #  Передвинем мяч.
                b.move()

                for targ in targs:
                    # Проверка на попадаения мяча в цель.
                    if b.hittest(targ) and targ.live:
                        targ.live -= 1
                        b.live -= 1
                        point += 1

                    # Проверяем сколько раз осталось попасть по мишени.
                    if targ.live == 0:
                        targ.hit()  # Обработка попадания.
                        canv.itemconfig(id_points, text=point)  # Обновим счет.
                        targs.remove(targ)

                # Проверка на необходимость убрать мяч.
                if b.destroy() == 1:
                    balls.remove(b)  # Убираем мяч.

                if b.hittest(tank):
                    tank.live -= 1
                    b.live -= 1

            # Нарисуем новую мишень, если более на поле нет снарядов.
            if len(targs) == 0:
                for i in range(rnd(2, 10, 1)):
                    targs.append(dest_targs[i])  # Вернем мишень в массив

                    targs[i].new_target()  # Нарисуем новую мишень.
            if tank.live <= 0:
                canv.itemconfig(screen1, text='Игра закончена((( Потрачено: ' + str(bullet) + ' выстрелов \n' +
                                'счет: ' + str(point))
                stop = 1

        canv.update()  # Обновим кадр.
        time.sleep(time_per_frames)  # Задержка позволяет установить ФПС на уровне ~120.
        g1.targetting()  # Наведем пушку на курор.
        g1.power_up()  # Увеличим начальную скорость снаряда, если зажата мышь.


if __name__ == '__main__':
    new_game()
