"""
>>> import os
>>> os.path.dirname('xx.md')
''
>>>
>>> os.path.abspath('xx.md')
'C:\\Users\\chen\\xx.md'
>>>
>>> os.path.dirname(os.path.abspath('xx.md'))
'C:\\Users\\chen'
>>>

python3.8和python3.10的os.path.dirname函数功能不一样，3.8只能识别绝对路径
"""

"""
https://www.geeksforgeeks.org/python-passing-dictionary-as-arguments-to-function/
https://www.w3schools.com/python/gloss_python_function_arbitrary_arguments.asp
"""


def func_paly_dict(**kwargs):
    print(f'kwargs is {kwargs}')
    print(f'name is {kwargs["name"]}, num is {kwargs["num"]}')


def func_paly_list(*args):
    print(f'arg1 is {args[0]}, arg2 is {args[1]}')


"""
https://www.geeksforgeeks.org/enumerate-in-python/
"""


def play_enumerate():
    ll = ['qqq', 'www', 'eee']
    for count, el in enumerate(ll, 3):
        print(count, el)

    ss = 'qwer'
    for item in enumerate(ss):
        print(item)


"""
https://www.geeksforgeeks.org/python-property-function/
"""


class Pp:

    def __init__(self, v):
        self._value = v
        self.item = v

    def vv(self):
        return self._value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        print('set value to ' + v)
        self._value = v


"""
https://www.geeksforgeeks.org/decorators-in-python/
"""


def decorate_func(func):
    def inner_func(*args):
        print('start decorate_func')
        func(*args)
        print(f'{args[0]} use decorate_func')
    return inner_func


@decorate_func
def play_decorate(*args):
    print(f'run {args[0]}')


def play_decorate_b(*args):
    print(f'run {args[0]}')


play_decrate_func = decorate_func(play_decorate_b)


if __name__ == '__main__':
    # ll = [1, 2, 3]
    # func_paly_dict(name='ccc', num=9)
    # func_paly_list("qqq", '222')
    # func_paly_list(*ll)
    # play_enumerate()

    # p = Pp('aa')
    # print('get private param use function: ' + p.vv())
    # print('get public param: ' + p.item)
    # print('get private param use property' + p.value)
    # p.value = 'bb'
    # print('get private param use property' + p.value)

    play_decorate('play_decorate')
    play_decrate_func('play_decrate_func')
