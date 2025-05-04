"""
Module containing implementation for basic sorting algorithms.
"""

from typing import Any
from basic_sort.sort_lib.models.node import Node


class BasicSort:
    """
    Definition for base class of sorting algorithms.
    """

    # Create
    def __init__(self, nodes: list[Node], reverse: bool = False):
        self.nodes: list[Node] = nodes
        self.reverse = reverse

        self.node_count = len(self.nodes)
        self.comp_count = 0
        self.swap_count = 0

    # Read
    def _check_swap_criteria(self, idx_1: int, idx_2: int) -> bool:
        """
        Function to check if swap is required based on value comparison.
        """
        self.comp_count = self.comp_count + 1

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
        self.swap_count = self.swap_count + 1
        self.nodes[idx_1], self.nodes[idx_2] = self.nodes[idx_2], self.nodes[idx_1]
