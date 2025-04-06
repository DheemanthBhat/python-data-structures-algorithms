"""
Module containing Binary Search Tree utility.
"""

from node import Node
from bst_via_linked_list import BinarySearchTree
from bst_matrix import Matrix


class BSTUtils:
    """
    Definition for Binary search tree utilities.
    """

    def __init__(self, bst: BinarySearchTree):
        # Basic non empty validation of BST.
        if bst is None or bst.root is None:
            raise ValueError("Tree is empty.")

        self.bst: BinarySearchTree = bst
        self.max_level = self.bst.level

    def get_node_count(self, level: int = -1):
        """
        Function to get total number of nodes in a
        Binary Search Tree at any level `l`.

        NOTE:
            Formula for total number of nodes in
            a BST at any level/height `h` is:
            `n = 2^h - 1`
        """
        level = self.max_level if level == -1 else level

        return 2**level - 1

    def get_largest_node(self):
        """
        Function to get largest number in a Binary Search Tree.
        """
        curr_node: Node = self.bst.root

        while curr_node.right is not None:
            curr_node = curr_node.right

        return curr_node

    def crawl_bst(self, node: Node, level: int = 0, path: str = ""):
        """
        Recursive function to compute level/height (as row index) and
        right offset (as column index) for each node in a Binary Search Tree.
        """
        # Get total number of possible nodes below current level.
        curr_tot_nodes = self.get_node_count(self.max_level - level)

        # Calculate right offset.
        col_idx = curr_tot_nodes // 2
        for curr_level, direction in enumerate(path, start=1):
            if direction == "R":
                tot_left_nodes = self.get_node_count(self.max_level - curr_level)
                col_idx += tot_left_nodes + 1

        yield level, col_idx, node.value

        if node.left is not None:
            yield from self.crawl_bst(node.left, level + 1, path + "L")

        if node.right is not None:
            yield from self.crawl_bst(node.right, level + 1, path + "R")

    def display_bst(self):
        """
        Function to display Binary Search Tree.
        """
        print(f"Root: {str(self.bst.root):<33}")
        print(f"Max level: {self.max_level}\n")

        # Initialize 2D Matrix with height as row count and total number of nodes as column count.
        matrix = Matrix(bst=self.bst, row_count=self.max_level, col_count=self.get_node_count())

        # Fill matrix with values from nodes by crawling entire BST.
        for row_idx, col_idx, value in self.crawl_bst(self.bst.root):
            matrix[row_idx][col_idx] = value

        # Print matrix.
        for row in matrix:
            print(" ".join(row))
