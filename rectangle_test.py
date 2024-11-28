import unittest


import rectangle

import math

epsilon = pow(10,-10)

class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = rectangle.area(10, 0)
        self.assertEqual(res, 0)
        
        res = rectangle.area(0, 35)
        self.assertEqual(res,0)
        
        res = rectangle.area(3.5, 0)
        self.assertEqual(res,0)
        
        res = rectangle.area(0, 0.67)
        self.assertEqual(res,0)
 
    def test_square_mul(self):
        res = rectangle.area(10, 10)
        self.assertEqual(res, 100)
        
        res = rectangle.area(52, 52)
        self.assertEqual(res, 2704)
        
        res = rectangle.area(1.1, 1.1)
        self.assertTrue(abs(res - 1.21) < epsilon)
        
        res = rectangle.area(math.pi, math.pi)
        self.assertTrue(abs(res - 9.869604401089357120529513782849) < epsilon)
    
    def test_rectangle_mul(self):
        res = rectangle.area(239, 10)
        self.assertEqual(res,rectangle.area(10,239))
        self.assertEqual(res, 2390)
        
        res = rectangle.area(17, 35)
        self.assertEqual(res, rectangle.area(35,17))
        self.assertEqual(res, 595)
        
        res = rectangle.area(1.1, 1.5)
        self.assertEqual(res, rectangle.area(1.5, 1.1))
        self.assertTrue(abs(res - 1.65) < epsilon)
        
        res = rectangle.area(math.pi, math.e)
        self.assertEqual(res, rectangle.area(math.e, math.pi))
        self.assertTrue(abs(res - 8.539734222673565677848730527685) < epsilon)
        
    def test_zero_sum(self):
        res = rectangle.perimeter(10, 0)
        self.assertEqual(res, rectangle.perimeter(0, 10))
        self.assertEqual(res, 20)
        
        res = rectangle.perimeter(0, 35)
        self.assertEqual(res, rectangle.perimeter(35, 0))
        self.assertEqual(res, 70)
        
        res = rectangle.perimeter(3.5, 0)
        self.assertEqual(res, rectangle.perimeter(0, 3.5))
        self.assertTrue(abs(res - 7) < epsilon)
        
        res = rectangle.perimeter(0, 0.67)
        self.assertEqual(res, rectangle.perimeter(0.67, 0))
        self.assertTrue(abs(res - 1.34) < epsilon)
 
    def test_square_sum(self):
        res = rectangle.perimeter(10, 10)
        self.assertEqual(res, 40)
        
        res = rectangle.perimeter(52, 52)
        self.assertEqual(res, 208)
        
        res = rectangle.perimeter(1.1, 1.1)
        self.assertTrue(abs(res - 4.4) < epsilon)
        
        res = rectangle.perimeter(math.pi, math.pi)
        self.assertTrue(abs(res - 12.566370614359172) < epsilon)
    
    def test_rectangle_sum(self):
        res = rectangle.perimeter(239, 10)
        self.assertEqual(res,rectangle.perimeter(10,239))
        self.assertEqual(res, 498)
        
        res = rectangle.perimeter(17, 35)
        self.assertEqual(res, rectangle.perimeter(35,17))
        self.assertEqual(res, 104)
        
        res = rectangle.perimeter(1.1, 1.5)
        self.assertEqual(res, rectangle.perimeter(1.5, 1.1))
        self.assertTrue(abs(res - 5.2) < epsilon)
        
        res = rectangle.perimeter(math.pi, math.e)
        self.assertEqual(res, rectangle.perimeter(math.e, math.pi))
        self.assertTrue(abs(res - 11.719748964097676947645861709264) < epsilon)
        
