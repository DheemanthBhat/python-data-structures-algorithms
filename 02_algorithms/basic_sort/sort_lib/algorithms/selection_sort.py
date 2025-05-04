"""
Module containing implementation for Selection Sort algorithm.
"""

from basic_sort.sort_lib.algorithms.basic_sort import BasicSort


class SelectionSort(BasicSort):
    """
    Definition for Selection Sort.
    """

    def sort(self):
        """
        Function to sort nodes using Selection Sort algorithm.
        """
        for i in range(0, self.node_count - 1):
            target_idx = i

            # Locate target (min/max) index.
            for j in range(i + 1, self.node_count):
                if self._check_swap_criteria(idx_1=target_idx, idx_2=j) is True:
                    target_idx = j

            if i != target_idx:
                # Swap target node with current node.
                self._swap_nodes(i, target_idx)
