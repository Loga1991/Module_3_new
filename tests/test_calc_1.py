import pytest

from Calcul_ht.app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_succes(self):
        assert self.calc.adding(self, 1, 1) == 2
    def test_adding_unsucces(self):
        assert self.calc.adding(self, 1, 2) == 1

    def test_multiply_succes(self):
        assert self.calc.multiply(self, 3, 2) == 6
    def test_multiply_unsucces(self):
        assert self.calc.multiply(self, 3, 2) == 7

    def test_division_succes(self):
        assert self.calc.division(self, 8, 2) == 4
    def test_division_unsucces(self):
        assert self.calc.division(self, 8, 2) == 7
    def test_zero_division(self):
        with pytest.raises(ZeroDivisionError):
            self.calc.division(1, 0)

    def test_subtraction_succes(self):
        assert self.calc.subtraction(self, 8, 2) == 6
    def test_subtraction_unsucces(self):
        assert self.calc.subtraction(self, 8, 2) == 7

    def teardown(self):
        print("Выполнение метода Teardown")




