это
Лабораторная работа номер 4

import pygame
from pygame.draw import *
from random import randint

pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("ТЫКАЛКА!!!!!!!!!!!")

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x, y, r = 0, 0, 0
store = 0


def new_ball(x, y, r):
    '''рисует новый шарик '''
    global x, y, r
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def triggered():
    """
    Добавляет очки.
    :return: None
    """
    global store
    if r < 10:
        store += 5
    elif r < 20:
        store += 3
    else:
        store += 1


def mistake():
    """
    снимает очки
    :return: None
    """
    global store
    if r < 20:
        store -= 1
    else:
        store -= 3


def Click():
    global store
    pos = pygame.mouse.get_pos()
    if pos[0] ** 2 + pos[1] ** 2 <= r ** 2:
        triggered()
    else:
        mistake()


def text_store():
    global store
    font = pygame.font.Font(None, 40)
    text = font.render("РЕКОРД: " + str(store), True, (255, 255, 255))
    screen.blit(text, [50, 50])


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Click()
            text_store()

    new_ball()
    text_store()
    pygame.display.update()
    screen.fill(BLACK)
    text_store(store)

pygame.quit()










import pygame
from pygame.draw import *
from random import randint
pygame.init()

FPS = 2
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("ТЫКАЛКА!!!!!!!!!!!")

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x, y, r = 0, 0, 0
store = 0
pos_ball = [0, 0, 0]
def new_ball(x, y, r):
    '''рисует новый шарик '''
    global pos_ball
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    pos_bal = [x, y, r]
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def triggered(store):
    """
    Добавляет очки.
    :return: None
    """
    if r < 10:
        store += 5
    elif r < 20:
        store += 3
    else:
        store += 1


def mistake(store):
    """
    снимает очки
    :return: None
    """
    if r < 20:
        store -= 1
    else:
        store -= 3



def Click(x, y, r):
    global store
    pos = pygame.mouse.get_pos()
    if (pos[0] - x)**2 + (pos[1] -y)**2 <= r**2:
        triggered(store)
    else:
        mistake(store)

         
def text_store(store):
    font = pygame.font.Font(None, 40)
    text = font.render("РЕКОРД: " + str(store), True, (255, 255, 255))
    screen.blit(text, [50, 50])
           
            
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            Click(x, y, r)
            print(pos_ball)
            print(pygame.mouse.get_pos())
        text_store(store)

    new_ball(x, y, r)
    text_store(store)
    pygame.display.update()
    screen.fill(BLACK)
    text_store(store)


pygame.quit()
