"""
Module to test Quick Sort algorithm.
"""

from node import Node
from quick_sort import QuickSort


def main(input_values: list[int], reverse: bool):
    """
    Function to test Quick Sort algorithm.
    """
    # Create
    print("Sort below input values using Quick Sort algorithm:")
    print(input_values)

    quk_sort = QuickSort(
        nodes=[Node(value) for _, value in enumerate(input_values)],
        reverse=reverse,
    )

    # Update
    print("\nSorting using Quick Sort...")
    quk_sort.sort()

    # Read
    print("\nSorted list:")
    print(quk_sort.to_list())


if __name__ == "__main__":
    print("*" * 10, "Case 1: Sort in ascending order", "*" * 10)
    main(input_values=[4, 6, 1, 7, 3, 2, 5], reverse=False)
    print("*" * 55, "\n\n")

    print("*" * 10, "Case 2: Sort in descending order", "*" * 10)
    main(input_values=[6, 2, 6, 5, 1, 3], reverse=True)
    print("*" * 55)
