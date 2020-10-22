import pygame
from pygame.draw import *
from tkinter import *

pygame.init()  # Инициализация Pygame.
Window = Tk()  # Графический интерпретатор.

screen = pygame.display.set_mode((800, 1000))  # будет добавлен экран с альфа каналом
screen2 = pygame.Surface((800, 1000))
screen1 = pygame.Surface((800, 1000))
screen2.set_colorkey((0, 0, 0))
screen2.set_alpha(128)
screen3 = pygame.Surface((800, 1000))

FPS = 30
pi = 3.14159

color_of_ino = (200, 254, 206)
PURPLE = (255, 0, 255)
White = (250, 255, 255)

# Переменные, используемые в движении.
V_x_NLO = 0
V_y_NLO = 0
Active_rey = 0
Anim_rey_numF = 0
visibility = 55
VisOn = 1
x_NLO = 110
y_NLO = 310
x_rey = 30
y_rey = 0


def Settings():
    pygame.display.update()
    clock = pygame.time.Clock()

    global VisOn
    global V_x_NLO, V_y_NLO

    while True:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                Visibility_Use()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                Rey_active()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_w:
                V_y_NLO += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                V_y_NLO -= 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                V_x_NLO += 1
            if event.type == pygame.KEYDOWN and event.key == pygame.K_a:
                V_x_NLO -= 1
        Vis_check(visibility, VisOn)
        Going_NLO_check(V_x_NLO, V_y_NLO)
        Go_check()
        Rey_check()
        Exs2_imgN17()
        if V_x_NLO != 0:
            screen3 = pygame.transform.rotate(screen1, int(50 * V_x_NLO / 5))
            screen3 = pygame.transform.rotate(screen2, int(50 * V_x_NLO / 5))
            screen.blit(screen3, (((0 + x_NLO) / 0.5), ((-350 + y_NLO) / 0.5)))
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
    screen2 = pygame.Surface((800, 1000))
    screen1 = pygame.Surface((800, 1000))
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
                                       (Alpha * 155 + Alpha * x_rey, Alpha * 444 + Alpha * y_rey),
                                       (Alpha * 155 - Alpha * x_rey, Alpha * 444 + Alpha * y_rey)], 0)

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
    NLO(x_NLO, y_NLO, visibility, 0.5)

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
    if Alpha:  # Заполняем блоки левее нужного.
        for Block in range(x - 1):
            text1 = Label(Window, text="           ")
            text1.grid(column=Block, row=y)

    text1 = Label(Window, text=text)
    text1.grid(column=x, row=y)


def Visibility_Use():
    """
    Включение/выключение видимости НЛО.

    :param VisOn: Параметр, в котором написано, включена ли видимость в данный момент.
    :return:      None
    """
    global VisOn
    if VisOn == 0:
        VisOn += 1
    else:
        VisOn -= 1


def Vis_check(Visibility, VisOn):
    """
    Плавон приводит видимость к тому значению, которое просит пользователь.

    :param Visibility:  Видимость в данный момент.
    :param VisOn:       Должнв ли быть видимость.
    :return:            None
    """
    global visibility
    if VisOn == 1 and Visibility <= 250:
        visibility += 5
    if VisOn == 0 and Visibility >= 5:
        visibility -= 5


def Rey_active():
    """
    Включение/ выключение луча захвата.

    :return:    None
    """
    global Active_rey
    if Active_rey == 1:
        Active_rey = 0
    else:
        Active_rey = 1


def Rey_check():
    global x_rey, y_rey
    global Anim_rey_numF

    if Active_rey == 1 and Anim_rey_numF < 120:
        Anim_rey_numF += 1       # Считаем кадры

        if Anim_rey_numF <= 100:  # 120, 186 - координаты макс x_rey и y_rey
            y_rey += 186 / 100
        else:
            x_rey += 90 / 20

    if Active_rey == 0 and Anim_rey_numF > 0:
        Anim_rey_numF -= 1       # Считаем кадры

        if Anim_rey_numF < 100:  # 120, 186 - координаты макс x_rey и y_rey
            y_rey -= 186 / 100
        else:
            x_rey -= 90 / 20

def Going_NLO_check(V_x_NLO, V_y_NLO):
    """
    Отвечает за движение НЛО.
    :return: None
    """
    global x_NLO
    global y_NLO
    global screen1, screen2
    x_NLO += V_x_NLO
    y_NLO -= V_y_NLO


def Go_check():
    """
    Отвечает за то, чтобы НЛО имело инерцию.
    :return:  None
    """
    global V_x_NLO
    global V_y_NLO
    V_x_NLO = V_x_NLO * 0.95
    V_y_NLO = V_y_NLO * 0.93


def Learning():
    """
    Рассказывает об органах управления программы.

    :return:   None
    """
    global Window

    Window.title("Управление")  # Название окна.
    Window.geometry("700x450")  # Размер окна.
    Learn_text(Window, "Это программа Ino_NEW_Animated.py", 1, 0, True)
    Learn_text(Window, "Версия 1.2", 1, 1, True)
    Learn_text(Window, "          ", 1, 2, True)
    Learn_text(Window, "Cделать НЛО прозрачным", 1, 3, True)
    Learn_text(Window, ".........................", 2, 3, 0)
    Learn_text(Window, "Пробел", 3, 3, 0)
    Learn_text(Window, "Элементы управления НЛО", 1, 4, True)
    Learn_text(Window, ".........................", 2, 4, 0)
    Learn_text(Window, "WASD", 3, 4, 0)
    Learn_text(Window, "Включить луч захвата", 1, 5, 1)
    Learn_text(Window, ".........................", 2, 5, 0)
    Learn_text(Window, "E", 3, 5, 0)


try:
    # Сначала дадит почитать управление и после закрытия окна включим программу.
    Learning()
    Window.mainloop()

finally:
    # Включение программы.
    Exs2_imgN17()
    Settings()
