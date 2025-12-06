from functools import reduce


arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
# arr3 = [5,7,9]

arr3 = list(map(lambda x, y: x + y, arr1, arr2))
print(f"arr3 is {arr3}")

dict1 = {"cat": 1, "dog": 2, "pig": 3}
dict2 = {"cat": 3, "dog": 5, "pig": 1}
dict3 = dict(map(lambda x: (x, dict1[x] + dict2[x]), dict1.keys()))
#dict1.keys() is ['cat', 'dog', 'pig']
print(f"dict3 is {dict3}")


sum_animal = reduce(lambda x, y: x + y, dict1.values())
#dict1.values() is [1, 2, 3]
max_animal = reduce(lambda x, y: x if x[1] > y[1] else y, dict1.items())
#dict1.items() is [('cat', 1), ('dog', 2), ('pig', 3)]
print(f"sum_animal is {sum_animal}")
print(f"max_animal is {max_animal}")
