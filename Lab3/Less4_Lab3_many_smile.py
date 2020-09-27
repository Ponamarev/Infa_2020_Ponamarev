import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

FPS = 30
pi = 3.14159


def Settings():
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True



def Smile1():
    # фон.
    rect(screen, (130, 25, 250), (0, 0, 400, 400), 0)
    # Шляпа
    polygon(screen, (0, 0, 0), [(100,100), (200,50),
                    (300,100), (100,100)], 0)
    # основа смайлика.
    circle(screen, (255, 226, 1), (200, 175), 100, 0)
    circle(screen, (0, 0, 0), (200, 175), 102, 2)
    rect(screen, (10, 0, 0), (160, 220, 70, 20), 0)
    # правый глаз.
    circle(screen, (250, 3, 0), (240, 150), 25, 0)
    circle(screen, (0, 3, 0), (240, 150), 25, 3)
    circle(screen, (0, 3, 0), (240, 150), 8, 0)
    polygon(screen, (0, 0, 0), [(210, 140), (250,110)], 5)
    # левый глаз.
    circle(screen, (250, 3, 0), (160, 150), 15, 0)
    circle(screen, (0, 3, 0), (160, 150), 15, 3)
    circle(screen, (0, 3, 0), (160, 150), 2, 0)
    polygon(screen, (0, 0, 0), [(170, 140), (120, 110)], 5)


def Smile2():
    # фон.
    rect(screen, (130, 40, 50), (400, 0, 800, 400), 0)

    # основа смайлика.
    circle(screen, (255, 226, 1), (600, 175), 100, 0)
    circle(screen, (0, 0, 0), (600, 175), 102, 2)
    rect(screen, (10, 0, 0), (570, 220, 70, 10), 0)

    # правый глаз.
    circle(screen, (250, 230, 200), (640, 150), 20, 0)
    circle(screen, (0, 3, 0), (640, 150), 20, 1)
    circle(screen, (0, 3, 0), (640, 150), 8, 0)
    polygon(screen, (0, 0, 0), [(630, 110), (670, 140)], 5)

    # левый глаз.
    circle(screen, (250, 230, 200), (560, 150), 20, 0)
    circle(screen, (0, 3, 0), (560, 150), 20, 1)
    circle(screen, (0, 3, 0), (560, 150), 8, 0)
    polygon(screen, (0, 0, 0), [(575, 110), (530, 140)], 5)


def Smile3():
    # фон.
    rect(screen, (50, 140, 50), (800, 0, 1200, 400), 0)

    # основа смайлика.
    circle(screen, (255, 226, 1), (1000, 175), 100, 0)
    circle(screen, (0, 0, 0), (1000, 175), 102, 2)

    # Улыбка
    arc(screen, (0, 0, 0), (970, 220, 70, 20), pi, 2.1 * pi, 10)
    arc(screen, (0, 0, 0), (972, 223, 70, 20), pi, 2.1 * pi, 10)
    arc(screen, (0, 0, 0), (971, 221, 70, 20), pi, 2.1 * pi, 10)

    # нос.
    ellipse(screen, (0, 0, 9), (990, 178, 20, 10), 0)

    # правый глаз.
    circle(screen, (250, 230, 200), (1040, 150), 21, 0)
    circle(screen, (0, 3, 0), (1040, 150), 21, 1)
    circle(screen, (0, 3, 0), (1040, 150), 8, 0)
    polygon(screen, (0, 0, 0), [(1020, 120), (1070, 130)], 5)

    # левый глаз.
    circle(screen, (250, 230, 200), (960, 150), 21, 0)
    circle(screen, (0, 3, 0), (960, 150), 21, 1)
    circle(screen, (0, 3, 0), (960, 150), 8, 0)
    polygon(screen, (0, 0, 0), [(975, 120), (930, 130)], 5)


Smile1()
Smile2()
Smile3()
Settings()
