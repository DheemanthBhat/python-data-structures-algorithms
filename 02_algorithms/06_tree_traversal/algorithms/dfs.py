"""
Module containing implementation for Depth First Search algorithm.
"""

from typing import Any
from data_structures.tree.node import Node


class DepthFirstSearch:
    """
    Definition for Depth First Search algorithm.
    """

    def pre_order(self, curr_node: Node) -> Any:
        """
        Function to traverse Binary tree in pre-order.
        """
        yield curr_node.value

        if curr_node.left is not None:
            yield from self.pre_order(curr_node.left)

        if curr_node.right is not None:
            yield from self.pre_order(curr_node.right)

    def post_order(self, curr_node: Node) -> Any:
        """
        Function to traverse Binary tree in post-order.
        """
        if curr_node.left is not None:
            yield from self.post_order(curr_node.left)

        if curr_node.right is not None:
            yield from self.post_order(curr_node.right)

        yield curr_node.value

    def in_order(self, curr_node: Node) -> Any:
        """
        Function to traverse Binary tree in in-order.
        """
        if curr_node.left is not None:
            yield from self.in_order(curr_node.left)

        yield curr_node.value

        if curr_node.right is not None:
            yield from self.in_order(curr_node.right)
