"""
Module containing Node dataclass.
"""

from typing import Any


class Node:
    """
    Definition for two pointer Node.
    """

    def __init__(self, value: Any):
        self.value: Any = value
        self.left: dict | None = None
        self.right: dict | None = None

    def __str__(self) -> str:
        """
        Function to print Node as string
        """
        left_value = self.left.value if self.left else None
        right_value = self.right.value if self.right else None

        return f"Node(left={left_value}, value={self.value}, right={right_value})"
