"""
Module to test Binary Search Tree.
"""

from bst_via_linked_list import BinarySearchTree


def display_bst(bst: BinarySearchTree):
    """
    Function to display Stack as list.
    """
    print(f"Root: {str(bst.root):<33} Level: {bst.level}")


def main():
    """
    Function to test Binary Search Tree.
    """
    # Create
    print("\nInitialize empty Binary Search Tree:")
    bst = BinarySearchTree()

    # Update
    input_values = [1, 40, 20, 10, 50, 0]
    print(f"\nInsert values {input_values} into Binary Search Tree:")
    for value in input_values:
        bst.insert(value)

    display_bst(bst)

    # Read
    lookup_values = [10, 0, -20]
    print(f"\nCheck if values: {lookup_values} exists in Binary Search Tree:")
    for value in lookup_values:
        print(f"Value: {value} {'present' if value in bst else 'absent'}")


if __name__ == "__main__":
    main()
