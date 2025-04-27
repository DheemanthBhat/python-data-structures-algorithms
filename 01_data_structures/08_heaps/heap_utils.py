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
            raise ValueError("Heap is empty.")

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

    def get_left_child(self, curr_idx: int) -> tuple[Node, int] | tuple[None, None]:
        """
        Function to get left child.
        """
        lc_idx = self.heap.__get_left_child_idx__(curr_idx)
        if lc_idx > (len(self.heap.nodes) - 1):
            return None, None

        return self.heap.nodes[lc_idx], lc_idx

    def get_right_child(self, curr_idx: int) -> tuple[Node, int] | tuple[None, None]:
        """
        Function to get right child.
        """
        rc_idx = self.heap.__get_right_child_idx__(curr_idx)
        if rc_idx > (len(self.heap.nodes) - 1):
            return None, None

        return self.heap.nodes[rc_idx], rc_idx

    def get_max_char_len(self) -> int:
        """
        Function to get length of lengthiest value
        (by number of characters) in Heap.
        """
        # Get character length of value in each Node in the Heap.
        char_lens = [len(str(node.value)) for node in self.heap.nodes]
        return max(char_lens)

    def crawl_heap(self, curr_idx: int = 0, level: int = 0, path: str = ""):
        """
        Function to crawl heap.

        TODO:
        This is quick adaptation of `bst_utils.crawl_bst()`.
        This function must be simplified or rewritten for Heap.
        """
        curr_node: Node = self.heap.nodes[curr_idx]

        # Get total number of possible nodes below current level.
        curr_tot_nodes = self.get_node_count(self.max_level - level)

        # Calculate right offset.
        col_idx = curr_tot_nodes // 2
        for curr_level, direction in enumerate(path, start=1):
            if direction == "R":
                tot_left_nodes = self.get_node_count(self.max_level - curr_level)
                col_idx += tot_left_nodes + 1

        yield level, col_idx, curr_node.value

        left_node, left_idx = self.get_left_child(curr_idx)
        if left_node is not None:
            yield from self.crawl_heap(left_idx, level + 1, path + "L")

        right_node, right_idx = self.get_right_child(curr_idx)
        if right_node is not None:
            yield from self.crawl_heap(right_idx, level + 1, path + "R")

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
