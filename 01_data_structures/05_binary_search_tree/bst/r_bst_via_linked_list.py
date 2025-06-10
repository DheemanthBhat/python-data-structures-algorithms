"""
Module containing implementation for recursive Binary Search Tree data structure.
"""

from typing import Any
from bst.node import Node


class BinarySearchTree:
    """
    Definition for Binary Search Tree data structure with recursive implementation.
    """

    # Delete strategies.
    IN_ORDER_SUCCESSOR: int = 1
    IN_ORDER_PREDECESSOR: int = 2

    # Create
    def __init__(
        self,
        allow_duplicates: bool = False,
        delete_strategy: int = IN_ORDER_SUCCESSOR,
    ):
        self.root: Node = None
        self.level: int = 0
        self.allow_duplicates: bool = allow_duplicates
        self.delete_strategy = delete_strategy

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

    def get_min(self, cur_node: Node) -> Node:
        """
        Function return node with smallest value.
        """
        while cur_node.left is not None:
            cur_node = cur_node.left

        return cur_node

    def get_max(self, cur_node: Node) -> Node:
        """
        Function return node with largest value.
        """
        while cur_node.right is not None:
            cur_node = cur_node.right

        return cur_node

    def _get_successor(self, curr_node: Node) -> Node:
        """
        Function to find and return successor node from its
        parent node based on pre-selected delete strategy.
        """
        if self.delete_strategy == self.IN_ORDER_SUCCESSOR:
            # Get in-order-successor.
            return self.get_min(curr_node.right)
        elif self.delete_strategy == self.IN_ORDER_PREDECESSOR:
            # Get in-order-predecessor.
            return self.get_max(curr_node.left)
        else:
            raise ValueError(f"Invalid delete strategy: {self.delete_strategy}")

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

    # Delete
    def __delete(self, tgt_node: Node):
        """
        Recursive function to delete the node in BST matching the `value`.
        """
        # Case #1: Leaf node.
        if tgt_node.left is None and tgt_node.right is None:
            return None

        # Case #2: Half node.
        elif tgt_node.left is None:
            return tgt_node.right
        elif tgt_node.right is None:
            return tgt_node.left

        # Case #3: Full node.
        elif tgt_node.left is not None and tgt_node.right is not None:
            ssr_node = self._get_successor(tgt_node)
            ssr_node.left, ssr_node.right = tgt_node.left, tgt_node.right

    def __locate(self, curr_node: Node, value: Any):
        """
        Recursive function to locate the node in BST matching the `value`.
        """
        if curr_node is None:
            return None
        elif value == curr_node.value:
            curr_node = self.__delete(curr_node)
        elif value < curr_node.value:
            curr_node.left = self.__locate(curr_node.left, value)
        elif value > curr_node.value:
            curr_node.right = self.__locate(curr_node.right, value)

        return curr_node

    def delete(self, value: Any) -> bool:
        """
        Function to delete the node in BST matching the `value`.
        """
        tgt_node = self.__locate(self.root, value)

        if tgt_node is None:
            return False

        return True
