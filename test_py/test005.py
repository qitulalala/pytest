# todo 5. pytest fixture 用法 scope、autouse

import pytest

'''
测试夹具 fixture :我们可以在不修改当前函数代码逻辑的情况下，通过 fixture 来额外添加一些处理
定义
    fixture 是一个函数，在函数上添加注解@pytest.fixture来定义
    定义在 conftest.py 中，无需 import 就可以调用
    定义在其他文件中，import 后也可以调用
    定义在相同文件中，直接调用
使用
    第一种使用方式是@pytest.mark.usefixtures(fixturename)（如果修饰 TestClass 能对类中所有方法生效）
    第二种使用方式是作为函数参数
    第三种使用方式是 autouse（不需要显示调用，自动运行）
        autouse 遵循 scope 的规则，scope="session"整个会话只会运行 1 次，其他同理
        autouse 定义在 module 中，module 中的所有 function 都会用它（如果 scope="module"，只运行 1 次，如果 scope="function"，会运行多次）
        autouse 定义在 conftest.py，conftest 覆盖的 test 都会用它
        在使用 autouse 时需要同时注意 scope 和定义位置
    fixture 的顺序优先按 scope 从大到小，session > package > module > class > function
'''


@pytest.fixture(scope='class', autouse=True)
def test_login1():
    a = 'ha'
    print(a)
    return a


@pytest.fixture()
def test_login3():
    a = '你'
    print('\n'+a)
    return a


# @pytest.mark.usefixtures('test_login1', 'test_login3')
def test_login2(test_login1):
    a = test_login1
    b = '\n'+a+'好'
    print(b)


# @pytest.mark.usefixtures('test_login1')
class Testlogin4:
    def test_login4(self, test_login3):
        a = test_login3
        print(a)


# @pytest.mark.usefixtures()
def test_login4():
    a = 1
    print(a)
