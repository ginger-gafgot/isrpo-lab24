import unittest


import circle

import math

epsilon = pow(10,-10)

class CircleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = circle.area(0)
        self.assertEqual(res, 0)
        
    def test_circle_mul(self):
        res = circle.area(10)
        self.assertTrue(abs(res - 314.15926535897932384626433832795) < epsilon)
        
        res = circle.area(52)
        self.assertTrue(abs(res- 8494.8665353068009168029877083878) < epsilon)
        
        res = circle.area(1.1)
        self.assertTrue(abs(res - 3.8013271108436498185397984937682) < epsilon)
        
        res = circle.area(math.pi)
        self.assertTrue(abs(res - 31.006276680299820175476315067101) < epsilon)
    
    
    def test_zero_sum(self):
        res = circle.perimeter(0)
        self.assertEqual(res, 0)
        
    def test_circle_sum(self):
        res = circle.perimeter(10)
        self.assertTrue(abs(res - 62.83185307179586476925286766559) < epsilon)
        
        res = circle.perimeter(52)
        self.assertTrue(abs(res - 326.72563597333849680011491186107) < epsilon)
        
        res = circle.perimeter(1.1)
        self.assertTrue(abs(res - 6.9115038378975451246178154432149) < epsilon)
        
        res = circle.perimeter(math.pi)
        self.assertTrue(abs(res - 19.739208802178717237668981999752) < epsilon)