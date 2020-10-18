from random import shuffle

"""
Will sort a list of integers from lowest to highest

Insertion Sort:
Best - O(n)
Worst - O(n^2)
Average - O(n^2)
Space Complexity - O(1)

This function returns a copy for the sake of it.
"""


def insertion_sort(data: list) -> list:
    data = data[:]

    sorted_index = 0
    while sorted_index != len(data) - 1:
        item = data[sorted_index + 1]
        position = sorted_index
        while position >= 0 and data[position] > item:
            temp = data[position]
            data[position] = item
            data[position + 1] = temp
            position -= 1
        sorted_index += 1


    return data


def run():
    print("Insertion Sort")

    max_value = int(input("Enter maximum value: "))
    data = list(range(max_value))
    shuffle(data)

    print("Before: {}".format(data))
    data = insertion_sort(data)
    print("After: {}".format(data))
