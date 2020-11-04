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
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color
        )
        self.live = 30

    def destroy(self):
        """Проверяет необходимость удаления мяча из списка мячейю
           Возращает 1, если нужно убрать, 0 если не нужно"""
        if self.delete == 1:
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

        self.vy -= 1
        if self.y - self.vy > 556:
            self.vy = 0

        if abs(self.vy) == 0 and abs(self.vy) == 0:
            self.delete = 1

        self.x += self.vx
        self.y -= self.vy
        self.set_coords()
        self.vx *= 0.985
        self.vy *= 0.99

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


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1

        # Координаты пушки.
        self.x = 200
        self.y = 480

        self.id = canv.create_line(self.x, self.y, self.x + 30, self.y - 30, width=7)

    def fire2_start(self, event):
        """Запускает снаряд"""
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = ball(self.x, self.y)
        new_ball.r += 5
        # Зададим скорости снаряду.
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = - self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            # Получает угол, на который няжно повернуть пушку, чтобы она была направлена на курсор.
            self.an = math.atan((event.y - self.y) / (event.x - self.x))

            # Поворачивает угол относительно вертикали, если курсор левее пушки.
            if (event.x - self.x) / math.fabs(event.x - self.x) == -1:
                self.an = math.atan((event.y - self.y) / (event.x - self.x)) + math.pi

        if self.f2_on:
            canv.itemconfig(self.id, fill='orange')

        else:
            canv.itemconfig(self.id, fill='black')

        canv.coords(self.id, self.x, self.y,
                    self.x + max(self.f2_power, 20) * math.cos(self.an),
                    self.y + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        """Увеличавает начальную скорость снаряда, пока зажат мышь, и он еще не запущен"""
        if self.f2_on:
            if self.f2_power < 50:
                self.f2_power += 3

            canv.itemconfig(self.id, fill='orange')

        else:
            canv.itemconfig(self.id, fill='black')


class target():
    def __init__(self):
        self.points = 0
        self.id = canv.create_oval(0, 0, 0, 0)
        self.id_points = canv.create_text(30, 30, text=self.points, font='28')
        self.new_target()

    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = rnd(600, 780)
        y = self.y = rnd(200, 500)
        r = self.r = rnd(2, 50)

        self.v_x = rnd(-3, 2)
        self.v_y = rnd(-3, 2)

        self.live = 1

        color = self.color = 'red'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def hit(self, points=1):
        """Попадание шарика в цель."""
        canv.coords(self.id, -10, -10, -10, -10)
        self.points += points
        canv.itemconfig(self.id_points, text='')

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
        canv.itemconfig(self.id, fill=self.color)


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
        color = self.color = 'green'
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
        x = self.x = rnd(600, 780)
        y = self.y = rnd(20, 50)
        r = self.r = rnd(20, 50)

        self.v_x = 1
        self.v_y = 0

        color = self.color = 'yellow'
        canv.coords(self.id, x - r, y - r, x + r, y + r)
        canv.itemconfig(self.id, fill=color)

    def changer_day_night(self):

        # Столкновения со стенами.

        if self.x > 750 or self.x < 0:
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


targs = []  # Массив активных мишеней.
for i in range(10):
    targs.append(target())

dest_targs = []  # Массив мишеней.
for i in range(10):
    dest_targs.append(targs[i])

screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
point = 0  # Счет.


def new_game(event=''):
    """ Запускает новую игру"""
    global gun, targs, screen1, balls, bullet, dest_targs, point
    for i in range(rnd(2, 10, 1)):
        targs[i].new_target()  # Создание цели.

    bullet = 0  # Кол - во попаданий по мишени.
    balls = []  # Массив шаров.
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)
    id_points = canv.create_text(30, 30, text=point, font='28')

    time_per_frames = 0.03  # Время между кадрами.
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
        # Переместим цели.
        for targ in targs:
            targ.move()
        # Передвинем солнышко
        sun.move()
        sun.set_cords()
        sun.changer_day_night()
        # Переберем мячи из массива.
        for b in balls:
            #  Передвинем мяч.
            b.move()

            for targ in targs:
                # Проверка на попадаения мяча в цель.
                if b.hittest(targ) and targ.live:
                    targ.live -= 1

                # Проверяем сколько раз осталось попасть по мишени.
                if targ.live == 0:
                    targ.hit()  # Обработка попадания.
                    targs.remove(targ)

            if len(targs) == 0:
                # Выведем текст
                canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')

            # Проверка на необходимость убрать мяч.
            if b.destroy() == 1:
                balls.remove(b)  # Убираем мяч.

        # Сотрем надпись и нарисуем новую мишень, если более на поле нет снарядов.
        if len(balls) == 0 and len(targs) == 0:
            canv.itemconfig(screen1, text='')  # Сотрем надпись.
            bullet = 0  # Обновим счетчик мячей.

            point = dest_targs[0].points  # За эталон возьмем счет, посчитанный первым мячем, т к он появляется всегда.
            canv.itemconfig(id_points, text=point)  # Обновим счет.

            for i in range(rnd(2, 10, 1)):
                targs.append(dest_targs[i])  # Вернем мишень в массив

                targs[i].new_target()  # Нарисуем новую мишень.

        canv.update()  # Обновим кадр.
        time.sleep(time_per_frames)  # Задержка позволяет установить ФПС на уровне ~30.
        g1.targetting()  # Наведем пушку на курор.
        g1.power_up()  # Увеличим начальную скорость снаряда, если зажата мышь.

    canv.itemconfig(screen1, text='')


if __name__ == '__main__':
    new_game()
