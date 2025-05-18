# python-data-structures-algorithms

## 1 Introduction

### 1.1 Summary

1. This repository contains implementation for Data Structures and Algorithms in Python programming language.
2. Goal of this implementation is to use language specific features like Dataclasses, Generators, Function tools, Closures etc.
3. This implementation is based on Udemy course [Python Data Structures & Algorithms + LEETCODE Exercises][1] by [Scott Barrett][2].

> **Note**:  
> Not optimized for production environment.

### 1.2 Index

This repository covers following data structures and algorithms:

#### 1.2.1 Data Structures

1. [Singly Linked List](01_data_structures/01_singly_linked_list/README.md)
1. [Doubly Linked List](01_data_structures/02_doubly_linked_list/README.md)
1. [Stack](01_data_structures/03_stack/README.md)
1. [Queue](01_data_structures/04_queue/README.md)
1. [Binary Search Tree](01_data_structures/05_binary_search_tree/README.md)
1. [Hash Table](01_data_structures/06_hash_table/README.md)
1. [Graph](01_data_structures/07_graphs/README.md)
1. [Heap](01_data_structures/08_heaps/README.md)

#### 1.2.2 Algorithms

1. [Bubble Sort](02_algorithms/01_bubble_sort/README.md)
1. [Selection Sort](02_algorithms/02_selection_sort/README.md)
1. [Insertion Sort](02_algorithms/03_insertion_sort/README.md)
1. [Merge Sort](02_algorithms/04_merge_sort/README.md)
1. [Quick Sort](02_algorithms/05_quick_sort/README.md)

#### 1.2.3 Others

1. [Bubble sort vs. Selection sort vs. Insertion sort vs. Quick Sort](02_algorithms/basic_sort/README.md)

### 1.3 Technologies

1. Python: Programming language (version >= 3.12).
1. Libraries:
   1. [prettytable][3]: Python library used for displaying Hash Table.
   1. [networkx][4]: Python library used for displaying Graphs.

## 2 Setup

### STEP 1: Clone repository

Clone this repository and traverse to the project folder using below commands:

```sh
git clone https://github.com/DheemanthBhat/python-data-structures-algorithms.git
cd python-data-structures-algorithms
```

### STEP 2: Setup virtual environment

Create and activate virtual environment.

> **Why virtual environment?**
>
> This project is using libraries for displaying data structures.
> These libraries have dependencies that can conflict with your local python setup.
> To avoid any unintended behavior install the libraries and their dependencies in a Virtual environment.

#### Windows

```sh
python -m venv .venv
.venv\Scripts\activate
```

#### Linux

```sh
python -m venv .venv
source .venv/bin/activate
```

### STEP 3: Install python packages

```sh
pip install -r requirements.txt
```

[1]: https://www.udemy.com/share/104YM0/
[2]: https://www.udemy.com/user/scott-barrett-16/
[3]: https://pypi.org/project/prettytable/
[4]: https://pypi.org/project/networkx/
