"""
Module containing implementation for Hash Table data structure.
"""

from typing import Any
from node import Node


class HashTable:
    """
    Definition for Hash Table data structure.
    """

    # Create
    def __init__(self, size: int):
        self.size = size
        self.data_map: list[list[Node]] = [None] * self.size

    def __create_node__(self, key: str, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(key, value)
        return new_node

    def __get_index__(self, key: str) -> int:
        """
        Function to get index, where node will be positioned
        in the data map, using hash of key in the Node.
        """
        return hash(key) % self.size

    # Read
    def get_item(self, key: str) -> Node:
        """
        Function to get item from data map using its key.
        """
        index = self.__get_index__(key)

        if self.data_map[index] is None:
            return None

        for node in self.data_map[index]:
            if node.key == key:
                return node

        return None

    def get_keys(self) -> list[str]:
        """
        Function to get list of keys from Hash Table.
        """
        keys = []
        for values in self.data_map:
            if values is None:
                continue

            for node in values:
                keys.append(node.key)

        return keys

    # Update
    def add_item(self, key: str, value: Any):
        """
        Function to add item into Hash Table.
        """
        # Create new node.
        node = self.__create_node__(key, value)

        # Get address where node must be placed.
        index = self.__get_index__(node)

        if self.data_map[index] is None:
            self.data_map[index] = []

        # Push node to data map at the specified address.
        self.data_map[index].append(node)
