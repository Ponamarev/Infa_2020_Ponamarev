import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

FPS = 30

'''  тренировочный код.
FPS = 30
screen = pygame.display.set_mode((400, 400))

rect(screen, (255, 0, 255), (100, 100, 200, 200))
rect(screen, (0, 0, 255), (100, 100, 200, 200), 3)
polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
circle(screen, (0, 255, 0), (200, 175), 50)
circle(screen, (255, 255, 255), (200, 175), 50, 5)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
'''  # Тренировка 1.

def Smile():     # Упражение номер 1
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


Smile()

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True


pygame.quit()