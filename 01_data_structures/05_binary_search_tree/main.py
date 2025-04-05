"""
Module to test Binary Search Tree.
"""

import utils
from bst_via_linked_list import BinarySearchTree


def main():
    """
    Function to test Binary Search Tree.
    """
    # Create
    print("\nInitialize empty Binary Search Tree:")
    bst = BinarySearchTree()

    # Update
    input_values = [50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25]
    print("\nInsert below values into Binary Search Tree:")
    print(input_values)

    for value in input_values:
        bst.insert(value)

    print("\nDisplay Binary Search Tree:")
    utils.display_bst(bst)

    # Read
    lookup_values = [56, 0, -20]
    print(f"\nCheck if values: {lookup_values} exists in Binary Search Tree:")
    for value in lookup_values:
        print(f"Value: {value} {'present' if value in bst else 'absent'}")


if __name__ == "__main__":
    main()
