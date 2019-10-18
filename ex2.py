# Задание 2 (на создание новых классов)
# Создать классы
# 1) Прямоугольная площадка (пример: комната) (свойства: две стороны).
# Методы:
# 1.	вычисляем площадь,
# 2.	вычисляем периметр.
# 2) Точка на карте (свойства: X, Y).
# Методы:
# 1.	Нужно вычислить расстояние до начала координат,
# 2.	* вычисляется расстояние между точкой и другой точкой экземпляром этого же класса
# 3.	** перевод в другие системы координат

import math

class Square:
    def __init__(self, storona1, storona2):
        self.storona1 = storona1
        self.storona2 = storona2

    def Square_room(self):
        return self.storona1 * self.storona2

    def Perimetr(self):
        return (self.storona1 + self.storona2)*2


class Tochka:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def rast1(self):
        return (self.x**2 + self.y**2)**0.5

    def rast2(self, *args):
        p1 = args[0:2]
        p2 = args[2:4]
        return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    def another_system(self):
        #цилиндрическая
        p = math.sqrt(self.x**2 + self.y**2)
        phi = math.atan2(self.y, self.x)
        return "Radius", p, "degree", phi

p = Square(25, 45)
print(p.Square_room())
print(p.Perimetr())

k = Tochka(55, 35)
print(k.rast1())
print("Distance", k.rast2(15, 35, 25, 16))
print(k.another_system())


