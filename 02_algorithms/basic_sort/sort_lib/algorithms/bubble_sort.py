"""
Module containing implementation for Bubble Sort algorithm.
"""

from basic_sort.sort_lib.algorithms.basic_sort import BasicSort


class BubbleSort(BasicSort):
    """
    Definition for Bubble Sort algorithm.
    """

    def sort(self):
        """
        Function to sort list of nodes using Bubble Sort algorithm.
        """
        for i in range(1, self.node_count):
            for j in range(0, self.node_count - i):
                if self._check_swap_criteria(idx_1=j, idx_2=j + 1) is True:
                    self._swap_nodes(j, j + 1)
