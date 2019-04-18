import unittest
import utest1_calc_pro

testLoad = unittest.TestLoader()
suites = testLoad.loadTestsFromModule(utest1_calc_pro)

testResult = unittest.TestResult()

runner = unittest.TextTestRunner()
testResult = runner.run(suites)
print("errors")
print(len(testResult.errors))
print("failures")
print(len(testResult.failures))
print("skipped")
print(len(testResult.skipped))
print("testsRun")
print(testResult.testsRun)