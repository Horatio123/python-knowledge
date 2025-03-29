from functools import reduce

arr = [10,2,3,4]

arr2 = [b for b in arr if b > 2]

dct = {5:"cat", 2:"dog", 3:"pig"}

arr_animal = [k for k,v in dct.items()]
dct_animal = {(k+10):v for k,v in dct.items() if k >1}

for index, value in enumerate(arr, start=1):
    print(f"Position: {index}, arr: {value}")

arr3 = list(map(lambda x: x*2, arr))
sum = reduce(lambda x, y:x+y, arr3)
big = reduce(lambda x,y:x if x >y else y, arr3, 30)

num_fruit = {"apple":2, "orange": 9, "melon": 3}
# test map for dict
num_fruit_2 = dict(map(lambda x: (x[0], x[1]*2), num_fruit.items()))
print(f"num_fruit_2 is {num_fruit_2}")

#test reduce for dict
print(f"num_fruit is {num_fruit.items()}")
max_fruit = reduce(lambda a, b: a if num_fruit[a] > num_fruit[b] else b, num_fruit.keys())
print(f"max_fruit is {max_fruit}, num is {num_fruit[max_fruit]}")
min_fruit = reduce(lambda a, b: a if a[1] < b[1] else b, num_fruit.items())
print(f"min_fruit is {min_fruit[0]}, num is {min_fruit[1]}")

# test dict items
dct2 = {"a": {"type":{"id":1,"name":"god"}}, "b": 2, "c": 3}
print(f"dct2 is {dct2}")
print(f"dct2 is {dct2.items()}")

if __name__ == '__main__':
    print(f"arr2 is {arr2}")
    print(f"arr_animal is {arr_animal}")
    print(f"dct_animal is {dct_animal}")
    print(dct_animal.items())
    print(f"arr3 is {arr3}")
    print(f"sum is {sum}")
    print(f"big is {big}")
    it = iter(arr3)
    value = next(it)
    print(f"test iter value is {value}")
    for item in it:
        print(f"test iter item is {item}")


    