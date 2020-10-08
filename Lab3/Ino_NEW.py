import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((800, 1000))  # будет добавлен экран с альфа каналом
screen2 = pygame.Surface((800, 1000))
screen1 = pygame.Surface((800, 1000))
screen2.set_colorkey((0, 0, 0))
screen2.set_alpha(128)

FPS = 30
pi = 3.14159

color_of_ino = (200, 254, 206)
PURPLE = (255, 0, 255)
White = (250, 255, 255)



def Settings():
    pygame.display.update()
    clock = pygame.time.Clock()
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

        pygame.display.update()


def Settings_with_alphaChanel():
    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
                screen.blit(screen1, (6675, 66625))

        pygame.display.update()


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


def NLO(x, y, NEW, Alpha):
    """
    рисует НЛО.

    x, y       коодринаты верхней и левой граней НЛО.
    NEW -      непрозраность.
    Alpha -    коэфицент расширения.
    :return:   None
    """
    # Подключаем альфа канал.
    screen1.set_colorkey((0, 0, 0, 0))
    screen1.set_alpha(255)
    screen2.set_colorkey((0, 0, 0, 0))
    screen2.set_alpha(255)

    # Нло.
    # тело.
    ellipse(screen1, (150, 150, 150), (Alpha * 10, Alpha * 355, Alpha * 300, Alpha * 90), 0)
    ellipse(screen1, (180, 180, 180), (Alpha * 55, Alpha * 346, Alpha * 205, Alpha * 60), 0)

    # Фары.
    ellipse(screen1, White, (Alpha * 20, Alpha * 390, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 50, Alpha * 410, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 90, Alpha * 417, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 135, Alpha * 420, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 180, Alpha * 419, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 225, Alpha * 410, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 260, Alpha * 395, Alpha * 30, Alpha * 15), 0)

    # луч захвата.
    polygon(screen2, (205, 195, 190), [(Alpha * 155 - Alpha * 30, Alpha * 444),
                                       (Alpha * 155 + Alpha * 30, Alpha * 444),
                                       (Alpha * 155 + Alpha * 120, Alpha * 444 + Alpha * 186),
                                       (Alpha * 155 - Alpha * 120, Alpha * 444 + Alpha * 186)], 0)

    screen2.set_alpha(NEW * 0.4)
    screen1.set_alpha(NEW)

    screen.blit(screen2, (((0 + x) / Alpha), ((-350 + y) / Alpha)))
    screen.blit(screen1, (((0 + x) / Alpha), ((-350 + y) / Alpha)))


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


def Exs2_imgN17():
    background()
    Clouds()
    NLO(0, 350, 200, 1)
    NLO(110, 250, 50, 1)
    NLO(400, 50, 200, 1)



    person(1000, 950, 0.5, (0, 225, 206))
    person(800, 1100, 0.5, (200, 25, 206))
    person(300, 1000, 0.5, (200, 25, 4))


def test():
    """
    Помогает понять, как работает альфа канал.

    :return: None
    """
    purple_image = pygame.Surface((800, 1000))
    purple_image.set_alpha(55)
    rect(purple_image, PURPLE, (0, 0, 30, 30), 10)
    screen.blit(purple_image, (0, 0))


Exs2_imgN17()

Settings()
