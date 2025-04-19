"""
Module containing Graph utilities.
"""

from vertex import Vertex


class GraphUtils:
    """
    Definition for Graph utilities.
    """

    def display_adj_list(self, adj_list: dict[Vertex, list[Vertex]]):
        """
        Function to display adjacency list.
        """
        if adj_list is None or len(adj_list) == 0:
            print("Graph is empty!")

        for vtx, edges in adj_list.items():
            print(f"{vtx} => {edges}")

    def plot_graph(self, adj_list: dict[Vertex, list[Vertex]]):
        """
        Function to plot Graph as image.
        """
        # TODO: Implement graph plotting capabilities.
