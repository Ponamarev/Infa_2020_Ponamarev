import pygame
from pygame.draw import *
from random import randint
from tkinter import *

pygame.init()  # Инициализация Pygame.
Window = Tk()  # Графический интерпретатор.

FPS = 2
screen = pygame.display.set_mode((1200, 900))
pygame.display.set_caption("Игра")

# Цвета.
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)

# Массив цветов.
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x, y, r = 0, 0, 0  # Не используются.
store = 0          # Текущий счет.
pos_ball = [(0, 0, 0)]  # Массив позиций мячиков.
Store_User = 0     # Рекорд.
log_User = ""      # Введенный логин
pas_User = ""      # Введенный пароль.
num_in_arr = 0     # Номер строки с данными в массиве.
array_of_logs = []  # Массив логинов.
array_of_pass = []  # Массив паролей.
array_of_stores = [] # Массив рекордов.


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
    """
    Обрабатывает клик мышки.

    :param x:  None
    :param y:  None
    :param r:  None
    :return:   None
    """
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
    """
    Настраивает окно регистрации.

    :return:  None
    """
    global Window, login_input, password_input

    Window.title("Регистрация")  # Название окна.
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
    """
    Регистрирует новые данные.

    :return: None
    """
    # global log_User, pas_User

    log_User = "{}".format(login_input.get())  # Берет введенные данные.
    pas_User = "{}".format(password_input.get())  # Берет введенные данные.

    # Добавляем данные в массивы.
    array_of_stores.append('0')
    array_of_pass.append(pas_User)
    array_of_logs.append(log_User)

    # Обновляем данные.
    saver()
    get_logs()


def login():
    """
    Проверяет совпадение введенных данных с записанными.
    В случае отсутствия файла сохранений, создает его.

    :return: None
    """
    global log_User, pas_User

    # Проверим наличие файлов сохранения, если их нет, создадим.
    try:
        get_logs()  # Получает данные из файлов, если они есть.
    finally:
        saver()

    # Достает из строки вводенные данные.
    log_User = "{}".format(login_input.get())
    pas_User = "{}".format(password_input.get())
    # Сравнивает данные и введенную информацию
    searching()


def saver():
    """
    Сохраняет данные в файлы.

    :return: None
    """
    file = open('file_logs.txt', 'w')
    for i in range(len(array_of_logs)):
        if array_of_logs[i] != "":  # Убираем пустые строки.
            file.write(array_of_logs[i] + '\n')  # Сохраняем данные.
    file.close()

    file = open('file_pas.txt', 'w')
    for i in range(len(array_of_pass)):
        if array_of_pass[i] != "":  # Убираем пустые строки.
            file.write(array_of_pass[i] + '\n')  # Сохраняем данные.
    file.close()

    file = open('file_store.txt', 'w')
    for i in range(len(array_of_stores)):
        if array_of_stores[i] != "":  # Убираем пустые строки.
            file.write(array_of_stores[i] + '\n')  # Сохраняем данные.
    file.close()


def get_logs():
    """
    Достаяет данные из файлов.

    :return: None
    """
    global array_of_logs, array_of_pass, array_of_stores  # Массивы с данными.

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
    """
    Проверяет совпадение ввода и какой - либо строки из данных.

    :return: None
    """
    global array_of_logs, array_of_pass, array_of_stores  # Массивы с данными.
    global Store_User, num_in_arr  # Переменные с рекордом и номером строки,
    # в которой лежали данные об пользователе
    print(array_of_logs)  # Диагностический вывод в консоль.

    for num in range(len(array_of_logs)):
        # print(array_of_logs[num], '=', log_User) # Более не используемый диагностический вывод в консоль.
        # print(array_of_pass[num], '=', pas_User)
        # print([log_User, pas_User])

        if str(array_of_logs[num]) == str(log_User + '\n') \
                and array_of_pass[num] == str(pas_User + '\n'):
            Store_User = int(array_of_stores[num])  # Берет из массива данных рекорд.
            num_in_arr = num  # Сохраняет номер строки с данными.
            Window.destroy()  # Убирает окно регистрации.
            main()  # Запускает основную функцию.

            # Далее выполняется после закрытия программы.
            array_of_stores[num_in_arr] = str(Store_User)  # Кладет в массив данных рекорд.
            saver()  # Сохраняет данные.


def get_logs_from_line(line):  # Не используется.
    """
    Выдает часть строки до знака *.

    :param line: Строка, в которой ищется знак.
    :return: str
    """
    number_of_symbol = 0

    for symbol in range(len(line)):
        if line[symbol] == "*":
            number_of_symbol = symbol

    return line[0:number_of_symbol:]


def text_store(store):
    """
    Выводит текущие счет и рекорд.

    :param store:  Текущий счет.
    :return: None
    """
    font = pygame.font.Font(None, 40)  # Задает шрифт.
    text = font.render("РЕКОРД: " + str(Store_User) + "\nСчет: " + str(store), True, (255, 255, 255))
    screen.blit(text, [50, 50])  # Добавляет текст на экран на координатах 50, 50.


def store_check():
    """
    Проверяет, побит ли рекорд.
    Если побит, увеличивает его.

    :return: None
    """
    global Store_User  # Рекорд.

    if store > Store_User:
        Store_User = store


def main():
    """
    Основная функция.

    :return: None
    """
    pygame.display.update()
    clock = pygame.time.Clock()
    finished = False

    while not finished:
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                finished = True

            elif event.type == pygame.MOUSEBUTTONDOWN:

                Click(x, y, r)  # Запускает проверку, нажатия.
                print(pos_ball)  # Диангостический вывод точки нажатия и точки центра шара.
                print(pygame.mouse.get_pos())

            text_store(store)  # Обновляет текущий счет.

        new_ball(x, y, r)
        text_store(store)
        pygame.display.update()
        screen.fill(BLACK)
        text_store(store)
        store_check()


if __name__ == "__main__":

    try:  # Принимает данные из файла. Если его нет, создает файл.
        get_logs()
    except:
        saver()  # Запускается, если файла нет. Т.к. создает файлы.

    indificate()  # Запускает окно регистрации.
    Window.mainloop()  # Открывает это окно.
