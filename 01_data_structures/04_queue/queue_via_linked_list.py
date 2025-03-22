"""
Module containing Queue data structure implemented using singly linked list.
"""

from typing import Any
from functools import singledispatchmethod
from node import Node


class Queue:
    """
    Definition for Queue data structure.
    """

    # Create
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.length: int = 0

    def __create_node__(self, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(value)
        return new_node

    # Read
    @singledispatchmethod
    def __getitem__(self, idx: int) -> Node:
        """
        Function to fetch item at index `idx` from Queue.
        """
        if idx < 0 or idx >= self.length:
            raise IndexError(f"Index: {idx} out of range.")

        curr_idx: int = 0
        curr_node: Node = self.first

        while curr_idx != idx:
            curr_node = curr_node.next
            curr_idx += 1

        return curr_node

    @__getitem__.register
    def _(self, idx_range: slice) -> list[Any]:
        """
        Function to fetch values between index range
        [idx_range.start, idx_range.stop) from Queue.
        """
        values: list[Any] = []

        start_idx = idx_range.start
        stop_idx = idx_range.stop
        # step_val = idx_range.step  # Not supported.

        curr_node = self.first
        for idx in range(self.length):
            if idx == stop_idx:
                break

            if idx >= start_idx:
                values.append(curr_node.value)

            curr_node = curr_node.next

        return values

    def to_list(self) -> list[Any]:
        """
        Function to convert Queue to normal list.
        """
        values: list[Any] = []

        curr_node: Node = self.first
        while curr_node is not None:
            values.append(curr_node.value)
            curr_node = curr_node.next

        return values

    def __repr__(self) -> str:
        """
        Function to print nodes in Queue for string representation.
        """
        values: str = ""
        curr_node: Node = self.first
        for idx in range(self.length):
            values += f"{'  ' * idx}{curr_node}->\n"
            curr_node = curr_node.next

        return values

    # Update
    def enqueue(self, value: Any):
        """
        Function to push item into Queue.
        """
        new_node: Node = self.__create_node__(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    def __setitem__(self, idx: int, value: Any):
        """
        Dunder method to assign value using index i.e.,
        `my_queue[idx] = value`
        """
        curr_node: Node = self[idx]  # Time complexity: O(n)
        curr_node.value = value

    def reverse(self):
        """
        Function to reverse Queue.
        """
        if self.length == 0:
            return

        prev_node: Node = None
        curr_node: Node = self.first
        next_node: Node = curr_node.next

        while curr_node is not None:
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next if next_node is not None else None

        # Swap first and last.
        temp_node = self.first
        self.first = self.last
        self.last = temp_node

    # Delete
    def __reset__(self):
        """
        Function to reset Queue.
        """
        self.first = None
        self.last = None
        self.length = 0

    def dequeue(self) -> Node:
        """
        Function to pop item from Queue .
        """
        if self.length == 0:
            raise IndexError("Cannot pop from empty Queue.")

        del_node: Node = self.first

        if self.length == 1:
            self.__reset__()
            return del_node

        self.first = self.first.next
        self.length -= 1

        return del_node
