"""
Module to test Graph tata structure.
"""

from graph_utils import GraphUtils
from vertex import Vertex
from graph import DirectedGraph


def main():
    """
    Function to test Directed Graph data structure.
    """
    # Create
    print("\nInitialize empty Graph:")
    d_grp = DirectedGraph()
    grp_utils = GraphUtils()

    grp_utils.display_adj_list(d_grp.adj_list)

    # Update
    vertices = ["A", "B", "C", "D", "E"]
    print(f"\nAdd below {len(vertices)} vertices to graph:")
    print(vertices)

    for vtx in vertices:
        print(f"Adding vertex '{vtx}' into graph.")
        d_grp.add_vertex(Vertex(value=vtx))

    edges = [
        [Vertex("A"), Vertex("B")],
        [Vertex("B"), Vertex("C")],
        [Vertex("C"), Vertex("D")],
        [Vertex("D"), Vertex("A")],
        [Vertex("D"), Vertex("E")],
        [Vertex("X"), Vertex("Y")],
        [Vertex("D"), Vertex("Y")],
    ]
    print(f"\nAdd {len(edges)} valid edges to graph:")

    for frm_vtx, to_vtx in edges:
        try:
            print(f"Adding edge from {frm_vtx} to {to_vtx}.")
            d_grp.add_edge(frm_vtx, to_vtx)
        except ValueError as err:
            print("ERROR:", err)

    # Read
    print("\nAdjacency list:")
    grp_utils.display_adj_list(d_grp.adj_list)

    # print("\nPlot graph before delete operations.")
    # grp_utils.plot_graph(d_grp)

    # Delete
    del_vts = [Vertex("D"), Vertex("X")]
    print(f"\nDelete {len(del_vts)} vertices from graph:")
    for del_vtx in del_vts:
        try:
            print(f"Delete vertex: {del_vtx}")
            d_grp.remove_vertex(del_vtx)
        except ValueError as err:
            print("ERROR:", err)

    del_edges = [
        [Vertex("B"), Vertex("C")],
        [Vertex("A"), Vertex("C")],
        [Vertex("E"), Vertex("X")],
    ]
    print(f"\nDelete {len(del_edges)} edges:")

    for frm_vtx, to_vtx in del_edges:
        try:
            print(f"Deleting edge from {frm_vtx} to {to_vtx}.")
            d_grp.remove_edge(frm_vtx, to_vtx)
        except ValueError as err:
            print("ERROR:", err)

    print("\nUpdated adjacency list after delete:")
    grp_utils.display_adj_list(d_grp.adj_list)

    # print("\nPlot graph diagram after delete operations.")
    # grp_utils.plot_graph(d_grp)


if __name__ == "__main__":
    main()
