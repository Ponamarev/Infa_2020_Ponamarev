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


grey = (128, 128, 128)


def rabbit_head(x, y, width, height):
    """
    рисует голову.
    """
    ellipse(screen, (grey, width, height, 100, 200), 0)
    pass


def rabbit_body(x, y, width, height):
    """

    """
    pass


def rabbit_legs(x, y, width, height):
    """

    """
    pass


def rabbit_somethings(x, y, width, height):
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

    rabbit_head(x, y, width, height)
    rabbit_body(x, y, width, height)
    rabbit_legs(x, y, width, height)
    rabbit_somethings(x, y, width, height)

    # Подключаем настройки pygame.
    settings(30)


rabbit(2, 434, 334, 434)