"""
Module containing implementation for Undirected Graph data structure.
"""

from vertex import Vertex


class UndirectedGraph:
    """
    Definition for Undirected Graph data structure.
    """

    # Create
    def __init__(self):
        self.adj_list: dict[Vertex, list[Vertex]] = dict()

    # Update
    def add_vertex(self, vtx: Vertex):
        """
        Function to add new vertex into the graph.
        """
        if self.adj_list.get(vtx, None) is None:
            self.adj_list[vtx] = []

    def add_edge(self, vtx_1: Vertex, vtx_2: Vertex):
        """
        Function to add two new edges between vertices.
            1. From `vtx_1` vertex to `vtx_2` vertex.
            2. From `vtx_2` vertex to `vtx_1` vertex.
        """
        # Validation
        if self.adj_list.get(vtx_1, None) is None:
            raise ValueError(f"Not found: '{vtx_1}'")

        if self.adj_list.get(vtx_2, None) is None:
            raise ValueError(f"Not found: '{vtx_2}'")

        if vtx_2 not in self.adj_list[vtx_1] and vtx_1 not in self.adj_list[vtx_2]:
            # Add edge from `vtx_1` to `vtx_2`.
            self.adj_list[vtx_1].append(vtx_2)

            # Add edge from `vtx_2` to `vtx_1`.
            self.adj_list[vtx_2].append(vtx_1)

    # Delete
    def remove_vertex(self, vtx: Vertex):
        """
        Function to remove vertex `vtx` from the graph.
        """
        # Validation.
        if self.adj_list.get(vtx, None) is None:
            raise ValueError(f"Not found: '{vtx}'")

        # Delete all edges pointing to vertex `vtx`.
        for to_vtx in self.adj_list[vtx]:
            self.adj_list[to_vtx].remove(vtx)

        # Delete vertex `vtx` from adjacency list.
        del self.adj_list[vtx]

    def remove_edge(self, vtx_1: Vertex, vtx_2: Vertex):
        """
        Function to remove edges between two vertices.
            1. From `vtx_1` vertex to `vtx_2` vertex.
            2. From `vtx_2` vertex to `vtx_1` vertex.
        """
        # Validation
        if self.adj_list.get(vtx_1, None) is None:
            raise ValueError(f"Not found: '{vtx_1}'")

        if self.adj_list.get(vtx_2, None) is None:
            raise ValueError(f"Not found: '{vtx_2}'")

        if vtx_2 in self.adj_list[vtx_1] and vtx_1 in self.adj_list[vtx_2]:
            # Remove edge from `vtx_1` to `vtx_2`.
            self.adj_list[vtx_1].remove(vtx_2)

            # Remove edge from `vtx_2` to `vtx_1`.
            self.adj_list[vtx_2].remove(vtx_1)
