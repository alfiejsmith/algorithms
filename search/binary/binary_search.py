"""
Will search a list of integers for a value using a binary search algorithm.

Requires a sorted list to be passed in.
Works recursively
Returns -1 if item is not found

Binary Search:
Best - O(1)
Worst - O(log n)
Average - O(log n)
Space Complexity - O(1)
"""


def search_recursive(data: list, value: int, lower: int = 0, upper: int = -1) -> int:
    if upper == -1: # Will be -1 the first time as long as the upper wasn't specified (intended usage)
        upper = len(data) - 1
    elif upper < lower:
        return -1
    """
    Getting the middle value using an integer divide (floor divide)
    """
    middle = (lower + upper) // 2

    data_value = data[middle]
    if data_value == value:
        return middle
    elif data_value > value:
        return search_recursive(data, value, lower, middle - 1)
    else:
        return search_recursive(data, value, middle + 1, upper)


def search_normal(data: list, value: int):
    lower, upper = 0, len(data) - 1

    while lower <= upper:
        middle = (lower + upper) // 2
        data_value = data[middle]
        if data_value == value:
            return middle
        elif data_value > value:
            upper = middle - 1
        else:
            lower = middle + 1

    return -1


def run():
    print("Binary Search")
    print("Would you like to run it recursively or non-recursively?\n")

    selected = None
    while selected not in ['recursively', 'non-recursively']:
        selected = input("Option: ").lower()

    data_size = int(input("Enter the max value: "))
    data = list(range(data_size))
    value = int(input("Enter a value to search for: "))

    print("Looking for {} in {}".format(value, data))

    if selected == 'recursively':
        result = search_recursive(data, value)
        print("Not found in list" if result == -1 else "Found at index {}".format(result))
    else:
        result = search_normal(data, value)
        print("Not found in list" if result == -1 else "Found at index {}".format(result))