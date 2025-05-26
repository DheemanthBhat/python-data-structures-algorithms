"""
Module containing implementation for Queue data structure using Singly Linked List.
"""

from typing import Any
from data_structures.queue.node import Node


class Queue:
    """
    Definition for Queue data structure.
    """

    # Create
    def __init__(self):
        self.first: Node = None
        self.last: Node = None
        self.length: int = 0

    def _create_node(self, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(value)
        return new_node

    # Update
    def enqueue(self, value: Any):
        """
        Function to push item into Queue.
        """
        new_node: Node = self._create_node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length += 1

    # Delete
    def _reset(self):
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
            self._reset()
            return del_node

        self.first = self.first.next
        self.length -= 1

        return del_node
