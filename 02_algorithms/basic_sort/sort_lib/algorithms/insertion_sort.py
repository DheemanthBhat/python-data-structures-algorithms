"""
Module containing implementation for Insertion Sort algorithm.
"""

from basic_sort.sort_lib.algorithms.basic_sort import BasicSort


class InsertionSort(BasicSort):
    """
    Definition for Insertion Sort.
    """

    def sort(self) -> tuple[int, int]:
        """
        Function to sort nodes using Insertion Sort algorithm.
        """
        for i in range(1, self.node_count):
            for j in range(i, 0, -1):
                if self._check_swap_criteria(idx_1=j - 1, idx_2=j) is False:
                    break

                self._swap_nodes(idx_1=j - 1, idx_2=j)

        return self.comp_count, self.swap_count
