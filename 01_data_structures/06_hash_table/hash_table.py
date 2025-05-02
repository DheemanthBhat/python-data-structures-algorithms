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
    def __init__(self, size: int, allow_duplicates=True):
        self.size = size
        self.data_map: list[list[Node]] = [None] * self.size
        self.allow_duplicates = allow_duplicates

    def _create_node(self, key: str, value: Any) -> Node:
        """
        Function to create new node.
        """
        new_node = Node(key, value)
        return new_node

    def _get_index(self, item: str | Node) -> int:
        """
        Function to get index, where node will be positioned in
        the data-map, by generating hash of key-string or Node.
        """
        return hash(item) % self.size

    # Read
    def get_items(self, key: str) -> list[Node] | None:
        """
        Function to get item(s) from data-map using its key.
        """
        index = self._get_index(key)

        if self.data_map[index] is None:
            return None

        items = []
        for node in self.data_map[index]:
            if node.key == key:
                items.append(node)

                # If duplicates are not allowed then stop further lookup
                # and return the list containing first matching Node.
                if not self.allow_duplicates:
                    break

        # If list is empty return None.
        return items or None

    def get_keys(self) -> list[str]:
        """
        Function to get unique list of keys from Hash Table.
        """
        keys = set()
        for values in self.data_map:
            if values is None:
                continue

            for node in values:
                keys.add(node.key)

        return list(keys)

    # Update
    def add_item(self, key: str, value: Any):
        """
        Function to add item into Hash Table.
        """
        # Create new node using input key and value.
        new_node = self._create_node(key, value)

        # Get address where new node must be placed in data-map.
        index = self._get_index(new_node)

        # Initialize data-map with empty list
        # at the derived `index` if it is empty.
        if self.data_map[index] is None:
            self.data_map[index] = []

        # When duplicates are not allowed check if any node already exists,
        # in the list at derived index, in the data-map with incoming key.
        if not self.allow_duplicates:
            for node in self.data_map[index]:
                if node.key == key:
                    raise KeyError(f"Duplicate key: '{key}'.")

        # Push node into the list at the derived index in data-map.
        self.data_map[index].append(new_node)
