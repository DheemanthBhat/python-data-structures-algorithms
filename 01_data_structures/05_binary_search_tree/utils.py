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


def travel_bst(node: Node, height: int = 0, path: str = ""):
    """
    Recursive function to travel (reach every node) Binary Search Tree.
    """
    yield node.value, height, path

    if node.left is not None:
        yield from travel_bst(node.left, height + 1, path + "L")

    if node.right is not None:
        yield from travel_bst(node.right, height + 1, path + "R")


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

    # Create matrix grid with full of empty values to contain BST.
    matrix = [[f"{' ':>{char_length}}" for _ in range(tot_nodes)] for __ in range(bst.level)]

    # Fill matrix with values from nodes by traveling BST.
    for value, level, path in travel_bst(bst.root):
        # Get total number of nodes at current level.
        curr_tot_nodes = get_node_count(bst.level - level)
        c_idx = curr_tot_nodes // 2

        curr_level = 1
        for direction in path:
            if direction == "R":
                tot_left_nodes = get_node_count(bst.level - curr_level)
                c_idx += tot_left_nodes + 1
            curr_level += 1

        matrix[level][c_idx] = f"{value:>{char_length}}"

    # Print matrix.
    for row in matrix:
        print(" ".join(row))
