"""
Module to test Insertion Sort algorithm.
"""

from prettytable import PrettyTable
from basic_sort.sort_lib.models.node import Node
from basic_sort.sort_lib.algorithms.bubble_sort import BubbleSort
from basic_sort.sort_lib.algorithms.selection_sort import SelectionSort
from basic_sort.sort_lib.algorithms.insertion_sort import InsertionSort


def main(input_values: list[int], reverse: bool):
    """
    Function to test Insertion Sort algorithm.
    """
    # Create
    print("Sort below input values using Insertion Sort algorithm:")
    print(input_values)

    bbl_sort = BubbleSort(
        nodes=[Node(value) for _, value in enumerate(input_values)],
        reverse=reverse,
    )

    sel_sort = SelectionSort(
        nodes=[Node(value) for _, value in enumerate(input_values)],
        reverse=reverse,
    )

    ins_sort = InsertionSort(
        nodes=[Node(value) for _, value in enumerate(input_values)],
        reverse=reverse,
    )

    # Update
    bbl_sort.sort()
    sel_sort.sort()
    ins_sort.sort()

    # Display result
    table = PrettyTable(field_names=["Algorithm", "Comparison count", "Swap count"], align="l")
    table.add_rows(
        [
            ["Bubble sort", bbl_sort.comp_count, bbl_sort.swap_count],
            ["Selection sort", sel_sort.comp_count, sel_sort.swap_count],
            ["Insertion sort", ins_sort.comp_count, ins_sort.swap_count],
        ]
    )

    print("\nComparison result:")
    print(table)


if __name__ == "__main__":
    print("*" * 15, "Case 1: Random array", "*" * 15)
    main(input_values=[4, 2, 6, 5, 1, 3], reverse=False)
    print("*" * 55, "\n\n")

    print("*" * 10, "Case 2: Descending to Ascending", "*" * 10)
    main(input_values=[6, 5, 4, 3, 2, 1], reverse=False)
    print("*" * 55, "\n\n")

    print("*" * 12, "Case 3: Already sorted array", "*" * 12)
    main(input_values=[6, 5, 4, 3, 2, 1], reverse=True)
    print("*" * 55)
