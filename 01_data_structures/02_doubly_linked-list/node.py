"""
Module containing Node dataclass.
"""

from typing import Any
from dataclasses import dataclass


# @dataclass
# class Node:
#     """
#     Definition for node.
#     """

#     value: Any
#     next: dict | None = None


class Node:
    """
    Definition for node.
    """

    def __init__(self, value: Any):
        self.prev: dict | None = None
        self.value: Any = value
        self.next: dict | None = None

    def __str__(self) -> str:
        """
        Function to print Node as string
        """
        next_value = self.next.value if self.next else None
        prev_value = self.prev.value if self.prev else None
        return f"Node(prev={prev_value}, value={self.value}, next={next_value})"
