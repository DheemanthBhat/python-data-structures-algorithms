"""
Module containing implementation for Heap data structure.
"""

from typing import Any
from node import Node


class Heap:
    """
    Definition for Heap.
    """

    MAX_HEAP: int = 1
    MIN_HEAP: int = 2

    # Create
    def __init__(self, heap_type: int = MAX_HEAP):
        self.nodes: list[Node] = list()
        self.heap_type = heap_type

    def __create_node__(self, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(value)
        return new_node

    # Read
    def __meets_criteria__(self, par_node: Node, curr_node: Node):
        """
        Function to check if Heap criteria is met.
            1. Max Heap: Value in parent node must be greater than current node.
            2. Min Heap: Value in parent node must be less than current node.
        """
        if self.heap_type == self.MAX_HEAP:
            return True if par_node.value < curr_node.value else False

        if self.heap_type == self.MIN_HEAP:
            return True if par_node.value > curr_node.value else False

        raise ValueError("Failed to meet Heap criteria.")

    def __get_parent_idx__(self, curr_idx: int) -> int | None:
        """
        Function to get parent's index using current node's index.
        """
        if curr_idx <= 0:
            raise ValueError("Input index must be greater than zero.")

        return int((curr_idx - 1) // 2)

    def __get_left_child_idx__(self, curr_idx: int) -> int:
        """
        Function to get left child's index using current node's index.
        """
        if curr_idx < 0:
            raise ValueError("Input index cannot be less than zero.")

        return int((curr_idx * 2) + 1)

    def __get_right_child_idx__(self, curr_idx: int) -> int:
        """
        Function to get right child's index using current node's index.
        """
        if curr_idx < 0:
            raise ValueError("Input index cannot be less than zero.")

        return int((curr_idx * 2) + 2)

    def to_list(self):
        """
        Function to print heap as list.
        """
        return [node.value for node in self.nodes]

    # Update
    def __swap_nodes__(self, idx_1: int, idx_2: int):
        """
        Function to swap nodes between indices `idx_1` and `idx_2`.
        """
        self.nodes[idx_1], self.nodes[idx_2] = self.nodes[idx_2], self.nodes[idx_1]

    def insert(self, value: Any):
        """
        Function to insert item into Heap.
        """
        """
        STEP 1: Add item into Heap.
        """
        new_node: Node = self.__create_node__(value)
        self.nodes.append(new_node)

        if len(self.nodes) < 2:
            return

        """
        STEP 2: Swap with parent if value is larger than parent.
        """
        curr_idx: int = len(self.nodes) - 1
        par_idx = self.__get_parent_idx__(curr_idx)
        par_node: Node = self.nodes[par_idx]

        while curr_idx != 0 and self.__meets_criteria__(par_node, new_node):
            # Swap current node with parent node.
            self.__swap_nodes__(curr_idx, par_idx)

            # Update pointers.
            curr_idx = par_idx
            par_idx = self.__get_parent_idx__(par_idx) if par_idx > 0 else 0
            par_node = self.nodes[par_idx]

    # Delete
    def remove(self):
        """
        Function to remove root node from Heap.
        """
