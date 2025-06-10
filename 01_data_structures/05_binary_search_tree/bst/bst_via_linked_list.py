"""
Module containing implementation for Binary Search Tree data structure.
"""

from typing import Any
from bst.node import Node


class BinarySearchTree:
    """
    Definition for Binary Search Tree data structure.
    """

    # Delete strategies.
    IN_ORDER_SUCCESSOR: int = 1
    IN_ORDER_PREDECESSOR: int = 2

    # Directions.
    LEFT: int = 1
    RIGHT: int = 2

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
    def _get_family_tree(self, value: Any) -> tuple[Node, Node, int]:
        """
        Function to return following nodes of a node matching the `value`.
            1. Parent node
            2. Current node.
        """
        par_node: Node = None
        curr_node: Node = self.root
        direction: int = 0

        while curr_node is not None:
            if curr_node.value == value:
                return par_node, curr_node, direction
            elif value < curr_node.value:
                par_node = curr_node
                direction = self.LEFT
                curr_node = curr_node.left
            else:
                par_node = curr_node
                direction = self.RIGHT
                curr_node = curr_node.right

        return par_node, None, direction

    def __contains__(self, value: Any) -> bool:
        """
        Function to check if Binary Search Tree contains an item matching the `value`.
        """
        _, tgt_node, _ = self._get_family_tree(value)
        return True if tgt_node else False

    def _get_in_order_successor(self, start_node: Node) -> tuple[Node, Node]:
        """
        Function return in-order-successor of `start_node` along with its parent node.
        """
        par_node: Node = None
        cur_node: Node = start_node.right

        while cur_node.left is not None:
            par_node = cur_node
            cur_node = cur_node.left

        return par_node, cur_node

    def _get_in_order_predecessor(self, start_node: Node) -> tuple[Node, Node]:
        """
        Function return in-order-predecessor of `start_node` along with its parent node.
        """
        par_node: Node = None
        cur_node: Node = start_node.left

        while cur_node.right is not None:
            par_node = cur_node
            cur_node = cur_node.right

        return par_node, cur_node

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

    def _detach_successor(self, start_node: Node):
        """
        Function to find and detach successor node from its
        parent node based on pre-selected delete strategy.
        """
        if self.delete_strategy == self.IN_ORDER_SUCCESSOR:
            # Get in order successor.
            par_node, ssr_node = self._get_in_order_successor(start_node)

            # Detach successor node.
            if par_node is not None:
                par_node.left = None
            else:
                start_node.right = ssr_node.right

        elif self.delete_strategy == self.IN_ORDER_PREDECESSOR:
            # Get in order predecessor.
            par_node, ssr_node = self._get_in_order_predecessor(start_node)

            # Detach successor node.
            if par_node is not None:
                par_node.right = None
            else:
                start_node.left = ssr_node.left
        else:
            raise ValueError(f"Invalid delete strategy: {self.delete_strategy}")

        # Return successor node.
        return ssr_node

    def _update_child(self, par_node: Node, direction: int, child_node: Node | None = None):
        """
        Function to update parent node `par_node` with
        child node `child_node` based on some `direction`.
        """
        if direction == self.LEFT:
            par_node.left = child_node
        elif direction == self.RIGHT:
            par_node.right = child_node

    # Delete
    def delete(self, value: Any) -> bool:
        """
        Function to delete the node in BST matching the `value`.
        """
        """
        STEP 1: Validation.
        """
        if self.root is None:
            raise ValueError("Tree is empty!")

        """
        STEP 2: Traverse to the target node.
        """
        par_node, tgt_node, direction = self._get_family_tree(value)

        if tgt_node is None:
            return False

        """
        STEP 3: Check node type and accordingly handle parent node.
                Case #1: Leaf node.
                Case #2: Half node.
                Case #3: Full node.
        """
        ssr_node: Node = None

        # Case #1: Leaf node.
        if tgt_node.left is None and tgt_node.right is None:
            # Reset parent's connection with child node.
            self._update_child(par_node, direction, None)

        # Case #2: Half node.
        elif tgt_node.left is None:  # Right half node.
            # Connect successor node to parent of target node.
            self._update_child(par_node, direction, tgt_node.right)
        elif tgt_node.right is None:  # Left half node.
            # Connect successor node to parent of target node.
            self._update_child(par_node, direction, tgt_node.left)

        # Case #3: Full node.
        elif tgt_node.left is not None and tgt_node.right is not None:
            # Find and detach successor node from Tree.
            ssr_node = self._detach_successor(tgt_node)

            # Rewire left and right child of target node to successor node.
            ssr_node.left, ssr_node.right = tgt_node.left, tgt_node.right

            # Connect successor node to parent of target node.
            self._update_child(par_node, direction, ssr_node)

        """
        STEP 4: Update root pointer to successor node if the
                target node (Node getting deleted) is the root node.
        """
        if self.root is tgt_node:
            self.root = ssr_node

        return True
