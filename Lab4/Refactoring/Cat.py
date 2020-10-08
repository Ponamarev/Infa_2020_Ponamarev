import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((600, 600))


white = (255, 255, 255)
olive = (128, 128, 0)
orange = (255, 140, 0)
silver = (192, 192, 192)
blue = (30, 144, 255)
gold = (255, 215, 0)
khaki = (240, 230, 140)
red = (128, 0, 0)


def backgroung():
    """
    Рисует фон.

    :return: None
    """
    rect(screen, (184, 134, 11), (0, 0, 600, 600))
    rect(screen, (210, 180, 140), (0, 350, 600, 600))


def window(x, y, z):
    """
    Рисует окно на координатах х, у

    :param x:      Коодината х левой грани окна.
    :param y:      Координата у верхней грани окна.
    :param z:      Коэфицент расширения окна.
    :return:       None
    """
    rect(screen, (240, 255, 255), (x, y, 250*z, 250*z))
    rect(screen, (230, 230, 250), (x + 25*z, y + 25*z, 85*z, 85*z))
    rect(screen, (230, 230, 250), (x + 140*z, y + 25*z, 85*z, 85*z))
    rect(screen, (230, 230, 250), (x + 25*z, y + 140*z, 85*z, 85*z))
    rect(screen, (230, 230, 250), (x + 140*z, y + 140*z, 85*z, 85*z))


def cattus(a, b, c, furcolor, eyecolor):
    """
    Рисует котика на координатах a, b

    :param a:        Координата левой грани котика.
    :param b:        Координата верхней грани котика.
    :param c:        Коэфицент увеличения котика.
    :param furcolor: Цвет меха котика.
    :param eyecolor: Цвет глаз котика.
    :return:         None
    """
    # Хвост.
    ellipse(screen, furcolor, (a + 175*c, b + 75*c, 150*c, 30*c))
    ellipse(screen, (0, 0, 0), (a + 175*c, b + 75*c, 150*c, 30*c), 1)

    # Левое ухо.
    polygon(screen, furcolor, [(a, b + 37.5*c), (a + 25*c, b), (a - 12.5*c, b - 25*c)])
    polygon(screen, (0, 0, 0), [(a, b + 37.5*c), (a + 25*c, b), (a - 12.5*c, b - 25*c)], 1)

    polygon(screen, (250, 128, 114), [(a, b + 37.5*c), (a + 25*c, b), (a - 6.25*c, b - 12.5*c)])
    polygon(screen, (0, 0, 0), [(a, b + 37.5*c), (a + 25*c, b), (a - 6.25*c, b - 12.5*c)], 1)

    # Правое ухо.
    polygon(screen, furcolor, [(a + 50*c, b + 37.5*c), (a + 25*c, b), (a + 62.5*c, b - 25*c)])
    polygon(screen, (0, 0, 0), [(a + 50*c, b + 37.5*c), (a + 25*c, b), (a + 62.5*c, b - 25*c)], 1)

    polygon(screen, (250, 128, 114), [(a + 50*c, b + 37.5*c), (a + 25*c, b), (a + 56.25*c, b - 12.5*c)])
    polygon(screen, (0, 0, 0), [(a + 50*c, b + 37.5*c), (a + 25*c, b), (a + 56.25*c, b - 12.5*c)], 1)

    # Тело.
    ellipse(screen, furcolor,  (a, b, 200*c, 100*c))
    ellipse(screen, (0, 0, 0), (a, b, 200*c, 100*c), 1)
    # Мордочка.

    ellipse(screen, furcolor,  (a - 12.5*c, b - 12.5*c, 75*c, 75*c))
    ellipse(screen, (0, 0, 0), (a - 12.5*c, b - 12.5*c, 75*c, 75*c), 1)

    # Лапки.
    ellipse(screen, furcolor,  (a - 12.5*c, b + 75*c,   75*c, 25*c))
    ellipse(screen, (0, 0, 0), (a - 12.5*c, b + 75*c,   75*c, 25*c), 1)
    ellipse(screen, furcolor,  (a + 125*c,  b + 25*c,   75*c, 75*c))
    ellipse(screen, (0, 0, 0), (a + 125*c,  b + 25*c,   75*c, 75*c), 1)
    ellipse(screen, furcolor,  (a + 100*c,  b + 75*c,   75*c, 25*c))
    ellipse(screen, (0, 0, 0), (a + 100*c,  b + 75*c,   75*c, 25*c), 1)

    # Глаза.
    ellipse(screen, eyecolor, (a - 6.25*c, b + 18.75*c, 25*c, 12.5*c))
    ellipse(screen, (0, 0, 0), (a - 6.25*c, b + 18.75*c, 25*c, 12.5*c), 1)
    ellipse(screen, (0, 0, 0), (a, b + 18.75*c, 12.5*c, 12.5*c))
    ellipse(screen, (255, 255, 255), (a + 3.125*c, b + 18.75*c, 6.25*c, 6.25*c))

    ellipse(screen, eyecolor, (a + 31.75*c, b + 18.75*c, 25*c, 12.5*c))
    ellipse(screen, (0, 0, 0), (a + 31.75*c, b + 18.75*c, 25*c, 12.5*c), 1)
    ellipse(screen, (0, 0, 0), (a + 37.5*c, b + 18.75*c, 12.5*c, 12.5*c))
    ellipse(screen, (225, 255, 255), (a + 40.625*c, b + 18.75*c, 6.25*c, 6.25*c))

    # Нос.
    polygon(screen, (250, 128, 114), [(a + 18.75*c, b + 34.375*c),
                                      (a + 31.25*c, b + 34.375*c),
                                      (a + 25*c,    b + 40.625*c)])
    polygon(screen, (0, 0, 0), [(a + 18.75*c, b + 34.375*c),
                                (a + 31.25*c, b + 34.375*c),
                                (a + 25*c,    b + 40.625*c)], 1)
    line(screen, (0, 0, 0), (a + 25*c, b + 46.875*c), (a + 25*c, b + 40.625*c), 1)

    # Рот.
    arc(screen, (0, 0, 0), (a + 12.8*c, b + 40.625*c, 12.5*c, 12.5*c), -1.57, 0)
    arc(screen, (0, 0, 0), (a + 6.25*c, b + 34.375*c, 25*c, 25*c), 1.57, 3.14)
    arc(screen, (0, 0, 0), (a, b + 34.375*c, 37.5*c, 37.5*c), 1.57, 3.14)
    arc(screen, (0, 0, 0), (a - 6.25*c, b + 34.375*c, 50*c, 50*c), 1.57, 3.14)

    arc(screen, (0, 0, 0), (a + 25*c, b + 40.625*c, 12.5*c, 12.5*c), 3.14, 4.71)
    arc(screen, (0, 0, 0), (a + 18.75*c, b + 34.375*c, 25*c, 25*c), 0, 1.57)
    arc(screen, (0, 0, 0), (a + 12.5*c, b + 34.375*c, 37.5*c, 37.5*c), 0, 1.57)
    arc(screen, (0, 0, 0), (a + 6.25*c, b + 34.375*c, 50*c, 50*c), 0, 1.57)


def ball(m, n, k, ballcolor):
    """
    Рисует клубок шерсти на кооридинатах m, n

    :param m:         Координата левой грани клубка
    :param n:         Координата верхней грани клубка
    :param k:         Коэфицент увелечения клубка
    :param ballcolor: Цвет клубка
    :return:          None
    """
    ellipse(screen, ballcolor, (m, n, 50*k, 50*k))
    ellipse(screen, (0, 0, 0), (m, n, 50*k, 50*k), 1)
    line(screen, (0, 0, 0), (m + 20*k, n + 5*k), (m + 40*k, n + 20*k), 1)
    line(screen, (0, 0, 0), (m + 15*k, n + 10*k), (m + 45*k, n + 25*k), 1)
    line(screen, (0, 0, 0), (m + 5*k, n + 20*k), (m + 35*k, n + 35*k), 1)
    line(screen, (0, 0, 0), (m + 10*k, n + 35*k), (m + 35*k, n + 40*k), 1)


backgroung()
window(0, 50, 1)
window(350, 50, 1)
cattus(100, 250, 1.5, white, olive)
cattus(200, 500, 0.7, silver, blue)
ball(50, 500, 1, gold)
ball(450, 400, 0.75, khaki)

pygame.display.update()
cat = pygame.time.Clock()
finished = False

while not finished:
    cat.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
