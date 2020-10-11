import pygame
from pygame.draw import *
from tkinter import *

pygame.init()  # Инициализация Pygame.
Window = Tk()  # Графический интерпретатор.

screen = pygame.display.set_mode((800, 1000))  # будет заменен на экран с альфа каналом
screen1 = pygame.Surface((800, 1000), pygame.SRCALPHA)
clock = pygame.time.Clock()

FPS = 30
pi = 3.14159

color_of_ino = (200, 254, 206)


def Settings():
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            # if event.ty


def apple(x, y, Alpha):
    """
    рисует яблоко
    :return: None
    """
    ellipse(screen, (183, 0, 9), (Alpha * (630 + x - 460), Alpha * (620 + y - 480), Alpha * 64, Alpha * 58), 0)
    arc(screen, (0, 0, 0), (Alpha * (657 + x - 460), Alpha * (610 + y - 480), Alpha * 45, Alpha * 60), 0.6 * pi, pi, 2)


def Head(x, y, Alpha, color_of_ino):
    # голова.
    arc(screen, color_of_ino, (Alpha * (490 + x - 460), Alpha * (550 + y - 480),
                               Alpha * 100, Alpha * 30), 2 * pi, pi, 5)
    arc(screen, color_of_ino, (Alpha * (490 + x - 460), Alpha * (488 + y - 480),
                               Alpha * 90, Alpha * 150), pi, 1.5 * pi, 5)
    arc(screen, color_of_ino, (Alpha * (480 + x - 460), Alpha * (488 + y - 480),
                               Alpha * 110, Alpha * 150), 1.5 * pi, 2 * pi, 5)
    ellipse(screen, color_of_ino, (Alpha * (490 + x - 460), Alpha * (550 + y - 480), Alpha * 100, Alpha * 30), 0)
    ellipse(screen, color_of_ino, (Alpha * (493 + x - 460), Alpha * (560 + y - 480), Alpha * 95, Alpha * 30), 0)
    ellipse(screen, color_of_ino, (Alpha * (495 + x - 460), Alpha * (570 + y - 480), Alpha * 90, Alpha * 30), 0)
    ellipse(screen, color_of_ino, (Alpha * (497 + x - 460), Alpha * (580 + y - 480), Alpha * 85, Alpha * 30), 0)
    ellipse(screen, color_of_ino, (Alpha * (500 + x - 460), Alpha * (590 + y - 480), Alpha * 80, Alpha * 30), 0)
    ellipse(screen, color_of_ino, (Alpha * (500 + x - 460), Alpha * (570 + y - 480), Alpha * 80, Alpha * 60), 0)
    ellipse(screen, color_of_ino, (Alpha * (510 + x - 460), Alpha * (605 + y - 480), Alpha * 50, Alpha * 30), 0)


def Left_hear(x, y, Alpha, color_of_ino):
    """
    Рисует левое ухо.
    :param x:             коодината х опорной точки Ино.
    :param y:             коодината х опорной точки Ино.
    :param Alpha:         коэфицент расширения.
    :param color_of_ino:  цвет Ино.
    :return:              None
    """
    ellipse(screen, color_of_ino, (Alpha * (480 + x - 460), Alpha * (500 + y - 490), Alpha * 27, Alpha * 19), 0)
    ellipse(screen, color_of_ino, (Alpha * (487 + x - 460), Alpha * (514 + y - 480), Alpha * 28, Alpha * 13), 0)
    ellipse(screen, color_of_ino, (Alpha * (498 + x - 460), Alpha * (530 + y - 480), Alpha * 15, Alpha * 15), 0)
    ellipse(screen, color_of_ino, (Alpha * (500 + x - 460), Alpha * (540 + y - 480), Alpha * 18, Alpha * 15), 0)


def Right_hear(x, y, Alpha, color_of_ino):
    """
    Рисует правое ухо.
    :param x:             координата х опорной точки Ино.
    :param y:             координата у опорной точки Ино.
    :param Alpha:         коэфицент расширения Ино.
    :param color_of_ino:  цвет Ино.
    :return:              None
    """
    ellipse(screen, color_of_ino, (Alpha * (560 + x - 460), Alpha * (540 + y - 480), Alpha * 25, Alpha * 20), 0)
    ellipse(screen, color_of_ino, (Alpha * (572 + x - 460), Alpha * (530 + y - 480), Alpha * 10, Alpha * 11), 0)
    ellipse(screen, color_of_ino, (Alpha * (560 + x - 460), Alpha * (540 + y - 480), Alpha * 13, Alpha * 16), 0)
    ellipse(screen, color_of_ino, (Alpha * (582 + x - 460), Alpha * (513 + y - 480), Alpha * 10, Alpha * 24), 0)
    ellipse(screen, color_of_ino, (Alpha * (590 + x - 460), Alpha * (500 + y - 480), Alpha * 25, Alpha * 20), 0)


def Body(x, y, Alpha, color_of_ino):
    """
    Рисует тело Ино.
    :param x:             координата х опорной точки Ино.
    :param y:             координата у опорной точки Ино.
    :param Alpha:         коэфицент расширения Ино.
    :param color_of_ino:  цвет Ино.
    :return:              None
    """
    ellipse(screen, color_of_ino, (Alpha * (500 + x - 460), Alpha * (630 + y - 480), Alpha * 70, Alpha * 135), 0)


def Right_leg(x, y, Alpha, color_of_ino):
    """
    Рисует правую ногу Ино.
    :param x:            Координата х опорной точки Ино.
    :param y:            Координата у опорной точки Ино.
    :param Alpha:        Коэфицент расширения Ино.
    :param color_of_ino: Цвет Ино.
    :return:             None
    """
    ellipse(screen, color_of_ino, (Alpha * (550 + x - 460), Alpha * (735 + y - 480), Alpha * 30, Alpha * 40), 0)
    ellipse(screen, color_of_ino, (Alpha * (555 + x - 460), Alpha * (770 + y - 480), Alpha * 30, Alpha * 40), 0)
    ellipse(screen, color_of_ino, (Alpha * (560 + x - 460), Alpha * (804 + y - 480), Alpha * 52, Alpha * 27), 0)


def Left_leg(x, y, Alpha, color_of_ino):
    """
    Рисует левую ногу Ино.
    :param x:            Координата х опорной точки Ино.
    :param y:            Координата у опорной точки Ино.
    :param Alpha:        Коэфицент расширения Ино.
    :param color_of_ino: Цвет Ино.
    :return:             None
    """
    ellipse(screen, color_of_ino, (Alpha * (490 + x - 460), Alpha * (735 + y - 480), Alpha * 30, Alpha * 40), 0)
    ellipse(screen, color_of_ino, (Alpha * (485 + x - 460), Alpha * (765 + y - 480), Alpha * 25, Alpha * 35), 0)
    ellipse(screen, color_of_ino, (Alpha * (450 + x - 460), Alpha * (795 + y - 480), Alpha * 50, Alpha * 25), 0)


def Right_arm(x, y, Alpha, color_of_ino):
    """
    Рисует правую руку Ино.
    :param x:            Координата х опорной точки Ино.
    :param y:            Координата у опорной точки Ино.
    :param Alpha:        Коэфицент расширения Ино.
    :param color_of_ino: Цвет Ино.
    :return:             None
    """
    ellipse(screen, color_of_ino, (Alpha * (556 + x - 460), Alpha * (645 + y - 480), Alpha * 28, Alpha * 26), 0)
    ellipse(screen, color_of_ino, (Alpha * (590 + x - 460), Alpha * (660 + y - 480), Alpha * 25, Alpha * 18), 0)
    ellipse(screen, color_of_ino, (Alpha * (617 + x - 460), Alpha * (664 + y - 480), Alpha * 32, Alpha * 19), 0)


def Left_arm(x, y, Alpha, color_of_ino):
    """
    Рисует левую руку Ино.
    :param x:            Координата х опорной точки Ино.
    :param y:            Координата у опорной точки Ино.
    :param Alpha:        Коэфицент расширения Ино.
    :param color_of_ino: Цвет Ино.
    :return:             None
    """
    ellipse(screen, color_of_ino, (Alpha * (486 + x - 460), Alpha * (645 + y - 480), Alpha * 28, Alpha * 26), 0)
    ellipse(screen, color_of_ino, (Alpha * (467 + x - 460), Alpha * (664 + y - 480), Alpha * 30, Alpha * 20), 0)
    ellipse(screen, color_of_ino, (Alpha * (458 + x - 460), Alpha * (680 + y - 480), Alpha * 15, Alpha * 15), 0)


def eyes(x, y, Alpha):
    """
    Рисует глаза для Ино.
    :param x:           Координата х опорной точки Ино.
    :param y:           Координата у опорной точки Ино.
    :param Alpha:       Коэфинент расшрения Ино.
    :return:            None
    """
    circle(screen, (0, 0, 0), (int(Alpha * (520 + x - 460)), int(Alpha * (580 + y - 480))), int(Alpha * 12), 0)
    circle(screen, (250, 250, 250), (int(Alpha * (525 + x - 460)), int(Alpha * (583 + y - 480))), int(Alpha * 3), 0)

    circle(screen, (0, 0, 0), (int(Alpha * (565 + x - 460)), int(Alpha * (580 + y - 480))), int(Alpha * 10), 0)
    circle(screen, (250, 250, 250), (int(Alpha * (568 + x - 460)), int(Alpha * (582 + y - 480))), int(Alpha * 3), 0)


def person(x, y, Alpha, color_of_ino):
    """
    Рисует инопланетянина.
    x, y координаты верхней левой точки прямоуголька, в котором лежит фигура
    Alpha - коэфицент расширения
    color_of_ino - цвет Ино (получает на вход кортеж типа RGB).
    :return: None
    """
    # Иночеловечек:

    # левое ухо.
    Left_hear(x, y, Alpha, color_of_ino)

    # правое ухо
    Right_hear(x, y, Alpha, color_of_ino)

    # Голова.
    Head(x, y, Alpha, color_of_ino)

    # глаза.
    eyes(x, y, Alpha)

    # Тело инотоварища.
    Body(x, y, Alpha, color_of_ino)

    # рука левая
    Left_arm(x, y, Alpha, color_of_ino)

    # рука правая
    Right_arm(x, y, Alpha, color_of_ino)

    # нога левая
    Left_leg(x, y, Alpha, color_of_ino)

    # нога правая
    Right_leg(x, y, Alpha, color_of_ino)

    # Яблоко.
    apple(x, y, Alpha)


def background():
    """
    Рисует фон - траву, небо, луну.
    :return: None
    """
    rect(screen, (15, 25, 50), (0, 0, 800, 480), 0)
    rect(screen, (30, 50, 20), (0, 480, 800, 1000), 0)
    circle(screen, (193, 193, 193), (550, 223), 120, 0)


def NLO():
    """
    рисует НЛО.
    :return:  None
    """
    # Нло.
    # луч захвата.
    polygon(screen1, (115, 125, 150), [(160, 380), (110, 480), (210, 480)], 0)
    polygon(screen1, (130, 150, 120), [(110, 480), (210, 480), (285, 630), (35, 630)], 0)
    # тело.
    ellipse(screen, (150, 150, 150), (10, 355, 300, 90), 0)
    ellipse(screen, (180, 180, 180), (55, 346, 205, 60), 0)
    # Фары.
    ellipse(screen, (250, 255, 255), (20, 390, 30, 15), 0)
    ellipse(screen, (250, 255, 255), (50, 410, 30, 15), 0)
    ellipse(screen, (250, 255, 255), (90, 417, 30, 15), 0)
    ellipse(screen, (250, 255, 255), (135, 420, 30, 15), 0)
    ellipse(screen, (250, 255, 255), (180, 419, 30, 15), 0)
    ellipse(screen, (250, 255, 255), (225, 410, 30, 15), 0)
    ellipse(screen, (250, 255, 255), (260, 395, 30, 15), 0)


def Clouds():
    """
    рисует облака темные и светлые.
    :return:  None
    """
    #  светлые облака. ( нумерация сверху )
    ellipse(screen, (85, 85, 85), (-208, 10, 730, 170), 0)  # 2
    ellipse(screen, (85, 85, 85), (580, -20, 1000, 112), 0)  # 1
    ellipse(screen, (85, 85, 85), (-208, 205, 743, 130), 0)  # 4
    ellipse(screen, (85, 85, 85), (400, 100, 743, 130), 0)  # 3
    ellipse(screen, (85, 85, 85), (380, 250, 743, 130), 0)  # 5

    # темные облака. ( нумерация сверху )
    ellipse(screen, (55, 55, 55), (150, 70, 730, 100), 0)  # 1
    ellipse(screen, (55, 55, 55), (150, 330, 730, 95), 0)  # 3
    ellipse(screen, (55, 55, 55), (-370, 170, 730, 110), 0)  # 2


def Learn_text(Window, text, x, y, Alpha):
    """
    Пишет текст для управления в Tkinter.

    :param Window:    Окно Tkinter, в котором пишеся текст.
    :param text:      Сам текст.
    :param x:         Номер блока текста по гор. оси
    :param y:         Номер блока текста по верт. оси.
    :param Alpha:     Заполняет все блоки левее пустыми блоками
    :return:          None
    """
    if Alpha:         # Заполняем блоки левее нужного.
        for Block in range(x - 1):
            text1 = Label(Window, text="           ")
            text1.grid(column=Block, row=y)

    text1 = Label(Window, text=text)
    text1.grid(column=x, row=y)

def Learning():
    global Window

    Window.title("Управление")  # Название окна.
    Window.geometry("700x450")
    Learn_text(Window, "Будет добавлено в Ino_NEW_Animated.py", 1, 0, True)
    Learn_text(Window, "Версия 1.1", 1, 1, True)


def Exs2_imgN17(x, y, alpha):
    background()
    Clouds()
    NLO()
    person(20, 0, alpha, (200, 25, 206, 255))


try:
    Learning()
    Window.mainloop()

finally:
    Exs2_imgN17(0, 0, 1)
    Settings()
