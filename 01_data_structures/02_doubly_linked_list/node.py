"""
Module containing Node dataclass.
"""

from typing import Any
from dataclasses import dataclass


@dataclass
class Node:
    """
    Definition for two pointer Node.
    """

    value: Any
    prev: dict | None = None
    next: dict | None = None

    def __str__(self) -> str:
        """
        Function to print Node as string.
        """
        next_value = self.next.value if self.next else None
        prev_value = self.prev.value if self.prev else None
        return f"Node(prev={prev_value}, value={self.value}, next={next_value})"
