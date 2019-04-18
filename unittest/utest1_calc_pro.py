import unittest
import calc_pro

class BasicCalcTests(unittest.TestCase):

    def testAdd(self):
        self.assertEqual(calc_pro.add(2, 3), 5)

    def testSub(self):
        self.assertEqual(calc_pro.sub(7, 2), 5)

    def testMult(self):
        self.assertEqual(calc_pro.mult(2, 5), 10)

    def testDiv(self):
        self.assertEqual(calc_pro.div(10, 2), 5)

class ExtCalcTests(unittest.TestCase):

    def testPow(self):
        self.assertEqual(calc_pro.pow(2, 3), 8)

    def testSqrt(self):
        self.assertEqual(calc_pro.sqrt(16), 4.0)

if __name__ == '__main__':
    unittest.main()