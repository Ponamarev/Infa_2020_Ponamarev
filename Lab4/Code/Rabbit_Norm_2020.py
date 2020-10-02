import pygame
from pygame.draw import *

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
grey = (128, 128, 128)
black = (0, 0, 0)
white = (255, 255, 255)

def eye(x, y, alphaX, alphaY): # FIX
    ellipse(screen, (grey, alphaX * 400, alphaY * 200, alphaX * 200, alphaY * 200), 0)


def rabbit_head(x, y, alphaX, alphaY):  # FIX
    """
    рисует голову.
    """
    #
    ellipse(screen, (grey, alphaX * 400, alphaY * 200,  alphaX * 200, alphaY * 200), 0)

    #





def rabbit_body(x, y, alphaX, alphaY): # FIX
    """

    """
    pass


def rabbit_legs(x, y, alphaX, alphaY):  # FIX
    """

    """
    pass


def rabbit_somethings(x, y, alphaX, alphaY):  # FIX
    """


    """
    pass


def rabbit(x, y, alphaX, alphaY):
    """
    Рисует кролика.

    x, y - координаты левой нижней точки прямоугольника,
    в который вписан кролик.
    width - ширина прямоугольника.
    height - высота прямоугольника.
    """
    screen = pygame.display.set_mode((width, height))

    # Коэфиценты для расширения линейных размеров по соотв. осям.
    # Они нужны, т к у меня есть возможность самому выбрать размер окна.
    alphaX = width / 1000
    alphaY = height / 2000

    rabbit_head(x, y, alphaX, alphaY)
    rabbit_body(x, y, alphaX, alphaY)
    rabbit_legs(x, y, alphaX, alphaY)
    rabbit_somethings(x, y, alphaX, alphaY)

    # Подключаем настройки pygame.
    settings(30)


rabbit(2, 434, 1000, 2000)