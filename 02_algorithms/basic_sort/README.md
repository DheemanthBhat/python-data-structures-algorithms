# Basic Sort

## 1 Introduction

### 1.1 Summary

This folder contains comparison between below listed basic sorting techniques.

1. [Bubble Sort](../01_bubble_sort/README.md)
1. [Selection Sort](../02_selection_sort/README.md)
1. [Insertion Sort](../03_insertion_sort/README.md)
1. [Quick Sort](../05_quick_sort/README.md)

These sorting algorithms perform two common operations: **Comparison** and **Swapping** of nodes based on their values, hence in `basic_sort` above algorithms are brought under a single parent class called `BasicSort`.

Using the concepts of Object Oriented Programming (OOP), common operations are moved up into their parent class `BasicSort`, only retaining their unique sorting approach in their respective classes: `BubbleSort`, `SelectionSort`, `InsertionSort` and `QuickSort`.

## 2 Testing

### 2.1 Commands

Test all basic sorting techniques using below commands:

```sh
cd 02_algorithms
python -m basic_sort.main
```

### 2.2 Output

Comparison Result:

#### Case 1: Random array

Sorting a random array in ascending order.

```log
************************* Case 1: Random array *************************
Sort below input values using Insertion Sort algorithm:
[4, 2, 6, 5, 1, 3]

Comparison result:
+----------------+------------------+------------+--------------------+
| Algorithm      | Comparison count | Swap count | Sort result        |
+----------------+------------------+------------+--------------------+
| Bubble sort    | 15               | 9          | [1, 2, 3, 4, 5, 6] |
| Selection sort | 15               | 3          | [1, 2, 3, 4, 5, 6] |
| Insertion sort | 12               | 9          | [1, 2, 3, 4, 5, 6] |
| Quick sort     | 9                | 10         | [1, 2, 3, 4, 5, 6] |
+----------------+------------------+------------+--------------------+
************************************************************************
```

#### Case 2: Descending to Ascending

Sorting an array in descending order to ascending order.

```log
******************** Case 2: Descending to Ascending ********************
Sort below input values using Insertion Sort algorithm:
[6, 5, 4, 3, 2, 1]

Comparison result:
+----------------+------------------+------------+--------------------+
| Algorithm      | Comparison count | Swap count | Sort result        |
+----------------+------------------+------------+--------------------+
| Bubble sort    | 15               | 15         | [1, 2, 3, 4, 5, 6] |
| Selection sort | 15               | 3          | [1, 2, 3, 4, 5, 6] |
| Insertion sort | 15               | 15         | [1, 2, 3, 4, 5, 6] |
| Quick sort     | 15               | 14         | [1, 2, 3, 4, 5, 6] |
+----------------+------------------+------------+--------------------+
************************************************************************
```

#### Case 3: Already sorted array

Sorting and already sorted array

```log
******************** Case 3: Already sorted array ********************
Sort below input values using Insertion Sort algorithm:
[6, 5, 4, 3, 2, 1]

Comparison result:
+----------------+------------------+------------+--------------------+
| Algorithm      | Comparison count | Swap count | Sort result        |
+----------------+------------------+------------+--------------------+
| Bubble sort    | 15               | 0          | [6, 5, 4, 3, 2, 1] |
| Selection sort | 15               | 0          | [6, 5, 4, 3, 2, 1] |
| Insertion sort | 5                | 0          | [6, 5, 4, 3, 2, 1] |
| Quick sort     | 15               | 5          | [6, 5, 4, 3, 2, 1] |
+----------------+------------------+------------+--------------------+
************************************************************************
```
