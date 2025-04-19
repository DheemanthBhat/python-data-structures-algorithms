"""
Module containing Vertex dataclass.
"""

from typing import Any
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Vertex:
    """
    Definition for Vertex.
    """

    value: Any
