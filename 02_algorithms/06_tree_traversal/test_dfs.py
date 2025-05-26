"""
Module to test Depth First Search algorithm.
"""

from typing import Any
from data_structures.tree.bst_via_linked_list import BinarySearchTree
from algorithms.dfs import DepthFirstSearch
from utils.bst_utils import BSTUtils


def main(input_values: list[Any]):
    """
    Function to test Depth First Search algorithm.
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

    # Run Depth First Search algorithm on BST.
    dfs = DepthFirstSearch()

    print("\nTree nodes listed in pre-order:")
    pre_results: list[Any] = [value for value in dfs.pre_order(bst.root)]
    print(pre_results)

    print("\nTree nodes listed in post-order:")
    pos_results: list[Any] = [value for value in dfs.post_order(bst.root)]
    print(pos_results)

    print("\nTree nodes listed in in-order:")
    ino_results: list[Any] = [value for value in dfs.in_order(bst.root)]
    print(ino_results)


if __name__ == "__main__":
    print("*" * 15, "Case 1: Complete Binary Tree", "*" * 15)
    main([50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25])
    print("*" * 60, "\n\n")

    print("*" * 15, "Case 2: Skewed Binary Tree", "*" * 15)
    main([50, 60, 40, 55, 70, 45, 80])
    print("*" * 60)
