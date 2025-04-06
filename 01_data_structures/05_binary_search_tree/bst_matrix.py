"""
Module containing dataclasses used for displaying Binary Search Tree
"""

from typing import Any
from node import Node
from bst_via_linked_list import BinarySearchTree


class Row:
    """
    Definition for single row in matrix.
    """

    def __init__(self, col_count: int, max_char_len: int):
        self.max_char_len = max_char_len
        self.data: list[Any] = [f"{' ':>{max_char_len}}" for _ in range(col_count)]

    def __setitem__(self, col_idx: int, value: Any):
        """
        Function to set value at column index `col_idx`.
        """
        self.data[col_idx] = f"{value:>{self.max_char_len}}"


class Matrix:
    """
    Definition for matrix.
    """

    def __init__(self, bst: BinarySearchTree, row_count: int, col_count: int):
        max_char_len: int = max(list(self.__get_value_len__(bst.root)))
        self.rows: list[Row] = [Row(col_count, max_char_len) for _ in range(row_count)]

    def __get_value_len__(self, node: Node, lengthiest: int = -1):
        """
        Function to get lengthiest value in Binary search Tree.
        """
        yield len(str(node.value))

        if node.left is not None:
            yield from self.__get_value_len__(node.left, lengthiest)

        if node.right is not None:
            yield from self.__get_value_len__(node.right, lengthiest)

    def __getitem__(self, row_idx: int):
        """
        Function to return row at index: `rows_idx`.
        """
        return self.rows[row_idx]

    def __iter__(self):
        """
        Function return iterable rows.
        """
        for row in self.rows:
            yield row.data
