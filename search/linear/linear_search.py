from random import shuffle

"""
Will search a list of integers for a value using a linear search algorithm.

Does not require a sorted list to be passed in.
Returns -1 if item is not found

Linear Search:
Best - O(1)
Worst - O(n)
Average - O(n)
Space Complexity - O(1)
"""


def search(data: list, value: int) -> int:
    for i in range(len(data)):
        if data[i] == value:
            return i
    return -1


def run():
    print("Linear Search")

    data_size = int(input("Enter the max value: "))
    data = list(range(data_size))
    shuffle(data)
    value = int(input("Enter value to search for: "))

    print("Searching for {} in {}".format(value, data))
    result = search(data, value)
    print("Not found in list" if result == -1 else "Found at index {}".format(result))
