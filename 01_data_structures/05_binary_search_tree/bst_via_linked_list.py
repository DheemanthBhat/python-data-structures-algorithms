"""
Module containing implementation for Binary Search Tree data structure.
"""

from typing import Any
from node import Node


class BinarySearchTree:
    """
    Definition for Binary Search Tree data structure.
    """

    # Create
    def __init__(self, allow_duplicates: bool = False):
        self.root: Node = None
        self.level: int = 0
        self.allow_duplicates: bool = allow_duplicates

    def __create_node__(self, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(value)
        return new_node

    def __contains__(self, value: Any) -> bool:
        """
        Function to check if Binary Search Tree
        contains an item matching the `value`.
        """
        curr_node = self.root
        while curr_node is not None:
            if curr_node.value == value:
                return True
            elif value < curr_node.value:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right

        return False

    # Update
    def insert(self, value: Any):
        """
        Function to insert item into a Binary Search Tree.
        """
        """
        STEP 1: Create new node.
        """
        new_node: Node = self.__create_node__(value)

        """
        STEP 2: Create Binary Search Tree with new node
                as root node if the tree is empty.
        """
        if self.root is None:
            self.root = new_node
            self.level = 1
            return

        """
        STEP 3: Travel (left or right) upto the leaf node by comparing input value
                with the value in each node in the path leading to the leaf node.
        """
        curr_node: Node = self.root
        leaf_node: Node = None
        curr_level: int = 1

        while curr_node is not None:
            leaf_node = curr_node

            if value >= curr_node.value:
                if value == curr_node.value and self.allow_duplicates is False:
                    return
                curr_node = curr_node.right
            else:
                curr_node = curr_node.left

            curr_level += 1

        """
        STEP 4: Attach new node to the left of leaf node if the input value is
                less than the value in leaf node otherwise attach it to right.
        """
        if value < leaf_node.value:
            leaf_node.left = new_node
        else:
            leaf_node.right = new_node

        """
        STEP 5: Update level.
        """
        self.level = max(curr_level, self.level)
