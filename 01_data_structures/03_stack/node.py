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
        self.value: Any = value
        self.next: dict | None = None

    def __str__(self) -> str:
        """
        Function to print Node as string
        """
        next_value = self.next.value if self.next else None
        return f"Node(value={self.value}, next={next_value})"
