"""
Module containing Node dataclass.
"""

from typing import Any
from dataclasses import dataclass, field


@dataclass(frozen=True, slots=True)
class Node:
    """
    Definition for two pointer Node.
    """

    key: str
    value: Any = field(compare=False)

    def __hash__(self) -> int:
        """
        Function to override default implementation of `__hash__()`
        in dataclass and hash the object of `Node` only by its key.
        """
        return hash(self.key)
