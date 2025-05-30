"""
Module to test Bubble Sort algorithm.
"""

from node import Node
from bubble_sort import BubbleSort


def main(input_values: list[int], reverse: bool):
    """
    Function to test Bubble Sort algorithm.
    """
    # Create
    print("Sort below input values using Bubble Sort algorithm:")
    print(input_values)

    bbl_sort = BubbleSort(
        nodes=[Node(value) for _, value in enumerate(input_values)],
        reverse=reverse,
    )

    # Update
    print("\nSorting using Bubble Sort...")
    bbl_sort.sort()

    # Read
    print("\nSorted list:")
    print(bbl_sort.to_list())


if __name__ == "__main__":
    print("*" * 10, "Case 1: Sort in ascending order", "*" * 10)
    main(input_values=[4, 2, 6, 5, 1, 3], reverse=False)
    print("*" * 55, "\n\n")

    print("*" * 10, "Case 2: Sort in descending order", "*" * 10)
    main(input_values=[6, 2, 6, 5, 1, 3], reverse=True)
    print("*" * 55)
