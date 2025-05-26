# Tree Traversal

## 1 Introduction

There two tree traversal techniques:

1. Breadth First Search (BFS)
1. Depth First Search (DFS)

> **Note**:  
> Breadth First Search is also called as Level Order Traversal.

## 2 Breadth First Search (BFS)

### 2.1 Testing

Test Breadth First Search algorithm using below commands:

```sh
python 02_algorithms/06_tree_traversal/test_bfs.py
```

### 2.2 Output

#### Case 1: BFS on Complete Binary Tree

```log
*************** Case 1: Complete Binary Tree ***************
Create Binary Search Tree with below 15 values:
[50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25]

Display Binary Tree:
Root: Node(left=30, value=50, right=70)
Max level: 4

                     50
         30                      70
   20          40          55          80
 0    25    35    41    54    56    75    90


Tree nodes listed using Breadth First Search:
[50, 30, 70, 20, 40, 55, 80, 0, 25, 35, 41, 54, 56, 75, 90]
************************************************************
```

#### Case 2: BFS on Skewed Binary Tree

```log
*************** Case 2: Skewed Binary Tree ***************
Create Binary Search Tree with below 7 values:
[50, 60, 40, 55, 70, 45, 80]

Display Binary Tree:
Root: Node(left=40, value=50, right=60)
Max level: 4

                     50
         40                      60
               45          55          70
                                          80


Tree nodes listed using Breadth First Search:
[50, 40, 60, 45, 55, 70, 80]
************************************************************
```

## 3 Depth First Search (DFS)

### 3.1 Introduction

Depth First Search algorithm has three variants when traversing down the tree:

1. Pre-Order
2. Post-Order
3. In-Order

> **Note**:  
> Fetching values In-Order while traversing a Binary Tree results in values being sorted in ascending order.

### 3.2 Testing

Test Depth First Search algorithm using below commands:

```sh
python 02_algorithms/06_tree_traversal/test_dfs.py
```

### 3.3 Output

#### Case 1: DFS on Complete Binary Tree

```log
*************** Case 1: Complete Binary Tree ***************
Create Binary Search Tree with below 15 values:
[50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25]

Display Binary Tree:
Root: Node(left=30, value=50, right=70)
Max level: 4

                     50
         30                      70
   20          40          55          80
 0    25    35    41    54    56    75    90


Tree nodes listed in pre-order:
[50, 30, 20, 0, 25, 40, 35, 41, 70, 55, 54, 56, 80, 75, 90]

Tree nodes listed in post-order:
[0, 25, 20, 35, 41, 40, 30, 54, 56, 55, 75, 90, 80, 70, 50]

Tree nodes listed in in-order:
[0, 20, 25, 30, 35, 40, 41, 50, 54, 55, 56, 70, 75, 80, 90]
************************************************************
```

#### Case 2: DFS on Skewed Binary Tree

```log
*************** Case 2: Skewed Binary Tree ***************
Create Binary Search Tree with below 7 values:
[50, 60, 40, 55, 70, 45, 80]

Display Binary Tree:
Root: Node(left=40, value=50, right=60)
Max level: 4

                     50
         40                      60
               45          55          70
                                          80


Tree nodes listed in pre-order:
[50, 40, 45, 60, 55, 70, 80]

Tree nodes listed in post-order:
[45, 40, 55, 80, 70, 60, 50]

Tree nodes listed in in-order:
[40, 45, 50, 55, 60, 70, 80]
************************************************************
```
