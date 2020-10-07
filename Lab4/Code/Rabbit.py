import pygame
from pygame.draw import *
import random

pygame.init()


def settings(FPS):
    """
    Позволяет не писать весь этот код в конце
    FPS: ФПС
    """
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

# зададим часто используемые цвета заранее
grey =        (128, 128, 128)
grey_black =  (158, 158, 158)
black =       (0, 0, 0)
white =       (255, 255, 255)
green =       (37, 230, 11)
green_black = (37, 204, 11)
blue =        (117, 187, 253)

# константы.
pi = 3.14159

def rabbit_green_for_background(x, y, alphaX, alphaY, screen):
    """
    рисует случайное число травинок ( от 1 до 3)
    опорная точка - верхний левый угол левой травинки
    :param x: координата х верхнего левого угола левой травинки
    :param y: координата х верхнего левого угола левой травинки
    :param alphaX: коэфицент расширения
    :param alphaY: коэфицент расширения
    :param screen: экран, на котором рисуется травинка
    :return:       None
    """
    # Получаем число травинокю
    count = random.randint(1, 3)

    # Рисуем сами травинки
    for step in range(count):
        rect(screen, green_black, (x + step * alphaX * 8, y, alphaX * 12, alphaY * 5), 0)


def rabbit_background(alphaX, alphaY, screen):
    """
    Рисует фон для кролика.

    :param alphaX:  коэфицент расширения ширины фона
    :param alphaY:  коэфицент расширения высоты фона
    :param screen:  экран, на котором рисуется фон
    :return:        None
    """
    rect(screen, blue, (0, 0, 1000 * alphaX, 360 * alphaY), 0)
    rect(screen, green, (0, 360 * alphaY, 1000 * alphaX, 900 * alphaY), 0)

    # рисуем траву:
    # Получаем количество травинок.
    count = random.randint(10, 30)
    # Рисуем эти травинки.
    for green_object in range(count):
        # Получаем коодинаты опорной точки для отдельной травинки.
        x = random.randint(0, 1000 * alphaX)
        y = random.randint(int(360 * alphaY), int(900 * alphaY))
        # Рисуем травинки.
        rabbit_green_for_background(x, y, alphaX, alphaY, screen)


def eye(x, y, alphaX, alphaY, screen):           # FIX
    """
    Функция рисует глаз кролика.

    Опорные координаты
    :param x: координата х
    :param y: координата у
    :param alphaX: коэфицент расширения картинки по оси х
    :param alphaY: коэфицент расширения картинки по оси у
    :param screen: экран, на котором рисуется кролик
    :return: None
    """
    ellipse(screen, white, (x, y, alphaX * 40, alphaY * 34), 0)
    ellipse(screen, black, (x, y, alphaX * 40, alphaY * 34), 1)
    circle(screen, black, (int(x + alphaX * 16), int(y + alphaY * 16)),
           int(alphaX * 4), 0)


def rabbit_hear(x, y, alphaX, alphaY, screen): # fix
    """
    рисует ухо кролика.

    :param x: координата х верхней левойтоки прямоугольника,
    в которую заключено ухо
    :param y: координата у верхней левойтоки прямоугольника,
    в которую заключено ухо
    :param alphaX: коэфицент расширения картинки по оси х
    :param alphaY: коэфицент расширения картинки по оси у
    :param screen: экран, на котором рисуется кролик
    :return: None
    """
    ellipse(screen, grey, (x, y, alphaX * 45, alphaY * 170), 0)
    ellipse(screen, grey_black, (x + alphaX * 7, y + alphaY * 10, alphaX * 30, alphaY * 140), 0)


def rabbit_head(x, y, alphaX, alphaY, screen):   # FIX
    """
    Функция рисует голову кролика.

    Опорные координаты -
    x - координата х
    y - координата у
    alphaX - коэфицент расширения картинки по оси х
    alphaY- коэфицент расширения картинки по оси у
    screen - экран, на котором рисуется кролик
    """
    # уши.
    rabbit_hear(x + alphaX * 410, y + alphaY * 90,
                alphaX, alphaY, screen)
    rabbit_hear(x + alphaX * 550, y + alphaY * 90,
                alphaX, alphaY, screen)

    #  Основа головы.
    ellipse(screen, grey, (x + alphaX * 400, y + alphaY * 200, alphaX * 200, alphaY * 200), 0)

    # рот.
    arc(screen, black, (x + alphaX * 490, y + alphaY * 280,
                        45, 60), 1 * pi, 1.5 * pi, 2)
    arc(screen, black, (x + alphaX * 446, y + alphaY * 280,
                        45, 60), 1.5 * pi, 2 * pi, 2)

    # нос.
    ellipse(screen, black, (x + alphaX * 480, y + alphaY * 300, alphaX * 20, alphaY * 10), 0)

    # Глаза.
    eye(x + alphaX * 450, y + alphaY * 260, alphaX, alphaY, screen)
    eye(x + alphaX * 500, y + alphaY * 260, alphaX, alphaY, screen)


def rabbit_body(x, y, alphaX, alphaY, screen): # FIX
    """
    Функция рисует тело кролика.

    Опорные координаты -
    x - координата х
    y - координата у
    alphaX - коэфицент расширения картинки по оси х
    alphaY- коэфицент расширения картинки по оси у
    screen - экран, на котором рисуется кролик
    """
    ellipse(screen, grey, (alphaX * 425, alphaY * 400, alphaX * 150, alphaY * 400), 0)


def rabbit_legs(x, y, alphaX, alphaY, screen):  # FIX
    """
    Функция рисует ногу кролика.

    Опорные координаты -
    x - координата х
    y - координата у
    alphaX - коэфицент расширения картинки по оси х
    alphaY- коэфицент расширения картинки по оси у
    screen - экран, на котором рисуется кролик
    """
    ellipse(screen, grey, (x, y, alphaX * 60, alphaY * 40), 0)

def rabbit_somethings(x, y, alphaX, alphaY, screen):  # FIX
    """
    Функция рисует аксесуары кролика.

    Опорные координаты -
    x - координата х
    y - координата у
    alphaX - коэфицент расширения картинки по оси х
    alphaY- коэфицент расширения картинки по оси у
    screen - экран, на котором рисуется кролик
    """
    pass


def rabbit(x, y, width, height):
    """
    Рисует кролика.

    x, y - координаты левой верхней точки прямоугольника,
    в который вписан кролик.
    width - ширина прямоугольника.
    height - высота прямоугольника.
    """
    screen = pygame.display.set_mode((width, height))

    # Коэфиценты для расширения линейных размеров по соотв. осям.
    # Они нужны, т к у меня есть возможность самому выбрать размер окна.
    alphaX = width / 1000
    alphaY = height / 900

    rabbit_background(alphaX, alphaY, screen)
    rabbit_head(x, y, alphaX, alphaY, screen)
    rabbit_body(x, y, alphaX, alphaY, screen)
    rabbit_legs(alphaX * 390, alphaY * 790, alphaX, alphaY, screen)
    rabbit_legs(alphaX * 550, alphaY * 790, alphaX, alphaY, screen)
    rabbit_somethings(x, y, alphaX, alphaY, screen)

    # Подключаем настройки pygame.
    settings(30)


rabbit(0, 0, 1000, 900)
