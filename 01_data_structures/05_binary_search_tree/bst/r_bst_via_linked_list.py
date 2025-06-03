"""
Module containing implementation for recursive Binary Search Tree data structure.
"""

from typing import Any
from bst.node import Node


class BinarySearchTree:
    """
    Definition for Binary Search Tree data structure.
    """

    # Create
    def __init__(self, allow_duplicates: bool = False):
        self.root: Node = None
        self.level: int = 0
        self.allow_duplicates: bool = allow_duplicates

    def _create_node(self, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(value)
        return new_node

    # Read
    def _contains(self, curr_node: Node, value: Any):
        """
        Recursive function to check if Binary Search
        Tree contains an item matching the `value`.
        """
        if curr_node is None:
            return False
        elif value == curr_node.value:
            return True
        elif value < curr_node.value:
            return self._contains(curr_node.left, value)
        elif value > curr_node.value:
            return self._contains(curr_node.right, value)

        return False

    def __contains__(self, value: Any) -> bool:
        """
        Function to check if Binary Search Tree
        contains an item matching the `value`.
        """
        return self._contains(self.root, value)

    # Update
    def _insert(
        self,
        par_node: Node,
        curr_node: Node,
        new_node: Node,
        level: int = 1,
    ) -> tuple[Node, int]:
        """
        Recursive function to insert item into a Binary Search Tree.
        """
        # Create Binary Search Tree with new node
        # as root node if the parent is empty.
        if par_node is None:
            self.root = new_node
            self.level = 1
            return None, None

        if curr_node is None:
            return par_node, level

        elif new_node.value < curr_node.value:
            return self._insert(curr_node, curr_node.left, new_node, level + 1)

        elif new_node.value >= curr_node.value:
            if new_node.value == curr_node.value and self.allow_duplicates is False:
                return None, None

            return self._insert(curr_node, curr_node.right, new_node, level + 1)

    def insert(self, value: Any):
        """
        Function to insert item into a Binary Search Tree.
        """
        """
        STEP 1: Create new node.
        """
        new_node: Node = self._create_node(value)

        """
        STEP 2: Recursively travel (left or right) upto the leaf/half node by comparing input
                value with the value in each node in the path leading up to the target node.
        """
        tgt_node: Node = None
        curr_level: int = 1

        tgt_node, curr_level = self._insert(self.root, self.root, new_node, curr_level)

        if tgt_node is None:
            return

        """
        STEP 3: Attach new node to the left of target node if the input value is
                less than the value in target node otherwise attach it to right.
        """
        if value < tgt_node.value:
            tgt_node.left = new_node
        else:
            tgt_node.right = new_node

        """
        STEP 4: Update level.
        """
        self.level = max(curr_level, self.level)
