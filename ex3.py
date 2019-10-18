# Создайте наборы тестов на написанные функции из прошлого домашнего задания:
# •	Написать функцию is_year_leap, принимающую 1 аргумент — год, и возвращающую True, если год високосный, и False иначе.
# •	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами. Если треугольник существует, вернёт True, иначе False.
# •	Функция принимает три числа a, b, c. Функция должна определить, существует ли треугольник с такими сторонами и если существует,
# то возвращает тип треугольника Equilateral triangle (равносторонний), Isosceles triangle (равнобедренный), Versatile triangle (разносторонний) или не треугольник (Not a triangle).

import unittest
import my_old_func

class YearTest(unittest.TestCase):


    def test_is_year_leap(self):
        self.assertTrue(my_old_func.year())

    def test_triangle(self):
        self.assertTrue(my_old_func.triangle(12, 25, 35))

    def test_type_Equilateral_triangle(self):
        self.assertEquals(my_old_func.treygolnick(12, 25, 35), "Equilateral triangle")


