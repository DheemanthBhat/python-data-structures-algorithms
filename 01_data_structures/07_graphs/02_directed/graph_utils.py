"""
Module containing Graph utilities.
"""

import os
import networkx as nx
import matplotlib.pyplot as plt
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
            return

        print("\nAdjacency list:")
        for vtx, edges in adj_list.items():
            print(f"{vtx} => {edges}")

    def plot_graph(
        self,
        adj_list: dict[Vertex, list[Vertex]],
        file_name: str = "graph.png",
    ):
        """
        Function to plot Graph as image.
        """
        output_file_path = os.path.join("graph_plots", file_name)

        # Undirected graph.
        nx_grp = nx.DiGraph()

        for vtx_1, edges in adj_list.items():
            if len(edges) == 0:
                nx_grp.add_node(vtx_1.value)
                continue

            for vtx_2 in edges:
                nx_grp.add_edge(vtx_1.value, vtx_2.value)

        nx.draw(nx_grp, with_labels=True, node_size=1000, alpha=0.9)
        plt.savefig(output_file_path, dpi=100, bbox_inches='tight')
        plt.clf()
