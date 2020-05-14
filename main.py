import time


def countingSort(arr, exp1):
    n = len(arr)

    output = [0] * (n)
    count = [0] * (10)
    for i in range(0, n):
        index = (arr[i] / exp1)
        count[(index) % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i] / exp1)
        output[count[(index) % 10] - 1] = arr[i]
        count[(index) % 10] -= 1
        i -= 1

    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]


def radixSort(arr, print_array):
    t0 = time.time()
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        countingSort(arr, exp)
        exp *= 10

    tf = time.time()
    print("Radix sort time in seconds: {}".format(tf - t0))
    if print_array:
        printArray(arr)


def printArray(arr):
    for i in range(len(arr)):
        print(arr[i]),


def generate_random(size):
    from random import seed
    from random import random
    # seed random number generator
    seed(1)
    arr = []
    # generate random numbers between 0-1
    for _ in range(size):
        value = int(random() * 1000)
        arr.append(value)
        # print(value)
    return arr


def built_in_sort(arr):
    t0 = time.time()
    arr = sorted(arr)
    tf = time.time()
    print("\nBuilt in Sort time in seconds: {}".format(tf - t0))


def bubble_sort(arr, debug):
    t0 = time.time()
    n = len(arr)

    for i in range(n - 1):
        for j in range(0, n - i - 1):

            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
        if debug:
            print("."),
    tf = time.time()
    print("\nBubble Sort time in seconds: {}".format(tf - t0))


if __name__ == '__main__':
    n = 1000
    print("Ordenando {} elementos".format(n))
    arr = generate_random(n)

    bubble_sort(arr, debug=True)
    radixSort(arr, print_array=False)
    built_in_sort(arr)
