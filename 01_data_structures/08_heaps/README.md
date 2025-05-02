# Heaps

## 1 Types of Heaps

Based on the nature of value in root node, there are two types of Heaps.

1. Max Heap
   1. Root node will have the largest value.
   1. Value of every children under a node will be smaller than its parent.
1. Min Heap
   1. Root node will have the smallest value.
   1. Value of every children under a node will be greater than its parent.

## 2 Testing

### 2.1 Commands

Test Heap using below commands:

> **Note**:  
> Run the command from project root folder `python-data-structures-algorithms`.

```sh
python 01_data_structures/08_heaps/main.py
```

### 2.2 Output

#### Case 1: Max Heap

```log
******************** Case 1: Max Heap ********************
Initialize empty Heap:

Insert below 7 values into Heap:
[99, 72, 61, 58, 100, 75, 18]

List Heap values:
[100, 99, 75, 58, 72, 61, 18]

Display Max Heap:
Root: Node(value=100)
Max level: 3

            100
     99              75
 58      72      61      18


Deleting root: Node(value=100)
Heap after delete with new root:
Root: Node(value=99)
Max level: 3

         99
   72          75
58    18    61


Deleting root: Node(value=99)
Heap after delete with new root:
Root: Node(value=75)
Max level: 3

         75
   72          61
58    18

************************************************************
```

#### Case 2: Min Heap

```log
******************** Case 2: Min Heap ********************
Initialize empty Heap:

Insert below 10 values into Heap:
[61, 58, 72, 99, 55, 27, 18, 0, 99, 33]

List Heap values:
[0, 18, 27, 58, 33, 72, 55, 99, 99, 61]

Display Max Heap:
Root: Node(value=0)
Max level: 4

                      0
         18                      27
   58          33          72          55
99    99    61


Deleting root: Node(value=0)
Heap after delete with new root:
Root: Node(value=18)
Max level: 4

                     18
         33                      27
   58          61          72          55
99    99


Deleting root: Node(value=18)
Heap after delete with new root:
Root: Node(value=27)
Max level: 4

                     27
         33                      55
   58          61          72          99
99


Deleting root: Node(value=27)
Heap after delete with new root:
Root: Node(value=33)
Max level: 3

         33
   58          55
99    61    72    99

************************************************************
```
