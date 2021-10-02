# import pytest
from base_calculator import Calculator


# todo 测试类-计算器
class TestCalculator:
    # def __init__(self):
    #     pass
    # @classmethod
    # def setup_class(cls):
    #     cls.cal = Calculator()
    def setup_class(self):
        self.cal = Calculator()

    def test_add(self):
        result = self.cal.add(1, 2)
        assert result == 3
        print(result)

    def test_sub(self):
        self.cal.sub(3, 1)

    def test_mul(self):
        return self.cal.mul(2, 6)

    def test_div(self):
        print(self.cal.div(4, 2))
