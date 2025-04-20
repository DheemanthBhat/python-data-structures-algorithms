# Undirected Graph

## 1 Testing

### 1.1 Commands

Test Undirected Graph using below commands:

> **Note**:  
> Run the command from project root folder `python-data-structures-algorithms`.

```sh
python 01_data_structures/07_graphs/01_undirected/main.py
```

### 1.2 Output

```log
Initialize empty Graph:
Graph is empty!

Add below 5 vertices to graph:
['A', 'B', 'C', 'D', 'E']
Adding vertex 'A' into graph.
Adding vertex 'B' into graph.
Adding vertex 'C' into graph.
Adding vertex 'D' into graph.
Adding vertex 'E' into graph.

Add valid edges to graph:
Adding edge between Vertex(value='A') and Vertex(value='B').
Adding edge between Vertex(value='B') and Vertex(value='C').
Adding edge between Vertex(value='C') and Vertex(value='D').
Adding edge between Vertex(value='D') and Vertex(value='A').
Adding edge between Vertex(value='D') and Vertex(value='E').
Adding edge between Vertex(value='D') and Vertex(value='Y').
ERROR: Not found: 'Vertex(value='Y')'
Adding edge between Vertex(value='Y') and Vertex(value='D').
ERROR: Not found: 'Vertex(value='Y')'
Adding edge between Vertex(value='X') and Vertex(value='Y').
ERROR: Not found: 'Vertex(value='X')'

Adjacency list:
Vertex(value='A') => [Vertex(value='B'), Vertex(value='D')]
Vertex(value='B') => [Vertex(value='A'), Vertex(value='C')]
Vertex(value='C') => [Vertex(value='B'), Vertex(value='D')]
Vertex(value='D') => [Vertex(value='C'), Vertex(value='A'), Vertex(value='E')]
Vertex(value='E') => [Vertex(value='D')]

Delete 2 vertices from graph:
Delete vertex: Vertex(value='D')
Delete vertex: Vertex(value='X')
ERROR: Not found: 'Vertex(value='X')'

Delete edges:
Deleting edge between Vertex(value='B') and Vertex(value='C').
Deleting edge between Vertex(value='A') and Vertex(value='C').
Deleting edge between Vertex(value='E') and Vertex(value='X').
ERROR: Not found: 'Vertex(value='X')'
Deleting edge between Vertex(value='X') and Vertex(value='A').
ERROR: Not found: 'Vertex(value='X')'
Deleting edge between Vertex(value='X') and Vertex(value='Y').
ERROR: Not found: 'Vertex(value='X')'

Updated adjacency list after delete:
Vertex(value='A') => [Vertex(value='B')]
Vertex(value='B') => [Vertex(value='A')]
Vertex(value='C') => []
Vertex(value='E') => []
```
