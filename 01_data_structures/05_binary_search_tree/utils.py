"""
Module containing utility functions.
"""

from bst_via_linked_list import BinarySearchTree
from node import Node


def get_node_count(level: int):
    """
    Function to get total number of nodes in a
    Binary Search Tree at any level `l`.

    NOTE:
        Formula for total number of nodes in
        a BST at any level/height `h` is:
        `n = 2^h - 1`
    """
    return 2**level - 1


def get_largest_node(bst: BinarySearchTree):
    """
    Function to get largest number in a Binary Search Tree.
    """
    curr_node = bst.root

    while curr_node.right is not None:
        curr_node = curr_node.right

    return curr_node


def create_2d_matrix(rows: int, cols: int, default_value: str = ""):
    """
    Function to create 2D matrix.
    """
    return [[default_value for _ in range(cols)] for __ in range(rows)]


def travel_bst(bst: BinarySearchTree):
    """
    Closure to travel Binary Search Tree.
    """
    bst_level = bst.level

    def next_node(node: Node, level: int = 0, path: str = ""):
        """
        Recursive function to compute level/height (as row index) and
        right offset (as column index) for each node in a Binary Search Tree.
        """
        # Get total number of possible nodes below current level.
        curr_tot_nodes = get_node_count(bst_level - level)

        # Calculate right offset.
        col_idx = curr_tot_nodes // 2
        for curr_level, direction in enumerate(path, start=1):
            if direction == "R":
                tot_left_nodes = get_node_count(bst_level - curr_level)
                col_idx += tot_left_nodes + 1

        yield level, col_idx, node.value

        if node.left is not None:
            yield from next_node(node.left, level + 1, path + "L")

        if node.right is not None:
            yield from next_node(node.right, level + 1, path + "R")

    return next_node


def display_bst(bst: BinarySearchTree):
    """
    Function to display Binary Search Tree.
    """
    # Basic validation of BST.
    if bst is None or bst.root is None:
        print("Tree is empty.")

    print(f"Root: {str(bst.root):<33}")
    print(f"Max level: {bst.level}\n")

    # Get total number of nodes in BST.
    tot_nodes = get_node_count(bst.level)

    # Get Node with largest value in BST.
    largest_node = get_largest_node(bst)
    char_length = len(str(largest_node.value))

    # Create 2 dimensional matrix with full of empty values to contain BST.
    matrix = create_2d_matrix(bst.level, tot_nodes, f"{' ':>{char_length}}")

    # Initialize BST crawler.
    next_node = travel_bst(bst)

    # Fill matrix with values from nodes by traveling BST.
    for row_idx, col_idx, value in next_node(bst.root):
        matrix[row_idx][col_idx] = f"{value:>{char_length}}"

    # Print matrix.
    for row in matrix:
        print(" ".join(row))
