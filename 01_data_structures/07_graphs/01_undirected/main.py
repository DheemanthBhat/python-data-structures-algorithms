"""
Module to test Graph tata structure.
"""

from graph_utils import GraphUtils
from vertex import Vertex
from graph import UndirectedGraph


def main():
    """
    Function to test Directed Graph data structure.
    """
    # Create
    print("\nInitialize empty Graph:")
    ud_grp = UndirectedGraph()
    grp_utils = GraphUtils()

    grp_utils.display_adj_list(ud_grp.adj_list)

    # Update
    vertices = ["A", "B", "C", "D", "E"]
    print(f"\nAdd below {len(vertices)} vertices to graph:")
    print(vertices)

    for vtx in vertices:
        print(f"Adding vertex '{vtx}' into graph.")
        ud_grp.add_vertex(Vertex(value=vtx))

    edges = [
        [Vertex("A"), Vertex("B")],
        [Vertex("B"), Vertex("C")],
        [Vertex("C"), Vertex("D")],
        [Vertex("D"), Vertex("A")],
        [Vertex("D"), Vertex("B")],
        [Vertex("D"), Vertex("E")],
        [Vertex("X"), Vertex("Y")],
        [Vertex("D"), Vertex("Y")],
    ]
    print("\nAdd valid edges to graph:")

    for vtx_1, vtx_2 in edges:
        try:
            print(f"Adding edge between {vtx_1} and {vtx_2}.")
            ud_grp.add_edge(vtx_1, vtx_2)
        except ValueError as err:
            print("ERROR:", err)

    # Read
    print("\nAdjacency list:")
    grp_utils.display_adj_list(ud_grp.adj_list)

    # print("\nPlot graph before delete operations.")
    # grp_utils.plot_graph(ud_grp)

    # Delete
    del_vts = [Vertex("D"), Vertex("X")]
    print(f"\nDelete {len(del_vts)} vertices from graph:")
    for del_vtx in del_vts:
        try:
            print(f"Delete vertex: {del_vtx}")
            ud_grp.remove_vertex(del_vtx)
        except ValueError as err:
            print("ERROR:", err)

    del_edges = [
        [Vertex("B"), Vertex("C")],
        [Vertex("A"), Vertex("C")],
        [Vertex("E"), Vertex("X")],
    ]
    print("\nDelete edges:")

    for vtx_1, vtx_2 in del_edges:
        try:
            print(f"Deleting edge between {vtx_1} and {vtx_2}.")
            ud_grp.remove_edge(vtx_1, vtx_2)
        except ValueError as err:
            print("ERROR:", err)

    print("\nUpdated adjacency list after delete:")
    grp_utils.display_adj_list(ud_grp.adj_list)

    # print("\nPlot graph diagram after delete operations.")
    # grp_utils.plot_graph(ud_grp)


if __name__ == "__main__":
    main()
