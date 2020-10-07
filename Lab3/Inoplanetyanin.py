import pygame
from pygame.draw import *

pygame.init()

screen = pygame.display.set_mode((800, 1000))
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


def person():
    pass

def background():
    pass


def NLO():
    pass


def Clouds():
    pass


def Exs2_imgN17(x, y, alpha):
    #фон - трава, небо, луна.
    rect(screen, (15, 25, 50), (0, 0, 800, 480), 0)
    rect(screen, (30, 50, 20), (0, 480, 800, 1000), 0)
    circle(screen, (193, 193, 193), (550, 223), 120, 0)

    #  светлые облака. ( нумерация сверху )
    ellipse(screen, (85, 85, 85), (-208, 10, 730, 170), 0)  # 2
    ellipse(screen, (85, 85, 85), (580, -20, 1000, 112), 0) # 1
    ellipse(screen, (85, 85, 85), (-208, 205, 743, 130), 0) # 4
    ellipse(screen, (85, 85, 85), (400, 100, 743, 130), 0)  # 3
    ellipse(screen, (85, 85, 85), (380, 250, 743, 130), 0)  # 5

    # темные облака. ( нумерация сверху )
    ellipse(screen, (55, 55, 55), (150, 70, 730, 100), 0 ) # 1
    ellipse(screen, (55, 55, 55), (150, 330, 730, 95), 0)  # 3
    ellipse(screen, (55, 55, 55), (-370, 170, 730, 110), 0)  # 2

    # Нло.
    # луч захвата.
    polygon(screen, (115, 125, 150), [(160, 380), (110, 480), (210, 480)], 0)
    polygon(screen, (130, 150, 120), [(110, 480), (210, 480), (285, 630), (35, 630)], 0)
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

    # Иночеловечек.
    # левое ухо.
    ellipse(screen, (200, 254, 206), (480, 500, 27, 19), 0)
    ellipse(screen, (200, 254, 206), (487, 514, 28, 13), 0)
    ellipse(screen, (200, 254, 206), (498, 530, 15, 15), 0)
    ellipse(screen, (200, 254, 206), (500, 540, 18, 15), 0)
    # правое ухо
    ellipse(screen, (200, 254, 206), (560, 540, 25, 20), 0)
    ellipse(screen, (200, 254, 206), (572, 530, 10, 11), 0)
    ellipse(screen, (200, 254, 206), (560, 540, 13, 16), 0)
    ellipse(screen, (200, 254, 206), (582, 513, 10, 24), 0)
    ellipse(screen, (200, 254, 206), (590, 500, 25, 20), 0)
    # голова.
    arc(screen, (200, 254, 206), (490, 550, 100, 30), 2 * pi, pi, 5)
    arc(screen, (200, 254, 206), (490, 488, 90, 150), pi , 1.5 * pi, 5)
    arc(screen, (200, 254, 206), (480, 488, 110, 150), 1.5 * pi, 2 * pi, 5)
    ellipse(screen, (200, 254, 206), (490, 550, 100, 30), 0)
    ellipse(screen, (200, 254, 206), (493, 560, 95, 30), 0)
    ellipse(screen, (200, 254, 206), (495, 570, 90, 30), 0)
    ellipse(screen, (200, 254, 206), (497, 580, 85, 30), 0)
    ellipse(screen, (200, 254, 206), (500, 590, 80, 30), 0)
    ellipse(screen, (200, 254, 206), (500, 570, 80, 60), 0)
    ellipse(screen, (200, 254, 206), (510, 605, 50, 30), 0)
    # глаза.
    circle(screen, (0, 0, 0), (520, 580), 12, 0)
    circle(screen, (250, 250, 250), (525, 583), 3, 0)

    circle(screen, (0, 0, 0), (565, 580), 10, 0)
    circle(screen, (250, 250, 250), (568, 582), 3, 0)
    # Тело инотоварища.
    ellipse(screen, (200, 254, 206), (500, 630, 70, 135), 0)
    # рука левая
    ellipse(screen, (200, 254, 206), (486, 645, 28, 26), 0)
    ellipse(screen, (200, 254, 206), (467, 664, 30, 20), 0)
    ellipse(screen, (200, 254, 206), (458, 680, 15, 15), 0)
    # рука правая
    ellipse(screen, (200, 254, 206), (556, 645, 28, 26), 0)
    ellipse(screen, (200, 254, 206), (590, 660, 25, 18), 0)
    ellipse(screen, (200, 254, 206), (617, 664, 32, 19), 0)
    # нога левая
    ellipse(screen, (200, 254, 206), (490, 735, 30, 40), 0)
    ellipse(screen, (200, 254, 206), (485, 765, 25, 35), 0)
    ellipse(screen, (200, 254, 206), (450, 795, 50, 25), 0)
    # нога правая
    ellipse(screen, (200, 254, 206), (550, 735, 30, 40), 0)
    ellipse(screen, (200, 254, 206), (555, 770, 30, 40), 0)
    ellipse(screen, (200, 254, 206), (560, 804, 52, 27), 0)
    # яблоко
    ellipse(screen, (183, 0, 9), (630, 620, 64, 58), 0)
    arc(screen, (0, 0, 0), (657, 610, 45, 60), 0.6 * pi, pi, 2)



Exs2_imgN17(0, 0, 1)
Settings()
