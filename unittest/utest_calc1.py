import unittest
import calc

class CalcTest(unittest.TestCase):
    def testAdd(self):
        self.assertEqual(calc.add(2, 3), 5)

    def testSub(self):
        self.assertEqual(calc.sub(7, 2), 5)

    def testMult(self):
        self.assertEqual(calc.mult(2, 5), 10)

    def testDiv(self):
        self.assertEqual(calc.div(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
