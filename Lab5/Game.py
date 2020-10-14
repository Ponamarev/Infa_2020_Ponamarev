import pygame
from pygame.draw import *
from random import randint
from tkinter import *

pygame.init()  # Инициализация Pygame.
Window = Tk()  # Графический интерпретатор.

FPS = 2
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Игра")

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
pos_ball = [(0, 0, 0)]
Store_User = 0
log_User = ""
pas_User = ""
num_in_arr = 0
array_of_logs = []
array_of_pass = []
array_of_stores = []

def new_ball(x, y, r):
    '''рисует новый шарик '''
    global pos_ball
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    pos_ball = [(x, y, r)]
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def triggered():
    """
    Добавляет очки.
    :return: None
    """
    global store, r
    print(pos_ball)
    if pos_ball[0][2] < 20:
        store += 10
    elif pos_ball[0][2] < 50:
        store += 5
    else:
        store += 3


def mistake():
    """
    снимает очки
    :return: None
    """
    global store
    if pos_ball[0][2] < 30:
        store -= 1
    else:
        store -= pos_ball[0][2] // 10


def Click(x, y, r):
    global store
    pos = pygame.mouse.get_pos()
    if (pos[0] - pos_ball[0][0]) ** 2 + (pos[1] - pos_ball[0][1]) ** 2 <= pos_ball[0][2] ** 2:
        triggered()
    else:
        mistake()


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


def indificate():
    global Window, login_input, password_input

    Window.title("Управление")  # Название окна.
    Window.geometry("700x450")  # Размер окна.

    # Текст для окна.
    Learn_text(Window, "Вход:", 0, 0, 1)
    Learn_text(Window, "Логин:", 1, 1, 1)
    Learn_text(Window, "Пароль:", 1, 2, 1)

    # Окна для ввода данных.
    login_input = Entry(Window, width=10)  # Ввод логина.
    login_input.grid(column=2, row=1)

    password_input = Entry(Window, width=10)  # Ввод пароля.
    password_input.grid(column=2, row=2)

    # Кнопки для приема данных.
    btn1 = Button(Window, text="Зарегистрироваться", command=logup)
    btn1.grid(column=4, row=4)

    btn1 = Button(Window, text="Войти", command=login)
    btn1.grid(column=4, row=3)


def logup():
    global password_input, login_input
    global log_User, pas_User

    log_User = "{}".format(login_input.get())
    pas_User = "{}".format(password_input.get())
    array_of_stores.append('0')
    array_of_pass.append(pas_User)
    array_of_logs.append(log_User)
    saver()


def login():
    global password_input, login_input
    global log_User, pas_User

    get_logs()
    log_User = "{}".format(login_input.get())
    pas_User = "{}".format(password_input.get())
    searching()


def saver():
    file = open('file_logs.txt', 'w')
    for i in range(len(array_of_logs)):
        file.write(array_of_logs[i] + '\n')
    file.close()

    file = open('file_pas.txt', 'w')
    for i in range(len(array_of_pass)):
        file.write(array_of_pass[i] + '\n')
    file.close()

    file = open('file_store.txt', 'w')
    for i in range(len(array_of_stores)):
        file.write(array_of_stores[i] + '\n')
    file.close()


def get_logs():
    global array_of_logs, array_of_pass, array_of_stores

    file = open('file_logs.txt', 'r')
    array_of_logs = file.readlines()
    file.close()

    file = open('file_pas.txt', 'r')
    array_of_pass = file.readlines()
    file.close()

    file = open('file_store.txt', 'r')
    array_of_stores = file.readlines()
    file.close()


def searching():
    global array_of_logs, array_of_pass, array_of_stores
    global Store_User, num_in_arr
    print(array_of_logs)

    for num in range(len(array_of_logs)):
        # print(array_of_logs[num], '=', log_User)
        # print(array_of_pass[num], '=', pas_User)
        # print([log_User, pas_User])
        if str(array_of_logs[num]) == str(log_User + '\n') and array_of_pass[num] == str(pas_User + '\n'):
            Store_User = int(array_of_stores[num])
            num_in_arr = num
            Window.destroy()
            main()
            array_of_stores[num_in_arr] = str(Store_User)
            saver()


def get_logs_from_line(line):
    number_of_symbol = 0

    for symbol in range(len(line)):
        if line[symbol] == "*":
            number_of_symbol = symbol

    return line[0:number_of_symbol:]


def text_store(store):
    font = pygame.font.Font(None, 40)
    text = font.render("РЕКОРД: " + str(Store_User) + "\nСчет: " + str(store), True, (255, 255, 255))
    screen.blit(text, [50, 50])


def store_check():
    global Store_User
    if store > Store_User:
        Store_User = store


def main():
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
        store_check()


if __name__ == "__main__":
    get_logs()
    indificate()
    Window.mainloop()
