from random import shuffle

"""
Will sort a list of integers from lowest to highest

Binary Search:
Best - O(n)
Worst - O(n!)
Average - O(n!)
Space Complexity - O(1)

This function returns a copy for the sake of it.
"""


def bogo_sort(data: list) -> list:
    data = data[:]

    is_sorted = False
    while not is_sorted:
        shuffle(data)
        is_sorted = True
        for i in range(len(data) - 1):
            if data[i] > data[i + 1]:
                is_sorted = False
                break

    return data


def run():
    print("Bogo Sort")

    max_value = int(input("Enter maximum value: "))
    data = list(range(max_value))
    shuffle(data)

    print("Before: {}".format(data))
    data = bogo_sort(data)
    print("After: {}".format(data))
