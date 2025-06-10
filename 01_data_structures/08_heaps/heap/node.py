"""
Module containing Node dataclass.
"""

from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Node:
    """
    Definition for data Node.
    """

    value: Any
