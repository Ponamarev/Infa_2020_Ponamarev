import tkinter
import pygame


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
        self.L += self.V * dt
        # Нулевая точка должна быть закреплена.

    def count_force(self, obj1, obj2):
        """
        Рассчитывает новые силы, действующие на точку рогатки
        :param obj1: точка ближе к рогатке.
        :param obj2: точка далье от рогатки.
        :return: переменные сил сделает новые.
        """
        global k
        L = 0.1 / count_of_points  # м.
        self.T1 = obj1.T2

        if k * (L - (self.L - obj1.L)) * count_of_points > 0:
            T1 = k * (L - (self.L - obj1.L)) * count_of_points
        else:
            T1 = 0

        if k * (obj2.L - self.L - L) * count_of_points > 0:
            T2 = k * (obj2.L - self.L - L) * count_of_points
        else:
            T2 = 0

        self.a = (T2 - T1) / self.m

        self.T2 = T2

        # Нужно обработать первую и последнюю точки.

    def force_first_point(self, massive):
        """
        Рассчет силы для первой точки.
        :param massive: Массив точек рогатки.
        :return: None
        """
        L = 0.1 / count_of_points  # м.
        if k * (massive[1].L - L) > 0:
            self.T2 = k * (massive[1].L - L) * count_of_points
        else:
            self.T2 = 0

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

    def move_shell(self, dt):
        """Передвигает снаряд"""
        # if (left_points[count_of_points].T2 + right_points[count_of_points].T2) < 0:
        if 2 * right_points[count_of_points - 1].T2 < 0:
            self.a = 0
        else:
            # self.a = (left_points[count_of_points].T2 + right_points[count_of_points].T2) / self.M
            self.a = 2 * right_points[count_of_points - 1].T2 / self.M

        self.V += self.a * dt
        self.L -= self.V * dt

    def print_shell(self):
        """
        Рисует снаряд для визуализации
        :return: None
        """
        pygame.draw.circle(screen, (193, 0, 0), (int(550 - self.L * 2500), 223), 3, 0)


count_of_points = 100000
delta_time = 1 / 10000000  # с.
left_points = []
right_points = []
lenght_of_gun = 0.10  # м.
weight_of_gun = 11.030  # кг.
k = 10 / 0.2  # Н / м.
frame = 0
finished = False


def main():
    global k
    frame = 0
    finished = False
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
                right_points[num].count_force(right_points[num - 1], shell)
            else:
                # left_points[num].count_force(left_points[num - 1], left_points[num + 1])
                right_points[num].count_force(right_points[num - 1], right_points[num + 1])
        # Выполним передвижение точек рогатки.
        for num in range(1, count_of_points):  # Нулевая точка закреплена тем, что отсчет идет с единицы.
            # left_points[num].move_points(delta_time)
            right_points[num].move_points(delta_time)
        # Выполним передвижние снаряда.
        shell.move_shell(delta_time)
        print(right_points[count_of_points - 1].T2)
        print('скорость' + str(shell.V))
        print(right_points[count_of_points - 1].V)

        if frame >= 10:
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

    # Надо решить проблему со знаками сил точек.
    # Надо решить проблему со знаками в движении снаряда. и у частиц тоже.


if __name__ == '__main__':
    main()
