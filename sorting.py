from datetime import datetime
from random import *

def gen_arr(n):
    arr=[]
    for i in range(0,n):
        arr.append(randint(-10000,10000))
    return arr

def timeit(func):
    def wrapper(*args, **kwargs):
        start = datetime.now()
        result = func(*args, **kwargs)
        print(datetime.now() - start)
        return result
    return wrapper

@timeit
def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]

    return arr

@timeit
def select_sort_stable(arr):
    if len(arr) == 0: return
    for j in range(len(arr)):
        min = j
        for i in range(j + 1, len(arr)):
            if arr[i] < arr[min]: min = i
        if min != j:
            value = arr[min]
            for l in range(min, j - 1, -1):
                arr[l] = arr[l - 1]
            arr[j] = value

def main():

    n=int(input("Input numbers elements for sorting:"))
    a=gen_arr(n)

    print("Time bubble sort is ")
    bubble_sort(a)
    print("Time selection sort is")
    select_sort_stable(a)

if __name__ == '__main__':
    main()

