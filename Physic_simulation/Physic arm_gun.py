import pygame
import numba
from numba import njit
import time


pygame.init()  # Инициализация Pygame.
screen = pygame.display.set_mode((800, 1000))
k = None


class Point_of_gun():
    def __init__(self, L, m):
        """
        Класс точек рогатки
        :param L: Удлинение для этой точки
        :param m: Масса кусочка.
        """
        self.L = L
        self.T1 = None
        self.T2 = None
        self.V = 0
        self.m = m
        self.E = self.m * self.V**2 / 2
        self.a = 0

    def move_points(self, dt):
        """Перемещает точку"""

        self.V += self.a * dt
        self.L -= self.V * dt

    def count_force(self, obj1, obj2, L, k_effect):
        """
        Рассчитывает новые силы, действующие на точку рогатки
        :param obj1: точка ближе к рогатке.
        :param obj2: точка далье от рогатки.
        :return: переменные сил сделает новые.
        """
        global k

        T1, T2 = force_count_by_numba(obj1.L, obj2.L, self.L, L, k_effect)

        self.a = (T1 - T2) / self.m
        self.T1 = T1
        self.T2 = T2

    def force_first_point(self, massive):
        """
        Рассчет силы для первой точки.
        :param massive: Массив точек рогатки.
        :return: None
        """
        # L = 0.1 / count_of_points  # м.
        # if massive[1].L - L > 0:
        #     self.T2 = k * (massive[1].L - L) * count_of_points
        # elif L + massive[1].L < 0:
        #     self.T2 = k * (massive[1].L + L) * count_of_points
        # else:
        #     self.T2 = 0
        pass

    def print_point(self):
        """
        Рисует точки для визуализации процесса.
        :return:  None
        """
        pygame.draw.circle(screen, (193, 193, 0), (int(550 - self.L * 2500), 223), 3, 0)


class Shell():
    def __init__(self):
        """Снаряд, который запускает товарищ с рогаткой"""
        self.L = 0.2  # м.
        self.M = 0.010  # кг.
        self.a = 0
        self.V = 0

    def move_shell(self, dt, count_of_points):
        """Передвигает снаряд"""
        self.a = 2 * right_points[count_of_points - 1].T2 / self.M
        self.V += self.a * dt
        self.L -= self.V * dt

    def print_shell(self):
        """
        Рисует снаряд для визуализации
        :return: None
        """
        pygame.draw.circle(screen, (193, 0, 0), (int(550 - self.L * 2500), 223), 3, 0)


left_points = []
right_points = []
k = 10 / 0.1  # Н / м.
lenght_of_gun = 0.10  # м.
weight_of_gun = 0.030  # кг.


def main(count_of_points, delta_time, visual):
    """
    Эта функция выполняет рассчет скорости, которая будет у снаряда в момент вылета из рогатки.
    :param count_of_points: количество точек, на которое бьтся резинка рогатки.
    :param delta_time: время, за которое считаются малые перемещения обьектов.
    """
    global k, right_points
    right_points = []
    frame = 0
    finished = False
    k_effect = k * count_of_points  # Н/м - Коэфицент упругости резинки для одной точки.
    L = 0.1 / count_of_points  # м. - расстояние между точками в нерастянутом виде.

    # Создадим массив точек рогатки.
    for num in range(count_of_points):
        l = lenght_of_gun / count_of_points * num * 2
        dm = weight_of_gun / count_of_points
        # left_points.append(Point_of_gun(l, dm))
        right_points.append(Point_of_gun(l, dm))
    # Создадим снаряд.
    shell = Shell()

    while shell.L > 0 and not finished:  # Левый массив убран, так как он имеет аналогичные рассчеты \
        # и тратит время на пересчет своих точек.
        # Выполним перерассчет сил.
        for num in range(count_of_points):
            if num == 0:  # Первая точка не взаимодествует с точками ближе к рогатке, чем она.
                # left_points[num].force_first_point(left_points)
                right_points[num].force_first_point(right_points)
            elif num == count_of_points - 1:  # Последняя точка взаимодействует со снарядом.
                # left_points[num].count_force(left_points[num - 1], shell)
                right_points[num].count_force(right_points[num - 1], shell, L, k_effect)
            else:
                # left_points[num].count_force(left_points[num - 1], left_points[num + 1])
                right_points[num].count_force(right_points[num - 1], right_points[num + 1], L, k_effect)

        # Выполним передвижение точек рогатки.
        for num in range(1, count_of_points):  # Нулевая точка закреплена тем, что отсчет идет с единицы.
            # left_points[num].move_points(delta_time)
            right_points[num].move_points(delta_time)
        # Выполним передвижние снаряда.
        shell.move_shell(delta_time, count_of_points)

        if visual == True:
            if frame >= 10000:
                frame = 0
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        finished = True

                screen.fill((0, 0, 0))

                for num in range(50):
                    num_of_point = int(count_of_points / 50 * num)
                    right_points[num_of_point].print_point()
                shell.print_shell()
                pygame.draw.circle(screen, (193, 193, 200), (int(550), 223), 3, 0)
                pygame.display.update()

            frame += 1
    print(shell.V)


def circle():
    """
    Это функция, которая запускает моделирование с различными параметрами.
    В качестве параметров выбраны количесво точек резинки и дельта времени.
    """
    # Зададим количество точек рогатки.
    start_count = 10
    step_of_count = 5
    finish_count = start_count + step_of_count * 10
    # Зададим период времени, за который происходят малые перемещения.
    start_delta_time = 1 / 10**4
    step_of_delta_time = 1
    count_of_delta_times = 4
    finish_delta_time = start_delta_time / 10**(step_of_delta_time * (count_of_delta_times - 1))

    for num_of_count in range((finish_count - start_count) // step_of_count + 1):
        _count_of_points = start_count + num_of_count * step_of_count
        print("Количество точек: " + str(_count_of_points))
        for num_of_time in range(count_of_delta_times):
            _delta_time = start_delta_time / 10**num_of_time
            main(_count_of_points, _delta_time, False)


@njit(fastmath=True, cache=True)
def force_count_by_numba(obj1_L, obj2_L, self_L, L, k_effect):
    """
    Это функция подсчета силы, действующей на точку резинки.
    Она ускорена припомощи Numba.
    :param obj1: точка ближе к рогатке.
    :param obj2: точка далье от рогатки.
    :param self: обьект, для которого считается сила.
    :param L: расстояние между соседнии точками в не растянутом состоянии.
    """
    if self_L - obj1_L > L:
        T1 = k_effect * ((self_L - obj1_L) - L)
    elif obj1_L - self_L > L:
        T1 = k_effect * ((self_L - obj1_L) + L)
    else:
        T1 = 0

    if obj2_L - self_L > L:
        T2 = k_effect * ((obj2_L - self_L) - L)
    elif self_L - obj2_L > L:
        T2 = k_effect * ((obj2_L - self_L) + L)
    else:
        T2 = 0

    return T1, T2


if __name__ == '__main__':
    time_of_start = time.time()
    #main(20, 1 / 10000, True)
    circle()
    print("Время работы: " + str(time.time() - time_of_start))