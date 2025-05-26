"""
Module to test Binary Search Tree.
"""

from typing import Any
from bst.bst_via_linked_list import BinarySearchTree
from utils.bst_utils import BSTUtils


def main(input_values: list[Any], lookup_values: list[Any], allow_duplicates: bool):
    """
    Function to test Binary Search Tree.
    """
    # Create
    print("Initialize empty Binary Search Tree:")
    bst = BinarySearchTree(allow_duplicates)

    # Update
    print(f"\nInsert below {len(input_values)} values into Binary Search Tree:")
    print(input_values)

    for value in input_values:
        bst.insert(value)

    bst_utils = BSTUtils(bst)
    print("\nDisplay Binary Search Tree:")
    bst_utils.display_bst()

    # Read
    print(f"\nCheck if values: {lookup_values} exists in Binary Search Tree:")
    for value in lookup_values:
        if value in bst:
            print(f"Value: '{value}' found in BST.")
        else:
            print(f"Value: '{value}' NOT found in BST.")


if __name__ == "__main__":
    print("*" * 25, "Case 1: Reject duplicates", "*" * 25)
    input_vals = [50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25]
    lookup_vals = [56, 0, -20]
    main(input_vals, lookup_vals, False)
    print("*" * 80, "\n\n")

    print("*" * 25, "Case 2: Allow duplicates", "*" * 25)
    input_vals = [50, 60, 40, 50, 60, 45, 60]
    lookup_vals = [60, 0, 45]
    main(input_vals, lookup_vals, True)
    print("*" * 80)
