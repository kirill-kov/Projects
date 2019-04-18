import unittest
import calc

class CalcTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """Set up for class"""
        print("setUpClass")
        print("==========")

    @classmethod
    def tearDownClass(cls):
        """Tear down for class"""
        print("==========")
        print("tearDownClass")

    def setUp(self):
        """Set up for test"""
        print("Set up for [" + self.shortDescription() + "]")

    def tearDown(self):
        """Tear down for test"""
        print("Tear down for [" + self.shortDescription() + "]")
        print("")


    def testAdd(self):
        """Add operation test"""
        print("id: " + self.id())
        self.assertEqual(calc.add(2, 3), 5)

    def testSub(self):
        """Sub operation test"""
        print("id: " + self.id())
        self.assertEqual(calc.sub(7, 2), 5)

    def testMult(self):
        """Mult operation test"""
        print("id: " + self.id())
        self.assertEqual(calc.mult(2, 5), 10)

    def testDiv(self):
        """Div operation test"""
        print("id: " + self.id())
        self.assertEqual(calc.div(10, 2), 5)

if __name__ == '__main__':
    unittest.main()
