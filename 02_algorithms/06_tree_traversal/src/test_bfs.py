"""
Module to test Breadth First Search algorithm.
"""

from typing import Any
from src.data_structures.tree.bst_via_linked_list import BinarySearchTree
from src.algorithms.bfs import BreadthFirstSearch
from src.utils.bst_utils import BSTUtils


def main(input_values: list[Any]):
    """
    Function to test Breadth First Search algorithm.
    """

    # Build a binary tree (BST for example).
    bst = BinarySearchTree()

    # Add nodes to Binary Tree.
    print(f"Create Binary Search Tree with below {len(input_values)} values:")
    print(input_values)

    for value in input_values:
        bst.insert(value)

    # Display Tree
    bst_utils = BSTUtils(bst)
    print("\nDisplay Binary Tree:")
    bst_utils.display_bst()

    # Run Breadth First Search algorithm on BST.
    bfs = BreadthFirstSearch(root_node=bst.root)
    results = bfs.tree_traversal()

    print("\nTree as list:")
    print(results)


if __name__ == "__main__":
    print("*" * 15, "Case 1: Complete Binary Tree", "*" * 15)
    main([50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25])
    print("*" * 60, "\n\n")

    print("*" * 15, "Case 2: Skewed Binary Tree", "*" * 15)
    main([50, 60, 40, 55, 70, 45, 80])
    print("*" * 60)
