"""
Module containing implementation for Merge Sort algorithm.
"""

from typing import Any
from node import Node


class MergeSort:
    """
    Definition for Merge Sort.
    """

    # Create
    def __init__(self, nodes: list[Node], reverse: bool = False):
        self.nodes: list[Node] = nodes
        self.reverse = reverse

        self.node_count = len(self.nodes)

    # Read
    def _check_sort_criteria(self, node_1: Node, idx_1: int, node_2: Node, idx_2: int) -> bool:
        """
        Function to check if swap is required based on value comparison.
        """
        n1_idx, n2_idx = None, None

        if self.reverse is True:
            if node_1 > node_2:
                n1_idx = idx_1
            else:
                n2_idx = idx_2

        elif self.reverse is False:
            if node_1 < node_2:
                n1_idx = idx_1
            else:
                n2_idx = idx_2

        else:
            raise ValueError("Invalid value for reverse flag.")

        return n1_idx, n2_idx

    def to_list(self, nodes: list[Node] | None) -> list[Any]:
        """
        Function to list values in nodes.
        """
        nodes: list[Node] = nodes or self.nodes
        return [node.value for node in nodes]

    # Update
    def _split(self, nodes: list[Node]):
        """
        Function to split list into two smaller list until the list size is one.
        """
        if (node_count := len(nodes)) > 1:
            split_1 = nodes[0 : node_count // 2]
            split_2 = nodes[node_count // 2 :]

            yield from self._split(split_1)
            yield from self._split(split_2)

            yield split_1, split_2

    def _merge(self, split_1: list[Node], split_2: list[Node]):
        """
        Function to merge two sorted splits `split_1` and `split_2`.
        """
        sorted_nodes = []

        i: int = 0
        j: int = 0
        while i < len(split_1) and j < len(split_2):
            idx_1, idx_2 = self._check_sort_criteria(split_1[i], i, split_2[j], j)

            if idx_1 is not None:
                sorted_nodes.append(split_1[i])
                i += 1
            elif idx_2 is not None:
                sorted_nodes.append(split_2[j])
                j += 1

        if i != len(split_1):
            sorted_nodes += split_1[i:]

        if j != len(split_2):
            sorted_nodes += split_2[j:]

        return sorted_nodes

    def sort(self):
        """
        Function to sort nodes using Merge Sort algorithm.
        """
        sorted_nodes = []
        for split_1, split_2 in self._split(self.nodes):
            print("\nSplit 1:", split_1)
            print("Split 2:", split_2)

            sorted_nodes = self._merge(split_1, split_2)

        return sorted_nodes
