arr = [10,2,3,4]

arr2 = [b for b in arr if b > 2]

dct = {1:"cat", 2:"dog", 3:"pig"}

arr_animal = [k for k,v in dct.items()]
dct_animal = {(k+10):v for k,v in dct.items() if k >1}

for index, value in enumerate(arr, start=1):
    print(f"Position: {index}, arr: {value}")


if __name__ == '__main__':
    print(arr2)
    print(arr_animal)
    print(dct_animal)
    