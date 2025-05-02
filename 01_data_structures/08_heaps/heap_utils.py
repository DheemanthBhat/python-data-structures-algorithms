"""
Module containing Heap utility.
"""

from math import log2, ceil
from node import Node
from heap_ds import Heap
from heap_matrix import Matrix


class HeapUtils:
    """
    Definition for heap utilities.
    """

    def __init__(self, heap: Heap):
        if heap is None or len(heap.nodes) == 0:
            raise ValueError("Heap is empty!")

        self.heap = heap
        self.max_level = ceil(log2(len(heap.nodes) + 1))

    def get_level(self, idx: int):
        """
        Function get level of node in Tree based on item index in Heap.

        NOTE:
            1. Formula to get level/height `h` in a Perfect
               Binary Tree based on item count/index `n` is:
               `h = log_base_2(n + 1)`
            2. Height `h` is ceiled if the Tree is not Perfect Binary Tree.
        """
        return ceil(log2(idx + 2))

    def get_node_count(self, level: int = -1):
        """
        Function to get total number of nodes in a
        Perfect Binary Tree at any level `l`.

        NOTE:
            Formula for total number of nodes in
            a BST at any level/height `h` is:
            `n = 2^h - 1`
        """
        level = self.max_level if level == -1 else level

        return 2**level - 1

    def get_max_char_len(self) -> int:
        """
        Function to get length of lengthiest value
        (by number of characters) in Heap.
        """
        # Get character length of value in each Node in the Heap.
        char_lens = [len(str(node.value)) for node in self.heap.nodes]
        return max(char_lens)

    def crawl_heap(
        self,
        node_idx: int = 0,
        child_type: str = None,
        level: int = 0,
        par_idx: int = -1,
    ):
        """
        Function to crawl heap.

        TODO:
        This is quick adaptation of `bst_utils.crawl_bst()`.
        This function must be simplified or rewritten for Heap.
        """
        node: Node = self.heap.nodes[node_idx]

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
        left_node_idx = self.heap.__get_left_child_idx__(node_idx)
        if left_node_idx != -1:
            yield from self.crawl_heap(left_node_idx, "L", level + 1, col_idx)

        # Handle right child.
        right_node_idx = self.heap.__get_right_child_idx__(node_idx)
        if right_node_idx != -1:
            yield from self.crawl_heap(right_node_idx, "R", level + 1, col_idx)

    def display_heap(self):
        """
        Function to display heap.
        """
        print(f"Root: {self.heap.nodes[0]}")
        print(f"Max level: {self.max_level}\n")

        # Initialize 2D Matrix with:
        #   1. Tree Height as row count.
        #   2. Total number of nodes in Perfect Binary Tree as column count.
        #   3. Maximum character length of values in Heap.
        matrix = Matrix(
            row_count=self.max_level,
            col_count=self.get_node_count(self.max_level),
            max_char_len=self.get_max_char_len(),
        )

        # Fill matrix with values from nodes by crawling Heap.
        for row_idx, col_idx, value in self.crawl_heap():
            matrix[row_idx][col_idx] = value

        # Print matrix.
        print(matrix)
