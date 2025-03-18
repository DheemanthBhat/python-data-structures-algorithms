"""
Module containing Linked List data structure.
"""

from typing import Any
from node import Node


class SinglyLinkedList:
    """
    Definition for singly Linked List data structure.
    """

    # Create
    def __init__(self):
        self.head: Node = None
        self.tail: Node = None
        self.length: int = 0

    def __create_node__(self, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(value)
        return new_node

    # Read
    def __getitem__(self, idx: int) -> Node:
        """
        Function to fetch item at index `idx` from linked list.
        """
        if idx < 0 or idx >= self.length:
            raise IndexError(f"Index: {idx} out of range.")

        curr_idx: int = 0
        curr_node: Node = self.head

        while curr_idx != idx:
            curr_node = curr_node.next
            curr_idx += 1

        return curr_node

    def to_list(self) -> list[Any]:
        """
        Function to convert linked list to normal list.
        """
        values: list[Any] = []

        curr_node: Node = self.head
        while curr_node is not None:
            values.append(curr_node.value)
            curr_node = curr_node.next

        return values

    def __repr__(self) -> str:
        """
        Function to print nodes in linked list for string representation.
        """
        values: str = ""
        count = 0
        curr_node: Node = self.head
        while curr_node is not None:
            values += f"{'  ' * count}{curr_node}->\n"
            count += 1
            curr_node = curr_node.next

        return values

    # Update
    def append(self, value: Any):
        """
        Function to insert item at the end of linked list.
        """
        new_node: Node = self.__create_node__(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1

    def prepend(self, value: Any):
        """
        Function to insert item at the beginning of a linked list.
        """
        new_node: Node = self.__create_node__(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.length += 1

    def insert(self, idx: int, value: Any):
        """
        Function to insert item into linked list at index `idx`.
        """
        if idx < 0 or idx > self.length:
            raise IndexError(f"Index: {idx} out of range.")

        if idx == 0:
            return self.prepend(value)

        if idx == self.length:
            return self.append(value)

        new_node = self.__create_node__(value)
        curr_idx = 0
        prev_node = None
        curr_node = self.head

        while curr_idx != idx:
            prev_node = curr_node
            curr_node = curr_node.next
            curr_idx += 1

        prev_node.next = new_node
        new_node.next = curr_node
        self.length += 1

    def __setitem__(self, idx: int, value: Any):
        """
        Dunder method to assign value using index i.e.,
        `my_linked_list[idx] = value`
        """
        curr_node: Node = self.__getitem__(idx)
        curr_node.value = value

    def reverse(self):
        """
        Function to reverse linked list.
        """
        if self.length == 0:
            return

        prev_node: Node = None
        curr_node: Node = self.head
        next_node: Node = curr_node.next

        while curr_node is not None:
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            next_node = next_node.next if next_node is not None else None

        # Swap head and tail.
        temp_node = self.head
        self.head = self.tail
        self.tail = temp_node

    # Delete
    def __reset__(self):
        """
        Function to reset linked list.
        """
        self.head = None
        self.tail = None
        self.length = 0

    def pop_first(self) -> Node:
        """
        Function to pop first item (at head) from linked list.
        """
        if self.length == 0:
            raise IndexError("Cannot pop (from head) from empty list.")

        del_node = self.head

        if self.length == 1:
            self.__reset__()
            return del_node

        self.head = self.head.next
        self.length -= 1

        return del_node

    def pop(self) -> Node:
        """
        Function to pop last item (at tail) from linked list.
        """
        if self.length == 0:
            raise IndexError("Cannot pop (from tail) from empty list.")

        del_node: Node = self.tail

        if self.length == 1:
            self.__reset__()
            return del_node

        prev_node: Node = None
        curr_node: Node = self.head
        while curr_node is not self.tail:
            prev_node = curr_node
            curr_node = curr_node.next

        self.tail = prev_node
        self.tail.next = None
        self.length -= 1

        return del_node

    def remove(self, idx: int) -> Node:
        """
        Function to remove item at index `idx` from linked list.
        """
        if idx < 0 or idx >= self.length:
            raise IndexError(f"Index: {idx} out of range.")

        if idx == 0:
            return self.pop_first()

        if idx == self.length - 1:
            return self.pop()

        curr_idx: int = 0
        prev_node: Node = None
        curr_node: Node = self.head
        next_node: Node = None

        while curr_idx != idx:
            prev_node: Node = curr_node
            curr_node: Node = curr_node.next
            next_node: Node = curr_node.next
            curr_idx += 1

        prev_node.next = next_node
        self.length -= 1

        return curr_node
