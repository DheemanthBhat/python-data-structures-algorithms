"""
Module to test Graph tata structure.
"""

from graph_utils import GraphUtils
from vertex import Vertex
from graph import DirectedGraph


def test_update(grp: DirectedGraph):
    """
    Function to test update operations on Directed Graph.
    """
    grp_utils = GraphUtils()

    """
    STEP 1: Add vertices.
    """
    vertices = ["A", "B", "C", "D", "E"]
    print(f"\nAdd below {len(vertices)} vertices to graph:")
    print(vertices)

    for vtx in vertices:
        print(f"Adding vertex '{vtx}' into graph.")
        grp.add_vertex(Vertex(value=vtx))

    grp_utils.display_adj_list(grp.adj_list)

    print("\nPlot graph with only vertices.")
    grp_utils.plot_graph(grp.adj_list, file_name="img_1_only_vertices.png")

    """
    STEP 2: Add edges between vertices.
    """
    edges = [
        [Vertex("A"), Vertex("B")],
        [Vertex("B"), Vertex("C")],
        [Vertex("C"), Vertex("D")],
        [Vertex("D"), Vertex("A")],
        [Vertex("D"), Vertex("E")],
        [Vertex("D"), Vertex("Y")],  # RHS vertex does not exist.
        [Vertex("Y"), Vertex("D")],  # LHS vertex does not exist.
        [Vertex("X"), Vertex("Y")],  # Both vertex does not exist.
    ]
    print(f"\nAdd {len(edges)} valid edges to graph:")

    for frm_vtx, to_vtx in edges:
        try:
            print(f"Adding edge from {frm_vtx} to {to_vtx}.")
            grp.add_edge(frm_vtx, to_vtx)
        except ValueError as err:
            print("ERROR:", err)

    grp_utils.display_adj_list(grp.adj_list)

    print("\nPlot graph after adding edges.")
    grp_utils.plot_graph(grp.adj_list, file_name="img_2_with_edges.png")


def test_delete(grp: DirectedGraph):
    """
    Function to test delete operations on Directed Graph.
    """
    grp_utils = GraphUtils()

    """
    STEP 1: Delete some vertices.
    """
    del_vts = [Vertex("D"), Vertex("X")]
    print(f"\nDelete {len(del_vts)} vertices from graph:")
    for del_vtx in del_vts:
        try:
            print(f"Delete vertex: {del_vtx}")
            grp.remove_vertex(del_vtx)
        except ValueError as err:
            print("ERROR:", err)

    grp_utils.display_adj_list(grp.adj_list)

    print("\nPlot graph after deleting vertices.")
    grp_utils.plot_graph(grp.adj_list, file_name="img_3_deleted_vertices.png")

    """
    STEP 2: Delete edges.
    """
    del_edges = [
        [Vertex("B"), Vertex("C")],  # Valid edge.
        [Vertex("A"), Vertex("C")],  # Missing edge.
        [Vertex("E"), Vertex("X")],  # RHS vertex does not exist.
        [Vertex("X"), Vertex("A")],  # LHS vertex does not exist.
        [Vertex("X"), Vertex("Y")],  # Both vertex does not exist.
    ]
    print(f"\nDelete {len(del_edges)} edges:")

    for frm_vtx, to_vtx in del_edges:
        try:
            print(f"Deleting edge from {frm_vtx} to {to_vtx}.")
            grp.remove_edge(frm_vtx, to_vtx)
        except ValueError as err:
            print("ERROR:", err)

    grp_utils.display_adj_list(grp.adj_list)

    print("\nPlot graph after deleting edges.")
    grp_utils.plot_graph(grp.adj_list, file_name="img_4_deleted_edges.png")


def main():
    """
    Function to test Directed Graph data structure.
    """
    # Create
    print("\nInitialize empty Directed Graph:")
    grp = DirectedGraph()
    grp_utils = GraphUtils()

    grp_utils.display_adj_list(grp.adj_list)

    # Update
    test_update(grp)

    # Delete
    test_delete(grp)


if __name__ == "__main__":
    main()
