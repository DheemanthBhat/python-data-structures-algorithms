"""
Module containing implementation for Quick Sort algorithm.
"""

from basic_sort.sort_lib.algorithms.basic_sort import BasicSort


class QuickSort(BasicSort):
    """
    Definition for Quick Sort algorithm.
    """

    def _sort_pivot(self, start_idx: int, end_idx: int) -> int:
        """
        Function to place pivot node at the correct position such that:
            1. LHS: All nodes to its left are smaller (greater when reversed).
            2. RHS: All nodes to its right are greater (smaller when reversed).

        Function returns index of the pivot node after it is correctly placed.
        """
        # Initialize partition index.
        partition_idx: int = start_idx

        # Rearrange nodes to meet target formation.
        for i in range(start_idx + 1, end_idx + 1):
            if self._check_swap_criteria(start_idx, i):
                partition_idx += 1
                self._swap_nodes(partition_idx, i)

        # Place pivot node at the correct position.
        self._swap_nodes(start_idx, partition_idx)

        # Return partition index.
        return partition_idx

    def _quick_sort(self, start_idx: int, end_idx: int):
        """
        Recursive function to sort list of nodes using Quick Sort algorithm.
        """
        # STEP 1: Check for base case.
        if end_idx <= start_idx:
            return

        # STEP 2: Place pivot node at its correct position.
        partition_idx = self._sort_pivot(start_idx, end_idx)

        # STEP 3: Sort nodes on LHS of partition index.
        self._quick_sort(start_idx, partition_idx - 1)

        # STEP 4: Sort nodes on RHS of partition index.
        self._quick_sort(partition_idx + 1, end_idx)

    def sort(self):
        """
        Function to sort list of nodes using Quick Sort algorithm.
        """
        self._quick_sort(start_idx=0, end_idx=self.node_count - 1)
