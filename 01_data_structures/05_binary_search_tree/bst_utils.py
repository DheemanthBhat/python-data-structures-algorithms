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

    def crawl_bst(self, node: Node, child_type: str = None, level: int = 0, par_idx: int = 0):
        """
        Recursive function to compute:
            1. level/height as row index
            2. left/right offset (from parent) as column index
        for each node in a Binary Search Tree.
        """
        # Get total number of possible nodes below current parent.
        curr_tot_nodes = self.get_node_count(self.max_level - level)

        # Initialize child's index.
        col_idx = curr_tot_nodes // 2

        # Based on child's type, calculate its offset from parent.
        if child_type == "L":
            col_idx = par_idx - 1 - col_idx
        elif child_type == "R":
            col_idx = par_idx + 1 + col_idx

        yield level, col_idx, node.value

        # Handle left child.
        if node.left is not None:
            yield from self.crawl_bst(node.left, "L", level + 1, col_idx)

        # Handle right child.
        if node.right is not None:
            yield from self.crawl_bst(node.right, "R", level + 1, col_idx)

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
        print(matrix)
