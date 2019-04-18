import unittest
import utest1_calc_pro

calcTestSuite = unittest.TestSuite()
calcTestSuite.addTest(unittest.makeSuite(utest1_calc_pro.BasicCalcTests))
calcTestSuite.addTest(unittest.makeSuite(utest1_calc_pro.ExtCalcTests))
print("count of tests: " + str(calcTestSuite.countTestCases()) + "\n")

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTestSuite)


















