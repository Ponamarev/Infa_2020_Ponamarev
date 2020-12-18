import math
from graphic import *
from settings import *
import tkinter


class PlayerImage():
    def __init__(self, root, canv):
        """
        Это конструктор класса, отвечающего за рисование текстуры игрока.
        :param root: Окно, на котором рисуется игра.
        :param canv: Холст, на котором рисуется игрок.
        """
        self.x = 100
        self.y = 90
        self.size = player_size
        self.params = [1, 1, 0, 0]
        self.root = root
        self.canv = canv
        self.fr = 0
        self.color = 'green'
        self.color_of_body = 'bisque2'
        self.color_of_outline = 'black'
        self.right_leg_obj = canv.create_polygon(0, 0, 0, 0, fill=self.color_of_body, outline=self.color_of_outline)
        self.left_leg_obj = canv.create_polygon(0, 0, 0, 0, fill=self.color_of_body, outline=self.color_of_outline)
        self.left_hand_obj = canv.create_polygon(0, 0, 0, 0, fill=self.color, outline=self.color)
        self.right_hand_obj = canv.create_polygon(0, 0, 0, 0, fill=self.color, outline=self.color)
        self.body_obj = canv.create_polygon(0, 0, 0, 0, fill=self.color, outline=self.color_of_outline)
        self.head_obj = canv.create_oval(0, 0, 0, 0, fill=self.color_of_body, outline=self.color_of_outline)
        self.neck_obj = canv.create_rectangle(0, 0, 0, 0, fill=self.color_of_body, outline=self.color_of_body)
        self.animate_on = 0
        self.last_animate = 0

    def body(self, x, y, k):
        """
        Рисует тело игрока (Голову, и туловище).
        :param x и y: Координаты центр головы.
        :param k: Коэфицент расширения.
        :return: None
        """
        self.canv.coords(self.neck_obj,
                         x - k, y + 2 * k, x + k, y + 6 * k,
                         )
        self.canv.coords(self.head_obj,
                         x - 4 * k, y - 4 * k, x + 4 * k, y + 4 * k,
                         )
        self.canv.coords(self.body_obj,
                         x - 3 * k, y + 18 * k, x - 6 * k, y + 8 * k,
                         x - k, y + 6 * k, x + k, y + 6 * k,
                         x + 6 * k, y + 8 * k, x + 3 * k, y + 18 * k,
                         )

    def right_hand(self, x, y, k, alpha_right):
        """
        Рисует правую руку.
        :param x и y: Координаты правой верхней точки руки.
        :param k:  Коэфицент расширения.
        :param alpha_right: Угол поворота (положительный поворачивает вправо).
        :return: None
        """
        self.canv.coords(self.right_hand_obj,
                         x - 6 * k, y + 8 * k,
                         x - 6 * k + 2 * k * math.cos(alpha_right), y + 8 * k + 2 * k * math.sin(alpha_right),
                         x - 6 * k - 18 * k * math.sin(alpha_right) + 2 * k * math.cos(alpha_right),
                         y + 8 * k + 18 * k * math.cos(alpha_right) + 2 * k * math.sin(alpha_right),
                         x - 6 * k - 18 * k * math.sin(alpha_right), y + 8 * k + 18 * k * math.cos(alpha_right),
                         )

    def left_hand(self, x, y, k, alpha_left):
        """
        Рисует левую руку.
        :param x и y: Координаты левой верхней точки руки.
        :param k:  Коэфицент расширения.
        :param alpha_left: Угол поворота (положительный поворачивает влево).
        :return: None
        """
        self.canv.coords(self.left_hand_obj,
                         x + 6 * k, y + 8 * k,
                         x + 6 * k - 2 * k * math.cos(alpha_left), y + 8 * k + 2 * k * math.sin(alpha_left),
                         x + 6 * k + 18 * k * math.sin(alpha_left) - 2 * k * math.cos(alpha_left),
                         y + 8 * k + 18 * k * math.cos(alpha_left) + 2 * k * math.sin(alpha_left),
                         x + 6 * k + 18 * k * math.sin(alpha_left), y + 8 * k + 18 * k * math.cos(alpha_left),
                         )

    def right_leg(self, x, y, k, beta_right):
        """
        Рисует правую ногу.
        :param x и y: Координаты правой верхней точки ноги.
        :param k:  Коэфицент расширения.
        :param beta_right:  Угол поворота (положительный поворачивает вправо).
        :return:  None
        """
        self.canv.coords(self.right_leg_obj,
                         x - 3 * k, y + 16 * k,
                         x - 3 * k + 3 * k * math.cos(beta_right), y + 16 * k + 3 * k * math.sin(beta_right),
                         x - 3 * k - 24 * k * math.sin(beta_right) + 3 * k * math.cos(beta_right),
                         y + 16 * k + 24 * k * math.cos(beta_right) + 3 * k * math.sin(beta_right),
                         x - 3 * k - 24 * k * math.sin(beta_right), y + 16 * k + 24 * k * math.cos(beta_right),
                         )

    def left_leg(self, x, y, k, beta_left):
        """
        Рисует левую ногу.
        :param x и y: Координаты левой верхней точки ноги.
        :param k:  Коэфицент расширения.
        :param beta_left:  Угол поворота (положительный поворачивает влево).
        :return:  None
        """
        self.canv.coords(self.left_leg_obj,
                         x + 3 * k, y + 16 * k,
                         x + 3 * k - 3 * k * math.cos(beta_left), y + 16 * k + 3 * k * math.sin(beta_left),
                         x + 3 * k + 24 * k * math.sin(beta_left) - 3 * k * math.cos(beta_left),
                         y + 16 * k + 24 * k * math.cos(beta_left) + 3 * k * math.sin(beta_left),
                         x + 3 * k + 24 * k * math.sin(beta_left), y + 16 * k + 24 * k * math.cos(beta_left),
                         )

    def draw_human(self):
        """
        Перерисовывает текстуру игрока.
        :return:  None
        """
        self.body(self.x, self.y, self.size)
        self.right_hand(self.x, self.y, self.size, self.params[0])
        self.left_hand(self.x, self.y, self.size, self.params[1])
        self.right_leg(self.x, self.y, self.size, self.params[2])
        self.left_leg(self.x, self.y, self.size, self.params[3])

    def __test_draw__(self):
        """
        Запускает выбранную тестировщиком анмацию.
        :return: None
        """
        self.animate_move()
        self.root.after(50, self.__test_draw__)

    def animate_move(self):
        """
        Отвечает за анимацию игрока.
        :return:  None
        """
        if self.animate_on == 0:
            self.params = [1, 1, 0, 0]

        elif self.animate_on == 1:
            if self.fr > 20:
                self.animate_on = 0
            self.fr += 1
            self.params[0] = 0.6 + math.sin(self.fr / 10)
            self.params[1] = 0.6 + math.sin(self.fr / 10)
            self.params[2] = 0 + math.sin(self.fr / 10) / 3
            self.params[3] = 0 + math.sin(self.fr / 10) / 3
            self.last_animate = self.animate_on

        elif self.animate_on == 2:
            if self.last_animate != self.animate_on:
                self.fr = 0
            elif self.fr > 7:
                self.animate_on = 0
            self.fr += 1
            self.params[0] = 0.6 + math.sin(self.fr / 3)
            self.params[1] = 0.6 + math.sin(self.fr / 3)
            self.params[2] = 0 + math.sin(self.fr / 3) / 3
            self.params[3] = 0 + math.sin(self.fr / 3) / 3
            self.last_animate = self.animate_on

        self.draw_human()


if __name__ == '__main__':
    print("Это модуль не для отдельного запуска. \nВключен режим тестирования.")

    canv = tkinter.Canvas(
        width=wight_of_screen,
        height=height_of_screen,
        bg='black',
        highlightthickness=0
    )
    canv.pack()
    root = tkinter.Tk()
    root.geometry('{}x{}'.format(str(wight_of_screen), str(height_of_screen)))
    p = PlayerImage(root, canv)

    print("Введите номер анимации для показа.\nТанец: 1.\nУдар в обе стороны: 2.")
    p.animate_on = int(input())
    # Проверим ввод на правильность.
    assert -1 < p.animate_on < 3 and p.animate_on % 1 == 0, "Введите целое число от 0 до 2"

    p.__test_draw__()
    root.mainloop()
