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

def eye(x, y, alphaX, alphaY):           # FIX
    ellipse(screen, (white, alphaX * x, alphaY * y, alphaX * 20, alphaY * 17), 0)
    ellipse(screen, (black, alphaX * x, alphaY * y, alphaX * 20, alphaY * 17), 1)
    ciclle(screen, (black, alphaX * (x + 10), alphaY * (y + 10), alphaX * 20, alphaY * 17), 0)


def rabbit_head(x, y, alphaX, alphaY, screen):   # FIX
    """
    рисует голову.
    """
    #  Основа головы.
    ellipse(screen, grey, (alphaX * 400, alphaY * 200, alphaX * 200, alphaY * 200), 0)

    # Глаза.
    eye(x, y, alphaX, alphaY)
    eye(x, y, alphaX, alphaY)






def rabbit_body(x, y, alphaX, alphaY, screen): # FIX
    """

    """
    pass


def rabbit_legs(x, y, alphaX, alphaY, screen):  # FIX
    """

    """
    pass


def rabbit_somethings(x, y, alphaX, alphaY, screen):  # FIX
    """


    """
    pass


def rabbit(x, y, width, height):
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
    alphaY = height / 900

    rabbit_head(x, y, alphaX, alphaY, screen)
    ellipse(screen, (183, 0, 9), (630, 620, 64, 58), 0)
    rabbit_body(x, y, alphaX, alphaY, screen)
    rabbit_legs(x, y, alphaX, alphaY, screen)
    rabbit_somethings(x, y, alphaX, alphaY, screen)

    # Подключаем настройки pygame.
    settings(30)


rabbit(2, 434, 1000, 900)
