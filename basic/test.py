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
import asyncio
import os

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

"""
TypeError: 'NoneType' object is not callable
https://stackoverflow.com/questions/9768865/python-nonetype-object-is-not-callable-beginner
https://www.geeksforgeeks.org/decorators-with-parameters-in-python/
"""


def decorator(*args, **kwargs):
    print("Inside decorator")

    def inner_func(func):
        # code functionality here
        print("Inside inner function")
        print(args[0], args[1], "I like", kwargs['like'])

        func()

    # returning inner function
    return inner_func


@decorator('aa', 'bb', like="geeksforgeeks")
def play_decorate_c():
    print("Inside actual function")


"""
https://www.youtube.com/watch?v=0GVLtTnebNA
https://zetcode.com/python/async-await/
https://realpython.com/async-io-python/
"""


async def kill_time(num):
    print(f"get {num}")
    await asyncio.sleep(1)


async def play_async():
    tasks = []
    for i in range(1, 101):
        tasks.append(kill_time(i))

    await asyncio.sleep(1)
    await asyncio.gather(*tasks)


async def mul(x, y):
    return x * y


def play_async_loop():
    loop = asyncio.get_event_loop()

    res = loop.run_until_complete(mul(5, 5))
    print(res)


def play_break():
    for i in range(10):

        for j in range(5):
            if j == 3:
                break
            print(f'i = {i}, j = {j}')

        if i == 2:
            break


def play_continue():
    for i in range(10):
        if i == 8:
            continue


def play_fileno():
    with open('python_cmd.py') as f:
        print(f)
        print(f.fileno())

    with open('shell_python.sh') as f2:
        print(f2)
        print(f2.fileno())


"""
https://www.tutorialspoint.com/python/os_open.htm
"""


def play_fileno2():
    fw = os.open('rw.text', os.O_RDWR | os.O_CREAT)
    print(type(fw))
    print(fw)
    os.write(fw, b"this is test")
    os.close(fw)

    fr = os.open('rw.text', os.O_RDONLY)
    read_info = os.fdopen(fr)
    print(fr)
    print("read info is: ", read_info.read())
    os.close(fr)


"""
https://www.geeksforgeeks.org/python-os-pipe-method/
"""


def play_pipe():
    r, w = os.pipe()
    text = b'hello pipe'
    print("w is: ", w)
    print("text is: ", text)
    print("text decode is: ", text.decode())
    os.write(w, text)
    os.close(w)

    read_info = os.fdopen(r)
    print("r is: ", r)
    print("Read text: ", read_info)
    print("Read text read: ", read_info.read())


def play_iter():
    ll = [1, 2, 3]
    for i in ll:
        print(i)

    it = iter(ll)

    print("get fist element in it: ", next(it))
    for e in it:
        print(e)


if __name__ == '__main__':
    print('\n')
    print('\n')
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

    # play_decorate('play_decorate')
    # play_decrate_func('play_decrate_func')
    # play_decorate_c

    # asyncio.run(play_async())
    # play_async_loop()

    # play_break()
    # play_continue()

    # play_fileno()
    play_fileno2()

    # play_pipe()

    # play_iter()
