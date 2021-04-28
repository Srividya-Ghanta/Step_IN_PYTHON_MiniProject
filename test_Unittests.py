import unittest
import CalculatorSimple

class TestCalc(unittest.TestCase):
    def test_Addition(self):
        res = CalculatorSimple.performAddition(2, 3)
        self.assertEqual(res,5)

    def test_Subtraction(self):
        res = CalculatorSimple.performSubtraction(4, 5)
        self.assertEqual(res,-1)
        res = CalculatorSimple.performSubtraction(5, 4)
        self.assertEqual(res,1)

    def test_FloatDivision(self):
        res = CalculatorSimple.performFloatDivision(24, 5)
        self.assertEqual(res,4.80)

    def test_IntegerDivision(self):
        res = CalculatorSimple.performIntegerDivision(24, 5)
        self.assertEqual(res,4)
        res = CalculatorSimple.performIntegerDivision(80,4)
        self.assertEqual(res,20)

    def test_Moduluos(self):
        res = CalculatorSimple.performModulous(80, 5)
        self.assertEqual(res,0)
        res = CalculatorSimple.performModulous(5, 3)
        self.assertEqual(res, 2)
    def test_Multiplication(self):
        res = CalculatorSimple.performMultiplication(3, 6)
        self.assertEqual(res,18)
        res = CalculatorSimple.performMultiplication(50, 100)
        self.assertEqual(res, 5000)
    def test_Power(self):
        res = CalculatorSimple.performPowerOperation(3, 4)
        self.assertEqual(res,81)
        res = CalculatorSimple.performPowerOperation(4, 1/2)
        self.assertEqual(res, 2)
        
if __name__ == '__main__':
    unittest.main()
    