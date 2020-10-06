from random import shuffle

"""
Will sort a list of integers from lowest to highest

Bubble Sort:
Best - O(n)
Worst - O(n^2)
Average - O(n^2)
Space Complexity - O(1)

This function returns a copy for the sake of it.
"""


def bubble_sort(data: list) -> list:
    data = data[:]

    swap = True
    while swap:
        swap = False
        for i in range(len(data) - 2):
            if data[i] > data[i + 1]:
                temp = data[i]
                data[i] = data[i + 1]
                data[i + 1] = temp
                swap = True

    return data


def run():
    print("Bubble Sort")

    max_value = int(input("Enter maximum value: "))
    data = list(range(max_value))
    shuffle(data)

    print("Before: {}".format(data))
    data = bubble_sort(data)
    print("After: {}".format(data))
