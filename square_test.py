import unittest


import square

import math

epsilon = pow(10,-10)

class SquareTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = square.area(0)
        self.assertEqual(res, 0)
        
    def test_square_mul(self):
        res = square.area(10)
        self.assertEqual(res, 100)
        
        res = square.area(52)
        self.assertEqual(res, 2704)
        
        res = square.area(1.1)
        self.assertTrue(abs(res - 1.21) < epsilon)
        
        res = square.area(math.pi)
        self.assertTrue(abs(res - 9.869604401089357120529513782849) < epsilon)
    
    
    def test_zero_sum(self):
        res = square.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_square_sum(self):
        res = square.perimeter(10)
        self.assertEqual(res, 40)
        
        res = square.perimeter(52)
        self.assertEqual(res, 208)
        
        res = square.perimeter(1.1)
        self.assertTrue(abs(res - 4.4) < epsilon)
        
        res = square.perimeter(math.pi)
        self.assertTrue(abs(res - 12.566370614359172) < epsilon)