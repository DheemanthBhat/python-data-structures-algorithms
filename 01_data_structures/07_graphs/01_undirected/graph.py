"""
Module containing implement for Undirected Graph data structure.
"""

from typing import Any
from vertex import Vertex


class UndirectedGraph:
    """
    Definition for Undirected Graph data structure.
    """

    # Create
    def __init__(self):
        self.adj_list: dict[Vertex, list[Vertex]] = dict()

    def __create_vertex__(self, ip_value: Any):
        """
        Function to create new vertex.
        """
        vtx = Vertex(value=ip_value)
        return vtx

    # Read
    def __getitem__(self, vtx: Vertex) -> list[Vertex]:
        """
        Function to get all vertices pointing to and from `vtx` vertex.
        """
        # Validation
        if self.adj_list.get(vtx, None) is None:
            raise ValueError(f"Not found: '{vtx}'")

        return self.adj_list[vtx]

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
        if vtx_2 not in self[vtx_1] and vtx_1 not in self[vtx_2]:
            # Add edge from `vtx_1` to `vtx_2`.
            self.adj_list[vtx_1].append(vtx_2)

            # Add edge from `vtx_2` to `vtx_1`.
            self.adj_list[vtx_2].append(vtx_1)

    # Delete
    def remove_vertex(self, vtx: Vertex):
        """
        Function to remove vertex `vtx` from the graph.
        """
        # Delete all edges pointing to vertex `vtx`.
        for to_vtx in self[vtx]:
            self[to_vtx].remove(vtx)

        # Delete vertex `vtx` from adjacency list.
        del self.adj_list[vtx]

    def remove_edge(self, vtx_1: Vertex, vtx_2: Vertex):
        """
        Function to remove edge between two vertices.
        Direction of the removed edge is from `vtx_1` vertex to `vtx_2` vertex.
        """
        if vtx_2 not in self[vtx_1] and vtx_1 not in self[vtx_2]:
            return

        # Remove edge from `vtx_1` to `vtx_2`.
        self.adj_list[vtx_1].remove(vtx_2)

        # Remove edge from `vtx_2` to `vtx_1`.
        self.adj_list[vtx_2].remove(vtx_1)
