"""
Module containing implementation for Breadth First Search algorithm.
"""

from typing import Any
from src.data_structures.tree.node import Node
from src.data_structures.queue.queue_via_linked_list import Queue


class BreadthFirstSearch:
    """
    Definition for Breadth First Search algorithm.
    """

    def __init__(self, root_node: Node):
        self.root_node: Node = root_node

        self.queue: Queue = Queue()
        self.queue.enqueue(self.root_node)

    def tree_traversal(self):
        """
        Function to traverse Binary tree.
        """
        results: list[Any] = list()

        while self.queue.length > 0:
            # STEP 1: Pull current node from queue.
            curr_node: Node = self.queue.dequeue().value

            # STEP 2: Push node's value to results.
            results.append(curr_node.value)

            # STEP 3: Add node's children to queue.
            if curr_node.left is not None:
                self.queue.enqueue(curr_node.left)

            if curr_node.right is not None:
                self.queue.enqueue(curr_node.right)

        return results
