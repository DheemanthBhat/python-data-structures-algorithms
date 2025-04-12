"""
Module containing dataclasses used for displaying Binary Search Tree.
"""

from typing import Any
from dataclasses import dataclass, InitVar, field
from node import Node
from bst_via_linked_list import BinarySearchTree


@dataclass
class Row:
    """
    Definition for single row in matrix.

    Note:
        Main reason for defining this additional dataclass `Row`,
        to represent matrix row, was to achieve below syntax.
        Assigning a value directly at required row and column indices:
            `my_matrix[row_index][col_index] = some_value`
    """

    col_count: InitVar[int]
    max_char_len: int = field(repr=False)
    data: list[Any] | None = None

    def __post_init__(self, col_count: int):
        self.data: list[Any] = [f"{' ':>{self.max_char_len}}"] * col_count

    def __setitem__(self, col_idx: int, value: Any):
        """
        Function to set value at column index `col_idx`.
        """
        self.data[col_idx] = f"{value:>{self.max_char_len}}"


@dataclass
class Matrix:
    """
    Definition for matrix.
    """

    bst: InitVar[BinarySearchTree]
    row_count: InitVar[int]
    col_count: InitVar[int]
    rows: list[Row] | None = None

    def __get_value_len__(self, node: Node, lengthiest: int = -1):
        """
        Function to get length of each value in Binary search Tree.
        """
        yield len(str(node.value))

        if node.left is not None:
            yield from self.__get_value_len__(node.left, lengthiest)

        if node.right is not None:
            yield from self.__get_value_len__(node.right, lengthiest)

    def __post_init__(self, bst: BinarySearchTree, row_count: int, col_count: int):
        # Get char length of lengthiest value in Binary search Tree.
        max_char_len: int = max(list(self.__get_value_len__(bst.root)))
        self.rows: list[Row] = [Row(col_count, max_char_len) for _ in range(row_count)]

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

    def __repr__(self) -> str:
        """
        Function to represent Matrix as string.
        """
        matrix_str = ""
        for row in self.rows:
            matrix_str += " ".join(row.data) + "\n"

        return matrix_str
