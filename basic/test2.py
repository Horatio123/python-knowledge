import pytest


def odd_numbers():
    n = 1
    while True:
        yield n
        n += 2


def countdown(n):
    while n > 0:
        yield n
        n -= 1


def test_play_yield():
    odd = odd_numbers()
    for i in range(5):
        print(next(odd))

    ll = countdown(5)
    print("cccc: ", next(ll))
    for i in ll:
        print(i)


def play_zip():
    names = ['Alice', 'Bob', 'Charlie']
    ages = [25, 30, 35]
    countries = ['USA', 'Canada', 'Australia']
    zipped = zip(names, ages, countries)
    print(type(zipped))
    for person in zipped:
        print(person)


def get_int(item):
    var = item.split('c')[1]
    return var


def play_sort():

    # func = lambda x: x.split('c')[1]
    files = ["cc001", "adc005", "adc104", "adc002"]

    files.sort(reverse=True)
    print(files)

    files.sort(key=get_int)
    print(files)

    files.sort(key=lambda x: x.split('c')[1])
    print(files)


def test_get_name():
    print()
    print(__name__)


if __name__ == '__main__':
    # play_hexlify()
    # play_yield()
    # play_zip()
    play_sort()
