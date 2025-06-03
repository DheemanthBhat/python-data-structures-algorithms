"""
Module containing implementation for Binary Search Tree data structure.
"""

from typing import Any
from data_structures.tree.node import Node


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

    # Update
    def insert(self, value: Any):
        """
        Function to insert item into a Binary Search Tree.
        """
        """
        STEP 1: Create new node.
        """
        new_node: Node = self._create_node(value)

        """
        STEP 2: Create Binary Search Tree with new node
                as root node if the tree is empty.
        """
        if self.root is None:
            self.root = new_node
            self.level = 1
            return

        """
        STEP 3: Travel (left or right) upto the leaf/half node by comparing input value
                with the value in each node in the path leading up to the target node.
        """
        curr_node: Node = self.root
        tgt_node: Node = None
        curr_level: int = 1

        while curr_node is not None:
            tgt_node = curr_node

            if value >= curr_node.value:
                if value == curr_node.value and self.allow_duplicates is False:
                    return
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

            curr_level += 1

        """
        STEP 4: Attach new node to the left of target node if the input value is
                less than the value in target node otherwise attach it to right.
        """
        if value < tgt_node.value:
            tgt_node.left = new_node
        else:
            tgt_node.right = new_node

        """
        STEP 5: Update level.
        """
        self.level = max(curr_level, self.level)
