from functools import reduce

arr = [10,2,3,4]

arr2 = [b for b in arr if b > 2]

dct = {1:"cat", 2:"dog", 3:"pig"}

arr_animal = [k for k,v in dct.items()]
dct_animal = {(k+10):v for k,v in dct.items() if k >1}

for index, value in enumerate(arr, start=1):
    print(f"Position: {index}, arr: {value}")

arr3 = list(map(lambda x: x*2, arr))
sum = reduce(lambda x, y:x+y, arr3)
big = reduce(lambda x,y:x if x >y else y, arr3, 30)


if __name__ == '__main__':
    print(f"arr2 is {arr2}")
    print(f"arr_animal is {arr_animal}")
    print(f"dct_animal is {dct_animal}")
    print(f"arr3 is {arr3}")
    print(f"sum is {sum}")
    print(f"big is {big}")
    it = iter(arr3)
    value = next(it)
    print(f"test iter value is {value}")
    for item in it:
        print(f"test iter item is {item}")


    