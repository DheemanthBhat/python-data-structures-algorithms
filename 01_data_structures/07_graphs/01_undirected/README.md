# Undirected Graph

## 1 Testing

### 1.1 Commands

Test Undirected Graph using below commands:

```sh
cd 01_data_structures/07_graphs/01_undirected
python main.py
```

### 1.2 Output

#### 1.2.1 Create

```log
Initialize empty Undirected Graph:
Graph is empty!

Add below 5 vertices to graph:
['A', 'B', 'C', 'D', 'E']
Adding vertex 'A' into graph.
Adding vertex 'B' into graph.
Adding vertex 'C' into graph.
Adding vertex 'D' into graph.
Adding vertex 'E' into graph.

Adjacency list:
Vertex(value='A') => []
Vertex(value='B') => []
Vertex(value='C') => []
Vertex(value='D') => []
Vertex(value='E') => []

Plot graph with only vertices.
```

![Image 1 only vertices](graph_plots/img_1_only_vertices.png)

#### 1.2.2 Update

```log
Add valid edges to graph:
Adding edges between Vertex(value='A') and Vertex(value='B').
Adding edges between Vertex(value='B') and Vertex(value='C').
Adding edges between Vertex(value='C') and Vertex(value='D').
Adding edges between Vertex(value='D') and Vertex(value='A').
Adding edges between Vertex(value='D') and Vertex(value='E').
Adding edges between Vertex(value='E') and Vertex(value='E').
Adding edges between Vertex(value='D') and Vertex(value='Y').
ERROR: Not found: 'Vertex(value='Y')'
Adding edges between Vertex(value='Y') and Vertex(value='D').
ERROR: Not found: 'Vertex(value='Y')'
Adding edges between Vertex(value='X') and Vertex(value='Y').
ERROR: Not found: 'Vertex(value='X')'

Adjacency list:
Vertex(value='A') => [Vertex(value='B'), Vertex(value='D')]
Vertex(value='B') => [Vertex(value='A'), Vertex(value='C')]
Vertex(value='C') => [Vertex(value='B'), Vertex(value='D')]
Vertex(value='D') => [Vertex(value='C'), Vertex(value='A'), Vertex(value='E')]
Vertex(value='E') => [Vertex(value='D'), Vertex(value='E'), Vertex(value='E')]

Plot graph after adding edges.
```

![Image 2 with edges](graph_plots/img_2_with_edges.png)

#### 1.2.3 Delete

```log
Delete 2 vertices from graph:
Delete vertex: Vertex(value='D')
Delete vertex: Vertex(value='X')
ERROR: Not found: 'Vertex(value='X')'

Adjacency list:
Vertex(value='A') => [Vertex(value='B')]
Vertex(value='B') => [Vertex(value='A'), Vertex(value='C')]
Vertex(value='C') => [Vertex(value='B')]
Vertex(value='E') => [Vertex(value='E'), Vertex(value='E')]

Plot graph after deleting vertices.
```

![Image 3 deleted vertices](graph_plots/img_3_deleted_vertices.png)

```log
Delete edges:
Deleting edges between Vertex(value='B') and Vertex(value='C').
Deleting edges between Vertex(value='A') and Vertex(value='C').
Deleting edges between Vertex(value='E') and Vertex(value='X').
ERROR: Not found: 'Vertex(value='X')'
Deleting edges between Vertex(value='X') and Vertex(value='A').
ERROR: Not found: 'Vertex(value='X')'
Deleting edges between Vertex(value='X') and Vertex(value='Y').
ERROR: Not found: 'Vertex(value='X')'

Adjacency list:
Vertex(value='A') => [Vertex(value='B')]
Vertex(value='B') => [Vertex(value='A')]
Vertex(value='C') => []
Vertex(value='E') => [Vertex(value='E'), Vertex(value='E')]

Plot graph after deleting edges.
```

![Image 4 deleted edges](graph_plots/img_4_deleted_edges.png)
