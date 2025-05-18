"""
Module containing implementation for Quick Sort algorithm.
"""

from typing import Any
from node import Node


class QuickSort:
    """
    Definition for Quick Sort.
    """

    # Create
    def __init__(self, nodes: list[Node], reverse: bool = False):
        self.nodes: list[Node] = nodes
        self.reverse: bool = reverse
        self.node_count: int = len(self.nodes)

    # Read
    def _check_swap_criteria(self, idx_1: int, idx_2: int) -> bool:
        """
        Function to check if swap is required based on value comparison.
        """
        if self.reverse is True:
            return self.nodes[idx_1] < self.nodes[idx_2]
        elif self.reverse is False:
            return self.nodes[idx_1] > self.nodes[idx_2]
        else:
            raise ValueError("Invalid value for reverse flag.")

    def to_list(self) -> list[Any]:
        """
        Function to list values in nodes
        """
        return [node.value for node in self.nodes]

    # Update
    def _swap_nodes(self, idx_1: int, idx_2: int):
        """
        Function to swap nodes between indices  `idx_1` and `idx_2`.
        """
        self.nodes[idx_1], self.nodes[idx_2] = self.nodes[idx_2], self.nodes[idx_1]

    def _sort_pivot(self, start_idx: int, end_idx: int) -> int:
        """
        Function to place pivot node at the correct position such that:
            1. LHS: All nodes to its left are smaller (greater when reversed).
            2. RHS: All nodes to its right are greater (smaller when reversed).

        Function returns index of the pivot node after it is correctly placed.
        """
        # Initialize partition index.
        partition_idx: int = start_idx

        # Rearrange nodes to meet target formation.
        for i in range(start_idx + 1, end_idx + 1):
            if self._check_swap_criteria(start_idx, i):
                partition_idx += 1
                self._swap_nodes(partition_idx, i)

        # Place pivot node at the correct position.
        self._swap_nodes(start_idx, partition_idx)

        # Return partition index.
        return partition_idx

    def _quick_sort(self, start_idx: int, end_idx: int):
        """
        Recursive function to sort nodes using Quick Sort
        """
        # STEP 1: Check for base case.
        if end_idx <= start_idx:
            return

        # STEP 2: Place pivot node at its correct position.
        partition_idx = self._sort_pivot(start_idx, end_idx)

        # STEP 3: Sort nodes on LHS of partition index.
        self._quick_sort(start_idx, partition_idx - 1)

        # STEP 4: Sort nodes on RHS of partition index.
        self._quick_sort(partition_idx + 1, end_idx)

    def sort(self) -> list[Node]:
        """
        Function to sort nodes using Quick Sort algorithm.
        """
        return self._quick_sort(start_idx=0, end_idx=self.node_count - 1)
