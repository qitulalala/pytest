import pytest
from base_calculator import Calculator

'''
@pytest.mark.**** 标记用例
@pytest.mark.parametrize(‘k1,k2,k3',[[v1,v2,v3],[V1,V2,V3]], ids=['用例名称1','用例名称2'])
    1. 第一个参数是字符串，多个参数中间用逗号隔开
    2. 第二个参数是list,多组数据用列表or元祖类型;传三个或更多参数也是这样传。
    3. list的每个元素都是一个列表or元组，列表or元组里的每个元素和按参数顺序一一对应第一参数字符串
    4. ids=给每一个用例起名字，对应关系如上
'''


# todo 参数化
@pytest.mark.parametrize('a,b,check', [
    (1, 2, -1),
    [2, 5, -3],
    [6, 1, 5]
], ids=['整数', '小数', '复数'])
def test002(a, b, check):
    result1 = Calculator().sub(a, b)
    assert result1 == check


# def test001(a, b, check):
#     result2 = Calculator().sub(a, b)
#     assert result2 == check

#
#
# list1 = [
#     (1, 2, 3),
#     [2.1, 5, 7.1],
#     [-1, -1, -2]
# ]
#
#
# @pytest.mark.parametrize('a', list1, ids=['整数', '小数', '复数'])
# def test002(a):
#     result = Calculator().add(a[0], a[1])
#     assert result == a[2]
