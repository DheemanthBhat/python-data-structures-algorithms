"""
Module containing implement for Directed Graph data structure.
"""

from typing import Any
from vertex import Vertex


class DirectedGraph:
    """
    Definition for Graph data structure.
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

    # Update
    def add_vertex(self, vtx: Vertex):
        """
        Function to add new vertex into the graph.
        """
        if self.adj_list.get(vtx, None) is None:
            self.adj_list[vtx] = []

    def add_edge(self, frm_vtx: Vertex, to_vtx: Vertex):
        """
        Function to add new edge between two vertices.
        Direction of the new edge is from `frm_vtx` vertex to `to_vtx` vertex.
        """
        # Validation
        if self.adj_list.get(frm_vtx, None) is None:
            raise ValueError(f"Not found: '{frm_vtx}'")

        if self.adj_list.get(to_vtx, None) is None:
            raise ValueError(f"Not found: '{to_vtx}'")

        # Add edge from `frm_vtx` to `to_vtx`.
        if to_vtx not in self.adj_list[frm_vtx]:
            self.adj_list[frm_vtx].append(to_vtx)

    # Delete
    def remove_vertex(self, vtx: Vertex):
        """
        Function to remove vertex `vtx` from the graph.
        """
        # Validation.
        if self.adj_list.get(vtx, None) is None:
            raise ValueError(f"Not found: '{vtx}'")

        # Delete all edges pointing to vertex `vtx`.
        for _, edges in self.adj_list.items():
            if vtx in edges:
                edges.remove(vtx)

        # Delete vertex `vtx` from adjacency list.
        del self.adj_list[vtx]

    def remove_edge(self, frm_vtx: Vertex, to_vtx: Vertex):
        """
        Function to remove edge between two vertices.
        Direction of the removed edge is from `frm_vtx` vertex to `to_vtx` vertex.
        """
        # Validation
        if self.adj_list.get(frm_vtx, None) is None:
            raise ValueError(f"Not found: '{frm_vtx}'")

        if self.adj_list.get(to_vtx, None) is None:
            raise ValueError(f"Not found: '{to_vtx}'")

        # Remove edge from `frm_vtx` to `to_vtx`.
        if to_vtx in self.adj_list[frm_vtx]:
            self.adj_list[frm_vtx].remove(to_vtx)
