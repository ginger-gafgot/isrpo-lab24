import unittest


import triangle

import math

epsilon = pow(10,-10)

class TriangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = triangle.area(10, 0)
        self.assertEqual(res, 0)
        
        res = triangle.area(0, 35)
        self.assertEqual(res,0)
        
        res = triangle.area(3.5, 0)
        self.assertEqual(res,0)
        
        res = triangle.area(0, 0.67)
        self.assertEqual(res,0)
 
    
    def test_triangle_mul(self):
        res = triangle.area(239, 10)
        self.assertEqual(res,triangle.area(10,239))
        self.assertTrue(abs(res - 1195) < epsilon)
        
        res = triangle.area(17, 35)
        self.assertEqual(res, triangle.area(35,17))
        self.assertTrue(abs(res - 297.5) < epsilon)
        
        res = triangle.area(1.1, 1.5)
        self.assertEqual(res, triangle.area(1.5, 1.1))
        self.assertTrue(abs(res - 0.825) < epsilon)
        
        res = triangle.area(math.pi, math.e)
        self.assertEqual(res, triangle.area(math.e, math.pi))
        self.assertTrue(abs(res - 4.2698671113367828389243652638425) < epsilon)
        
    def test_zero_sum(self):
        res = triangle.perimeter(0, 0, 0)
        self.assertEqual(res, 0)
        
        res = triangle.perimeter(0, 0, 1)
        self.assertEqual(res, triangle.perimeter(0, 1, 0))
        self.assertEqual(res, 1)
        
        res = triangle.perimeter(0, 1, 0)
        self.assertEqual(res, triangle.perimeter(1, 0, 0))
        self.assertEqual(res, 1)
        
        res = triangle.perimeter(1, 0, 0)
        self.assertEqual(res, triangle.perimeter(0, 0, 1))
        self.assertEqual(res, 1)
        
        res = triangle.perimeter(0, 1, 1)
        self.assertEqual(res, triangle.perimeter(1, 1, 0))
        self.assertEqual(res, 2)
        
        res = triangle.perimeter(1, 1, 0)
        self.assertEqual(res, triangle.perimeter(1, 0, 1))
        self.assertEqual(res, 2)
        
        res = triangle.perimeter(1, 0, 1)
        self.assertEqual(res, triangle.perimeter(0, 1, 1))
        self.assertEqual(res, 2)
        
    def test_triangle_sum(self):
        res = triangle.perimeter(239, 10, 230)
        self.assertEqual(res,triangle.perimeter(10,230, 239))
        self.assertEqual(res, 479)
        
        res = triangle.perimeter(17, 35, 51)
        self.assertEqual(res, triangle.perimeter(35, 51, 17))
        self.assertEqual(res, 103)
        
        res = triangle.perimeter(1.1, 1.5, 2.5)
        self.assertEqual(res, triangle.perimeter(1.5, 2.5, 1.1))
        self.assertTrue(abs(res - 5.1) < epsilon)
        
        res = triangle.perimeter(math.pi, math.e, 4)
        self.assertEqual(res, triangle.perimeter(math.e, 4,math.pi))
        self.assertTrue(abs(res - 9.8598744820488384738229308546322) < epsilon)
        
