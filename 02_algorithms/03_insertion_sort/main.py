"""
Module to test Insertion Sort algorithm.
"""

from node import Node
from insertion_sort import InsertionSort


def main(input_values: list[int], reverse: bool):
    """
    Function to test Insertion Sort algorithm.
    """
    # Create
    print("Sort below input values using Insertion Sort algorithm:")
    print(input_values)

    ins_sort = InsertionSort(
        nodes=[Node(value) for _, value in enumerate(input_values)],
        reverse=reverse,
    )

    # Update
    print("\nSorting using Insertion Sort...")
    ins_sort.sort()

    # Read
    print("\nSorted list:")
    print(ins_sort.to_list())


if __name__ == "__main__":
    print("*" * 10, "Case 1: Sort in ascending order", "*" * 10)
    main(input_values=[4, 2, 6, 5, 1, 3], reverse=False)
    print("*" * 55, "\n\n")

    print("*" * 10, "Case 2: Sort in descending order", "*" * 10)
    main(input_values=[6, 2, 6, 5, 1, 3], reverse=True)
    print("*" * 55)
