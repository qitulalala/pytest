import pytest

from base_calculator import Calculator
# todo terminal执行
'''
pytest --collect-only
pytest test_*.py
pytest -v
pytest -v -s
pytest -x       发现错误立即停止
pytest --maxfail=2
pytest -m
pytest --lf     执行上次错误用例
pytest --ff     先执行上次错误用例，再执行其他
pytest --junitxml=./result.xml  将测试结果生成xml文件
'''


@pytest.mark.webtest
def test_add_001():
    a = Calculator().add(5, 6)
    print(a)
    assert a == 11


@pytest.mark.webtest
def test_add_002():
    b = Calculator().add(1, 2.1)
    print(b)
    assert b == 3.1
