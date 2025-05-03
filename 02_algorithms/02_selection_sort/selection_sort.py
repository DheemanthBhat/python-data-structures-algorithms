"""
Module containing implementation for Selection Sort algorithm.
"""

from typing import Any
from node import Node


class SelectionSort:
    """
    Definition for Selection Sort.
    """

    # Create
    def __init__(self, nodes: list[Node], reverse: bool = False):
        self.nodes: list[Node] = nodes
        self.reverse = reverse

        self.node_count = len(self.nodes)

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

    def sort(self):
        """
        Function to sort nodes using Selection Sort algorithm.
        """
        for i in range(0, self.node_count - 1):
            target_idx = i

            # Locate target (min/max) index.
            for j in range(i + 1, self.node_count):
                if self._check_swap_criteria(idx_1=target_idx, idx_2=j) is True:
                    target_idx = j

            if i != target_idx:
                # Swap target node with current node.
                self._swap_nodes(i, target_idx)
