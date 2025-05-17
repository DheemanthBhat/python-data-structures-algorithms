"""
Module to test Merge Sort algorithm.
"""

from node import Node
from merge_sort import MergeSort


def main(input_values: list[int], reverse: bool):
    """
    Function to test Merge Sort algorithm.
    """
    # Create
    print("Sort below input values using Merge Sort algorithm:")
    print(input_values)

    mrg_sort = MergeSort(
        nodes=[Node(value) for _, value in enumerate(input_values)],
        reverse=reverse,
    )

    # Update
    print("\nSorting using Merge Sort...")
    sorted_nodes: list[Node] = mrg_sort.sort()

    # Read
    print("\nSorted list:")
    print(mrg_sort.to_list(sorted_nodes))


if __name__ == "__main__":
    print("*" * 10, "Case 1: Sort in ascending order", "*" * 10)
    main(input_values=[4, 2, 6, 5, 1], reverse=False)
    print("*" * 55, "\n\n")

    print("*" * 10, "Case 2: Sort in descending order", "*" * 10)
    main(input_values=[6, 2, 6, 5, 1, 3], reverse=True)
    print("*" * 55)
