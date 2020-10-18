from search.binary.binary_search import run as binary_search
from search.linear.linear_search import run as linear_search

from sort.bogo.bogo_sort import run as bogo_sort
from sort.bubble.bubble_sort import run as bubble_sort
from sort.insertion.insertion_sort import run as insertion_sort


algorithms = {
    "Binary Search": binary_search,
    "Linear Search": linear_search,
    "Bogo Sort": bogo_sort,
    "Bubble Sort": bubble_sort,
    "Insertion Sort": insertion_sort
}


def main():
    print("Possible algorithms: ")
    for algorithm in algorithms:
        print(f" * {algorithm}")

    print()
    selected = None
    while selected not in algorithms:
        selected = input("Enter algorithm: ").title()
    print()

    algorithms[selected]()


if __name__ == "__main__":
    main()
