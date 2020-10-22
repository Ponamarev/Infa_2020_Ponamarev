import pygame
from pygame.draw import *
from random import *
import math

from tkinter import *

pygame.init()  # Инициализация Pygame.
Window = Tk()  # Графический интерпретатор.

# Зададим поверхность для рисования ракеты.
screen_Rocket = pygame.Surface((90, 320))
screen_Rocket.set_colorkey((0, 0, 0, 0))
screen_Rocket.set_alpha(255)


FPS = 30
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
White = (250, 255, 255)
White1 = (250, 255, 255)

# Массив цветов.
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

x, y, r = 0, 0, 0  # Не используются.
store = 0  # Текущий счет.
pos_ball = [(0, 0, 0)]  # Массив позиций мячиков.
Store_User = 0  # Рекорд.
log_User = ""  # Введенный логин
pas_User = ""  # Введенный пароль.
num_in_arr = 0  # Номер строки с данными в массиве.
array_of_logs = []  # Массив логинов.
array_of_pass = []  # Массив паролей.
array_of_stores = []  # Массив рекордов.
Health = 255  # Здоровье корабля ( Принимает значения от 0 до 255).
Space_load = 0  # Очки возмножности использовать функцию.
frame = 0
is_rocket_on = 0 # Нужна, чтобы проверять, можно ли спавнить шарики.
is_rocketE_on = 0 # Нужна, чтобы проверять, можно ли спавнить шарики.
is_ball_black = 0 # Нужна, чтобы проверять, рисовать ли шарик, после стирания.
defeat = 0 # Урон, от ракеты.
power_of_notEnemy_rocket = 0 # Сила ракеты.
x_rocketE = 0 # Координата ракеты.
y_rocketE = 0 # Координата ракеты.
ancleE = 180  # Угол наклона ракеты.
x_rocket = 0 # Координата ракеты.
y_rocket = 0 # Координата ракеты.
ancle = 0    # Угол наклона ракеты.
max_num_of_balls_colour = 5 # Нужно, чтобы менять цвета шариков.



def new_ball(x, y, r):
    '''рисует новый шарик '''
    global pos_ball
    x = randint(100, 1100)
    y = randint(300, 600)
    r = randint(10, 100)
    pos_ball = [(x, y, r)]
    color = COLORS[randint(0, max_num_of_balls_colour)]
    circle(screen, color, (x, y), r)


def triggered():
    """
    Добавляет очки.
    :return: None
    """
    global store, r, Space_load, power_of_notEnemy_rocket, defeat
    print(pos_ball) # Диагностика.
    # Если попали по мячику, то увеличим счет.
    if is_rocket_on == 0 and is_rocketE_on == 0:
        if pos_ball[0][2] < 20:
            store += 10

        elif pos_ball[0][2] < 50:
            store += 5

        else:
            store += 3

        Space_load += 200 // pos_ball[0][2]

    # Если летит ракета, то увеличим ее силу.
    elif is_rocket_on == 1:
        if Space_load >= 3:
            power_of_notEnemy_rocket += 10
            Space_load -= 3

    # Если летит ракета enemy, то уменьшим defeat.
    elif is_rocketE_on == 1:
        # defeat больше или равен нулю.
        if defeat >= 5 and Space_load >= 3:
            defeat -= 5
            Space_load -= 3


def mistake():
    """
    снимает очки
    :return: None
    """
    global store, Health
    if pos_ball[0][2] < 30:
        store -= 1
    else:
        store -= pos_ball[0][2] // 10
        Health -= 5


def Click(x, y, r):
    """
    Обрабатывает клик мышки.
    :param x:  None
    :param y:  None
    :param r:  None
    :return:   None
    """
    global store, x_rocketE, x_rocket, y_rocketE, y_rocket, ancle, ancleE
    pos = pygame.mouse.get_pos()
    # До полета ракет.
    if is_rocket_on == 0 and is_rocketE_on == 0:
        if (pos[0] - pos_ball[0][0]) ** 2 + (pos[1] - pos_ball[0][1]) ** 2 <= pos_ball[0][2] ** 2:
            triggered()
        else:
            mistake()

    # Если летят ракеты, то нужно проверить попадание по ним мышкой.
    elif    x_rocket - 50 * math.sin(3.14 / 180 * ancle) - 90 <= pos[0] <= x_rocket + 50 * math.sin(3.14 / 180 * ancle)  \
        and y_rocket - 50 * math.cos(3.14 / 180 * ancle) - 90 <= pos[1] <= y_rocket + 50 * math.cos(3.14 / 180 * ancle) :
        triggered()

    elif    x_rocketE + 120 * math.sin(3.14 / 180 * ancleE) - 10 <= pos[0] <= x_rocketE + 225 * math.sin(3.14 / 180 * ancleE) + 30\
        and y_rocketE - 20 * math.cos(3.14 / 180 * ancleE) - 40 <= pos[1] <= y_rocketE - 260 * math.cos(3.14 / 180 * ancleE) - 20:
        triggered()
    # Диагностический вывод.
    print(defeat)
    print(x_rocketE - 120 * math.sin(3.14 / 180 * ancleE) - 10, x_rocketE - 225 * math.sin(3.14 / 180 * ancleE) + 30)
    print(y_rocketE - 90 * math.cos(3.14 / 180 * ancleE) - 40, y_rocketE - 180 * math.cos(3.14 / 180 * ancleE) - 20)


def enemy_click():
    """
    Нажимает на кружки и ракеты.
    :return: None
    """
    global store, power_of_notEnemy_rocket, defeat
    # Он может также нажимать на шарики.
    if randint(1, 1000) == 1:
        store -= pos_ball[0][2]

    # Может нажиматьна ракету.
    if is_rocket_on == 1:
        if randint(1, 50) == 1:
            power_of_notEnemy_rocket -= randint(1, 20)

    # И на свою тоже)))
    if is_rocketE_on == 1:
        if randint(1, 50) == 1:
            defeat += randint(1, 20)


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


def BAX1():
    """
    включит звук.
    :return:  None
    """
    pygame.mixer.music.load("выстрел 1.mp3")
    pygame.mixer.music.play()


def BAX2():
    """
    включит звук.
    :return:  None
    """
    pygame.mixer.music.load("выстрел 2.mp3")
    pygame.mixer.music.play()


def BAXMANY():
    """
    включит звук.
    :return:  None
    """
    pygame.mixer.music.load("выстрел много.mp3")
    pygame.mixer.music.play()


def USSR():
    """
    включит звук.
    :return:  None
    """
    pygame.mixer.music.load("Гимн СССР.mp3")
    pygame.mixer.music.play()


def CLac_clik():
    """
    включит звук.
    :return:  None
    """
    if randint(1,2) == 1:
        pygame.mixer.music.load("камера клац.mp3")
        pygame.mixer.music.play()
    else:
        pygame.mixer.music.load("камера клик.mp3")
        pygame.mixer.music.play()


def RocketStart__():
    """
    включит звук.
    :return:  None
    """
    pygame.mixer.music.load("старт ракеты.mp3")
    pygame.mixer.music.play()


def RocketStart_():
    """
    включит звук.
    :return:  None
    """
    pygame.mixer.music.load("запуск ракеты.mp3")
    pygame.mixer.music.play()


def atackSound():
    """
    включит звук.
    :return:  None
    """
    pygame.mixer.music.load("Сирена1.mp3")
    pygame.mixer.music.play()


def artSound():
    """
    включит звук.
    :return:  None
    """
    pygame.mixer.music.load("артилерия.mp3")
    pygame.mixer.music.play()


def enemy_rocket_start():
    """
    Запускает ракету.
    :return:
    """
    global x_rocketE, y_rocketE, ancleE, is_rocketE_on
    atackSound()
    x_rocketE = 100
    y_rocketE = 200
    ancleE  = 180
    is_rocketE_on = 1
    Rocket_print(x_rocketE, y_rocketE, 0.4, ancleE)


def enemy_rocket_check():
    """
    Передвигает ракету, отвечает за ее функции.
    :return:  None
    """
    global x_rocketE, y_rocketE, ancleE, Health, is_rocketE_on, frame, defeat
    if is_rocketE_on == 2:
        enemy_rocket_start() # Инициализация ракеты.

    elif is_rocketE_on == 1:
        # Движение ракеты.
        if y_rocketE < 860:
            y_rocketE += 5

        # Поворот ракеты.
        elif ancleE < 270:
            x_rocketE += 5 * math.cos(3.14 / 180 * ancleE)
            y_rocketE += 5 * math.sin(3.14 / 180 * ancleE)
            ancleE += 2.5

        # Движение ракеты.
        elif x_rocketE <= 500:
            x_rocketE += 5

        else:
            artSound()  # звук попадания.
            is_rocketE_on = 0   # выключение ракеты.
            Health -= defeat    # Нанесем урон от попадания.
            defeat = 0    # Обнулим урон до следующего запуска ракеты.
            frame = 0   # Запускает появление шаров.

        Rocket_print(x_rocketE, y_rocketE, 0.4, ancleE)


def start_notEnemy_rocket():
    """
    Запускает ракету.
    :return:
    """
    global x_rocket, y_rocket, ancle, is_rocket_on

    if max_num_of_balls_colour != 0: # Не перебивает гимн СССР.
        RocketStart__()
    # Зададим начальные параметры ракеты.
    x_rocket = 900
    y_rocket = 700
    ancle  = 0
    is_rocket_on = 1
    # Нарисуем ракету.
    Rocket_print(x_rocket, y_rocket, 0.4, ancle)


def notEnemy_rocket_check():
    """
    Передвигает ракету.
    :return:  None
    """
    global x_rocket, y_rocket, ancle, Health, is_rocket_on, store, frame, power_of_notEnemy_rocket
    if is_rocket_on == 2:
        start_notEnemy_rocket() # Инициализация ракеты.

    elif is_rocket_on == 1:
        if y_rocket > 300:
            y_rocket -= 5

        elif ancle < 90:
            x_rocket -= 5 * math.cos(3.14 / 180 * ancle)
            y_rocket -= 5 * math.sin(3.14 / 180 * ancle)
            ancle += 2.5

        elif x_rocket >= 470:
            x_rocket -= 5

        else:
            is_rocket_on = 0   # выключение ракеты.
            artSound()          # звук попадания.
            if max_num_of_balls_colour == 0: # Возращает гимн СССР.
                USSR()
            store += power_of_notEnemy_rocket    # Нанесем урон от попадания.
            frame = 0  # Запускает появление шаров.
            power_of_notEnemy_rocket = 0    # Обнулим урон до следующего запуска ракеты.

        # Рисуем ракету
        Rocket_print(x_rocket, y_rocket, 0.4, ancle)


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
        if array_of_logs[i] != "" + '\n':  # Убираем пустые строки.
            file.write(array_of_logs[i] + '\n')  # Сохраняем данные.
    file.close()

    file = open('file_pas.txt', 'w')
    for i in range(len(array_of_pass)):
        if array_of_pass[i] != "" + '\n':  # Убираем пустые строки.
            file.write(array_of_pass[i] + '\n')  # Сохраняем данные.
    file.close()

    file = open('file_store.txt', 'w')
    for i in range(len(array_of_stores)):
        if array_of_stores[i] != "" + '\n':  # Убираем пустые строки.
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


def Space_print():
    """
    Рисует шкалу, показывающую накопленную силу удара.

    :return: None
    """
    rect(screen, (240, 185, 12), (800, 76, Space_load, 30), 0)


def Space_work_print():
    """
    Рисует эффекты, сигнализирующие о готовности запуска ракеты.

    :return: None
    """
    if Space_load > 50:
        for i in range(randint(Space_load // 5, Space_load // 3)):
            ellipse(screen, White, (randint(800, 1200), randint(50, 100), 20, 15), 2)


def Health_print():
    """
    Рисует шкалу здоровья.

    :return: None
    """
    rect(screen, (255 - Health, 0 + Health, 12), (500, 76, Health, 30), 0)


def Rocket_print(x_rocket, y_rocket, alpha, ancle):
    """
    Рисует ракету на нужных координатах, повернутую влево на указанный угол ancle,
    размера, отличающегося от (90,320), в alpha раз

    :param x_rocket: координаты центра ракеты
    :param y_rocket: координаты центра ракеты
    :param alpha:    коэфицент расширения
    :param ancle:    угол поворота влево
    :return:         None
    """
    # Создаем поверхность для ракеты.
    screen_Rocket = pygame.Surface((45, 180))
    screen_Rocket.set_colorkey((0, 0, 0, 0))
    screen_Rocket.set_alpha(255)

    # Создаем поверхность, которую будем поворачивать.
    screen_Rocket_rotate = pygame.Surface((45, 180))
    screen_Rocket_rotate.set_colorkey((0, 0, 0, 0))
    screen_Rocket_rotate.set_alpha(255)

    # Фюзеляж.
    rect(screen_Rocket, (136, 127, 130), (10 * alpha, 110 * alpha, 70 * alpha, 240 * alpha), 0)

    # Стабилизаторы.
    polygon(screen_Rocket, (250, 127, 130), [(80 * alpha, 231 * alpha),
                                             (80 * alpha, 310 * alpha),
                                             (90 * alpha, 320 * alpha),
                                             (90 * alpha, 300 * alpha)], 0)
    polygon(screen_Rocket, (250, 127, 130), [(10 * alpha, 231 * alpha),
                                             (10 * alpha, 310 * alpha),
                                             (0, 320 * alpha),
                                             (0, 300 * alpha)], 0)
    polygon(screen_Rocket, (250, 127, 130), [(45 * alpha, 231 * alpha),
                                             (40 * alpha, 320 * alpha),
                                             (50 * alpha, 320 * alpha)], 0)

    # Носовой обтекатель.
    polygon(screen_Rocket, (250, 127, 130), [(5 * alpha, 110 * alpha),
                                             (85 * alpha, 110 * alpha),
                                             (80 * alpha, 105 * alpha),
                                             (45 * alpha, 0),
                                             (10 * alpha, 105 * alpha)], 0)
    # Эффект работы РЖД.
    left_fire = randint(1, 3)
    right_fire = randint(1, 3)

    # Боковые струи пламени.
    polygon(screen_Rocket, (226 ,88, 34), [(15 * alpha, 350 * alpha),
                                             (75 * alpha, 350 * alpha),
                                             ((10 * right_fire + 35) * alpha, (17 * right_fire + 350) * alpha),
                                             (45 * alpha, 350 * alpha),
                                             ((15 - left_fire * 3) * alpha,  (17 * left_fire  + 350) * alpha)], 0)
    # Центральный огонь.
    polygon(screen_Rocket, (226, 113, 34), [(15 * alpha, 350 * alpha),
                                            ((45 + 1 * (left_fire - right_fire)) * alpha,
                                            160 + 1 * math.fabs(left_fire - right_fire)),
                                            (75 * alpha, 350 * alpha)], 0)

    # Линия, проходящая через центр ракеты, проверяем точность поворота.
    # polygon(screen_Rocket, (0, 0, 130), [(0, 0), (90, 320)], 10)

    # Добавляем ракету на поверхность, которую будем поворачивать.
    screen_Rocket_rotate = pygame.transform.rotate(screen_Rocket, ancle)
    screen.blit(screen_Rocket_rotate, (x_rocket - 45 * alpha  - 60 * (math.sin(3.14159 / 180 * ancle)),
                                       y_rocket - 120 * alpha - 45 * (math.cos(3.14159 / 180 * ancle))))


def NLO_print(x, y, NEW, Alpha, White):
    """
    рисует НЛО.
    x, y       коодринаты верхней и левой граней НЛО.
    NEW -      непрозраность.
    Alpha -    коэфицент расширения.
    :return:   None
    """
    # Подключаем альфа канал.
    screen2 = pygame.Surface((800, 1000))
    screen1 = pygame.Surface((800, 1000))
    screen1.set_colorkey((0, 0, 0, 0))
    screen1.set_alpha(255)
    screen2.set_colorkey((0, 0, 0, 0))
    screen2.set_alpha(255)

    # Нло.
    # тело.
    ellipse(screen1, (150, 150, 150), (Alpha * 10, Alpha * 355, Alpha * 300, Alpha * 90), 0)
    ellipse(screen1, (180, 180, 180), (Alpha * 55, Alpha * 346, Alpha * 205, Alpha * 60), 0)

    # Фары.
    ellipse(screen1, White, (Alpha * 20, Alpha * 390, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 50, Alpha * 410, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 90, Alpha * 417, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 135, Alpha * 420, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 180, Alpha * 419, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 225, Alpha * 410, Alpha * 30, Alpha * 15), 0)
    ellipse(screen1, White, (Alpha * 260, Alpha * 395, Alpha * 30, Alpha * 15), 0)

    screen1.set_alpha(NEW)
    screen.blit(screen1, (((0 + x) / Alpha), ((-350 + y) / Alpha)))


def text_store(store):
    """
    Выводит текущие счет и рекорд.
    :param store:  Текущий счет.
    :return: None
    """
    font = pygame.font.Font(None, 30)  # Задает шрифт.
    text = font.render("РЕКОРД: " + str(Store_User) + "\nСчет: " + str(store), True, (255, 255, 255))
    screen.blit(text, [50, 50])  # Добавляет текст на экран на координатах 50, 50.


def Text_print(tekst, x):
    """
    Выводит текст, начало которого находится на координате х.

    tekst - сам текст.
    х   -   координата х.
    """
    font = pygame.font.Font(None, 40)  # Задает шрифт.
    text = font.render(tekst, True, (255, 255, 255))
    screen.blit(text, [x, 50])


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
    global frame, Space_load, is_rocket_on, is_rocketE_on, max_num_of_balls_colour, White1, Space_load
    Rocket_chanse = 5000

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

            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                if Space_load > 50:
                    is_rocket_on = 2
                    Space_load -= 50

            # Включить гимн СССР.
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_s:
                USSR()
                Rocket_chanse = 1000
                max_num_of_balls_colour = 0
                Space_load += 100
                White1 = RED

            text_store(store)  # Обновляет текущий счет.

        text_store(store)
        pygame.display.update()
        screen.fill(BLACK)
        text_store(store)
        NLO_print(100, -300, 255, 1.5, White)
        NLO_print(900, 700, 255, 1.5, White1)
        Space_work_print()
        Health_print()
        Space_print()
        Text_print("Здоровье", 500)
        Text_print("Удар (Пробел)", 800)
        store_check()

        # Примерно раз в минуту enemy тоже умеет пускать ракету.
        if randint(1, Rocket_chanse) == 1:
            is_rocketE_on = 2

        enemy_click()  # Проверка клика enemy.
        # Проверка ракет.
        notEnemy_rocket_check()
        enemy_rocket_check()

        frame += 1

        if frame == 30 and is_rocket_on == 0 and is_rocketE_on  == 0:
            new_ball(x, y, r)
            frame = 0


if __name__ == "__main__":

    try:  # Принимает данные из файла. Если его нет, создает файл.
        get_logs()
    except:
        saver()  # Запускается, если файла нет. Т.к. создает файлы.

    indificate()  # Запускает окно регистрации.
    Window.mainloop()  # Открывает это окно.
    #main()  # Добавлено, тк не работает вузовский комп.
