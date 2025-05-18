"""
Module to test Insertion Sort algorithm.
"""

from prettytable import PrettyTable
from basic_sort.sort_lib.models.node import Node
from basic_sort.sort_lib.algorithms.bubble_sort import BubbleSort
from basic_sort.sort_lib.algorithms.selection_sort import SelectionSort
from basic_sort.sort_lib.algorithms.insertion_sort import InsertionSort
from basic_sort.sort_lib.algorithms.quick_sort import QuickSort


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

    quk_sort = QuickSort(
        nodes=[Node(value) for _, value in enumerate(input_values)],
        reverse=reverse,
    )

    # Update
    bbl_sort.sort()
    sel_sort.sort()
    ins_sort.sort()
    quk_sort.sort()

    # Display result
    table = PrettyTable(
        field_names=["Algorithm", "Comparison count", "Swap count", "Sort result"],
        align="l",
    )
    table.add_rows(
        [
            ["Bubble sort", bbl_sort.comp_count, bbl_sort.swap_count, bbl_sort.to_list()],
            ["Selection sort", sel_sort.comp_count, sel_sort.swap_count, sel_sort.to_list()],
            ["Insertion sort", ins_sort.comp_count, ins_sort.swap_count, ins_sort.to_list()],
            ["Quick sort", quk_sort.comp_count, quk_sort.swap_count, quk_sort.to_list()],
        ]
    )

    print("\nComparison result:")
    print(table)


if __name__ == "__main__":
    print("*" * 25, "Case 1: Random array", "*" * 25)
    main(input_values=[4, 2, 6, 5, 1, 3], reverse=False)
    print("*" * 72, "\n\n")

    print("*" * 20, "Case 2: Descending to Ascending", "*" * 20)
    main(input_values=[6, 5, 4, 3, 2, 1], reverse=False)
    print("*" * 72, "\n\n")

    print("*" * 20, "Case 3: Already sorted array", "*" * 20)
    main(input_values=[6, 5, 4, 3, 2, 1], reverse=True)
    print("*" * 72, "\n\n")
