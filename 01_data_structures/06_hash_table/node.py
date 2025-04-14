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
        return hash(self.key)
