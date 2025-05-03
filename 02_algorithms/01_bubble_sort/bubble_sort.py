"""
Module containing implementation for Bubble Sort algorithm.
"""

from typing import Any
from node import Node


class BubbleSort:
    """
    Definition for Bubble Sort algorithm.
    """

    # Create
    def __init__(self, nodes: list[Node], reverse: bool = False):
        self.nodes: list[Node] = nodes
        self.reverse = reverse

        self.node_count = len(self.nodes)

    # Read
    def _check_swap_criteria(self, idx: int) -> bool:
        """
        Function to check if swap is required based on value comparison.
        """
        if self.reverse is True:
            return self.nodes[idx] < self.nodes[idx + 1]
        elif self.reverse is False:
            return self.nodes[idx] > self.nodes[idx + 1]
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
        Function to swap Nodes `node_1` and `node_2`.
        """
        self.nodes[idx_1], self.nodes[idx_2] = self.nodes[idx_2], self.nodes[idx_1]

    def sort(self):
        """
        Function to sort nodes using Bubble Sort algorithm.
        """
        for i in range(1, self.node_count):
            for j in range(0, self.node_count - i):
                if self._check_swap_criteria(idx=j) is True:
                    self._swap_nodes(j, j + 1)
