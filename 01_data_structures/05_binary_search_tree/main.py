"""
Module to test Binary Search Tree.
"""

from typing import Any
from utils.bst_utils import BSTUtils
from bst.bst_via_linked_list import BinarySearchTree

# from bst.r_bst_via_linked_list import BinarySearchTree


def main(
    input_values: list[Any],
    lookup_values: list[Any],
    delete_values: list[Any],
    allow_duplicates: bool = False,
    delete_strategy: int = BinarySearchTree.IN_ORDER_SUCCESSOR,
):
    """
    Function to test Binary Search Tree.
    """
    # Create
    print("Initialize empty Binary Search Tree:")
    bst = BinarySearchTree(allow_duplicates, delete_strategy)

    # Update
    print(f"\nInsert below {len(input_values)} values into Binary Search Tree:")
    print(input_values)

    for value in input_values:
        bst.insert(value)

    print("\nDisplay Binary Search Tree:")
    BSTUtils(bst).display_bst()

    # Read
    if len(lookup_values) > 0:
        print(f"\nCheck if values: {lookup_values} exists in Binary Search Tree:")

    for value in lookup_values:
        if value in bst:
            print(f"Value: '{value}' found in BST.")
        else:
            print(f"Value: '{value}' NOT found in BST.")

    # Delete
    for value in delete_values:
        print(f"\nDeleting node with value: {value} from BST...")
        del_status = bst.delete(value)
        if del_status is True:
            print("Binary Search Tree after deleting Node:", value)
            BSTUtils(bst).display_bst()
        else:
            print(f"Node with value: {value} not found in BST.")


if __name__ == "__main__":
    print("*" * 10, "Case 1: Full Binary Tree without duplicates", "*" * 10)
    input_vals = [50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25]
    lookup_vals = [56, 0, -20]
    delete_vals = [36, 75, 56, 30]
    main(input_vals, lookup_vals, delete_vals)
    print("*" * 65, "\n\n")

    print("*" * 18, "Case 2: Skewed Binary Tree without duplicates", "*" * 18)
    input_vals = [47, 21, 76, 18, 27, 52, 82, 25, 29, 24, 26, 28, 30]
    delete_vals = [27, 26, 47]
    main(input_vals, [], delete_vals, delete_strategy=BinarySearchTree.IN_ORDER_PREDECESSOR)
    print("*" * 85, "\n\n")

    print("*" * 10, "Case 3: Skewed Binary Tree with duplicates", "*" * 10)
    input_vals = [50, 60, 40, 50, 60, 45, 60]
    lookup_vals = [60, 0, 45]
    delete_vals = [60, 60, 40, 36]
    main(input_vals, lookup_vals, delete_vals, allow_duplicates=True)
    print("*" * 60)
