

import unittest
import my_old_func

class YearTest(unittest.TestCase):


    def test_is_year_leap(self):
        self.assertTrue(my_old_func.year())

    def test_triangle(self):
        self.assertTrue(my_old_func.triangle(12, 25, 35))

    def test_type_Equilateral_triangle(self):
        self.assertEquals(my_old_func.treygolnick(12, 25, 35), "Equilateral triangle")


