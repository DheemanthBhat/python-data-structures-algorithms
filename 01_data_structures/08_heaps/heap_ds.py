"""
Module containing implementation for Heap data structure.
"""

from typing import Any
from node import Node


class Heap:
    """
    Definition for Heap.
    """

    MAX_HEAP: int = 1
    MIN_HEAP: int = 2

    # Create
    def __init__(self, heap_type: int = MAX_HEAP):
        self.nodes: list[Node] = list()
        self.heap_type = heap_type

    def __create_node__(self, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(value)
        return new_node

    # Read
    def __meets_swap_criteria__(self, par_node: Node, curr_node: Node):
        """
        Function to check if Swap criteria is met.
            1. Max Heap: Value in parent node must be greater than current node.
            2. Min Heap: Value in parent node must be less than current node.
        """
        if self.heap_type == self.MAX_HEAP:
            return True if par_node.value < curr_node.value else False

        if self.heap_type == self.MIN_HEAP:
            return True if par_node.value > curr_node.value else False

        raise ValueError("Failed to meet Heap criteria.")

    def __get_parent_idx__(self, curr_idx: int) -> int | None:
        """
        Function to get parent's index using current node's index.
        """
        if curr_idx <= 0:
            raise ValueError("Input index must be greater than zero.")

        return int((curr_idx - 1) // 2)

    def __get_left_child_idx__(self, curr_idx: int) -> int:
        """
        Function to get left child's index using current node's index.
        """
        if curr_idx < 0:
            raise ValueError("Input index cannot be less than zero.")

        lc_idx = int((curr_idx * 2) + 1)
        return -1 if lc_idx > (len(self.nodes) - 1) else lc_idx

    def __get_right_child_idx__(self, curr_idx: int) -> int:
        """
        Function to get right child's index using current node's index.
        """
        if curr_idx < 0:
            raise ValueError("Input index cannot be less than zero.")

        rc_idx = int((curr_idx * 2) + 2)
        return -1 if rc_idx > (len(self.nodes) - 1) else rc_idx

    def to_list(self):
        """
        Function to print heap as list.
        """
        return [node.value for node in self.nodes]

    # Update
    def __swap_nodes__(self, idx_1: int, idx_2: int):
        """
        Function to swap nodes between indices `idx_1` and `idx_2`.
        """
        self.nodes[idx_1], self.nodes[idx_2] = self.nodes[idx_2], self.nodes[idx_1]

    def insert(self, value: Any):
        """
        Function to insert item into Heap.
        """
        """
        STEP 1: Add item into Heap.
        """
        new_node: Node = self.__create_node__(value)
        self.nodes.append(new_node)

        if len(self.nodes) < 2:
            return

        """
        STEP 2: Swap with parent if value is larger than parent.
        """
        curr_idx: int = len(self.nodes) - 1
        par_idx = self.__get_parent_idx__(curr_idx)
        par_node: Node = self.nodes[par_idx]

        while curr_idx != 0 and self.__meets_swap_criteria__(par_node, new_node):
            # Swap current node with parent node.
            self.__swap_nodes__(curr_idx, par_idx)

            # Update pointers.
            curr_idx = par_idx
            par_idx = self.__get_parent_idx__(par_idx) if par_idx > 0 else 0
            par_node = self.nodes[par_idx]

    # Delete
    def __meets_sink_criteria__(
        self,
        curr_idx: int,
        lc_idx: int,
        rc_idx: int,
    ) -> tuple[bool, bool, bool]:
        """
        Function to check sink criteria.
        """
        leaf_node, swap_with_left, swap_with_right = False, False, False

        """
        If both left and right indices are missing  i.e.,
        index is -1 then current node is a leaf node.
        """
        if lc_idx == -1 and rc_idx == -1:
            return True, False, False

        curr_node: Node | None = self.nodes[curr_idx] if curr_idx >= 0 else None
        left_child: Node | None = self.nodes[lc_idx] if lc_idx >= 0 else None
        right_child: Node | None = self.nodes[rc_idx] if rc_idx >= 0 else None

        if self.heap_type == self.MAX_HEAP:
            if left_child is not None and right_child is not None:
                """
                When both left child and right child are present,
                comparison for swap operation is done between children.
                """
                if left_child.value > right_child.value:
                    swap_with_left = True
                else:
                    swap_with_right = True
            elif (
                left_child is not None
                and right_child is None  # Redundant check but added for readability.
                and left_child.value > curr_node.value
            ):
                """
                When only left child is present (and right child is absent),
                left child is compared with current node for swap operation.
                """
                swap_with_left = True
            elif (
                left_child is None
                and right_child is not None  # Redundant check but added for readability.
            ):
                """
                This scenario can never happen in a Complete Binary Tree.

                Its always the right most child that is swapped with
                the root node before initiating sink down operation.
                """
                raise ValueError("Invalid heap!")

        elif self.heap_type == self.MIN_HEAP:
            if left_child is not None and right_child is not None:
                """
                When both left child and right child are present,
                comparison for swap operation is done between children.
                """
                if left_child.value < right_child.value:
                    swap_with_left = True
                else:
                    swap_with_right = True
            elif (
                left_child is not None
                and right_child is None  # Redundant check but added for readability.
                and left_child.value < curr_node.value
            ):
                """
                When only left child is present (and right child is absent),
                left child is compared with current node for swap operation.
                """
                swap_with_left = True
            elif (
                left_child is None
                and right_child is not None  # Redundant check but added for readability.
            ):
                """
                This scenario can never happen in a Complete Binary Tree.

                Its always the right most child that is swapped with
                the root node before initiating sink down operation.
                """
                raise ValueError("Invalid heap!")

        return leaf_node, swap_with_left, swap_with_right

    def __sink_down__(self, start_idx: int = 0):
        """
        Function to sink down current node until
        the Binary Tree is a valid Min/Max Heap.
        """
        # Initialize pointers.
        curr_idx = start_idx
        lc_idx = self.__get_left_child_idx__(curr_idx)
        rc_idx = self.__get_right_child_idx__(curr_idx)

        """
        Run sink down as long as any of the below criteria is met.
            1. Leaf node is reached.
            2. Left child is swappable with current node.
            2. Right child is swappable with current node.
        """
        while any(criteria := self.__meets_sink_criteria__(curr_idx, lc_idx, rc_idx)):
            leaf_node, swap_with_left, swap_with_right = criteria

            if leaf_node:
                break

            elif swap_with_left:
                self.__swap_nodes__(curr_idx, lc_idx)
                curr_idx = lc_idx  # New Parent

            elif swap_with_right:
                self.__swap_nodes__(curr_idx, rc_idx)
                curr_idx = rc_idx  # New Parent

            # Update pointers.
            lc_idx = self.__get_left_child_idx__(curr_idx)
            rc_idx = self.__get_right_child_idx__(curr_idx)

    def remove_root(self):
        """
        Function to remove root node from Heap.
        """
        """
        STEP 1: Handle empty heap.
        """
        if len(self.nodes) == 0:
            raise ValueError("Heap is empty!")

        """
        STEP 2: Complete the Binary Tree by:
                1. Swapping root and last node.
                2. Delete the current last node (which was previously root).
        """
        root_idx = 0
        last_idx = len(self.nodes) - 1
        self.__swap_nodes__(root_idx, last_idx)
        self.nodes.pop()

        """
        STEP 3: Sink down Heap starting from root node.
        """
        self.__sink_down__(start_idx=root_idx)
