
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


if __name__ == '__main__':
    ll = [1, 2, 3]
    func_paly_dict(name='ccc', num=9)
    func_paly_list("qqq", '222')
    func_paly_list(*ll)
