# python-data-structures-algorithms

## Introduction

### 1 About

1. This repository contains implementation for Data Structures and Algorithms in Python programming language.
2. Goal of this implementation in Python is to use language specific features like Generators, Function tools, etc.
3. This implementation is based on Udemy course [Python Data Structures & Algorithms + LEETCODE Exercises][1] by [Scott Barrett][2].

> Note: Not optimized for production environment.

### 2 Technologies

1. Python: Programming language.

### 3 Setup

#### STEP 1: Clone repo

Clone this repo:

```sh
git clone https://github.com/DheemanthBhat/python-data-structures-algorithms.git
```

#### STEP 2: Open project

Traverse to project folder:

```sh
cd python-data-structures-algorithms
```

## Data Structures

### 1 Linked List

#### 1.1 Singly linked list

Test singly linked list using below commands:

##### Commands

```sh
python 01_data_structures/01_singly_linked_list/main.py
```

##### Output

```log
Initialize empty Linked list:
Head: None                              Tail: None                              Length: 0
List: []

Append value 10:
Head: Node(value=10, next=None)         Tail: Node(value=10, next=None)         Length: 1
List: [10]

Prepend value 40:
Head: Node(value=40, next=10)           Tail: Node(value=10, next=None)         Length: 2
List: [40, 10]

Insert value 20 at index 1:
Head: Node(value=40, next=20)           Tail: Node(value=10, next=None)         Length: 3
List: [40, 20, 10]

Insert value 1 at index 0:
Head: Node(value=1, next=40)            Tail: Node(value=10, next=None)         Length: 4
List: [1, 40, 20, 10]

Insert value 0 at index: 4
Head: Node(value=1, next=40)            Tail: Node(value=0, next=None)          Length: 5
List: [1, 40, 20, 10, 0]

Insert value 50 at index 4:
Head: Node(value=1, next=40)            Tail: Node(value=0, next=None)          Length: 6
List: [1, 40, 20, 10, 50, 0]

Insert value 100 at index 100:
ERROR: Index: 100 out of range.

Update to value 5 at index 0:
Head: Node(value=5, next=40)            Tail: Node(value=0, next=None)          Length: 6
List: [5, 40, 20, 10, 50, 0]

Update to value 15 at index -1:
ERROR: Index: -1 out of range.

Update to value -10 at index 6:
ERROR: Index: 6 out of range.

Get 8 from 6 items by index:
Item at index 0: Node(value=5, next=40)
Item at index 1: Node(value=40, next=20)
Item at index 2: Node(value=20, next=10)
Item at index 3: Node(value=10, next=50)
Item at index 4: Node(value=50, next=0)
Item at index 5: Node(value=0, next=None)
ERROR: Index: 6 out of range.

List values between indices [1, 4):
[40, 20, 10]

Representation of Linked list (Before reverse):
Node(value=5, next=40)->
  Node(value=40, next=20)->
    Node(value=20, next=10)->
      Node(value=10, next=50)->
        Node(value=50, next=0)->
          Node(value=0, next=None)->


Reversed Linked list:
Head: Node(value=0, next=50)            Tail: Node(value=5, next=None)          Length: 6
List: [0, 50, 10, 20, 40, 5]

Representation of Linked list (After reverse):
Node(value=0, next=50)->
  Node(value=50, next=10)->
    Node(value=10, next=20)->
      Node(value=20, next=40)->
        Node(value=40, next=5)->
          Node(value=5, next=None)->


Try to pop 8 elements from the linked list containing 6 elements:

Deleted node: Node(value=0, next=50)  at index:  0
Head: Node(value=50, next=10)           Tail: Node(value=5, next=None)          Length: 5
List: [50, 10, 20, 40, 5]

Deleted node: Node(value=5, next=None)  at index:  4
Head: Node(value=50, next=10)           Tail: Node(value=40, next=None)         Length: 4
List: [50, 10, 20, 40]

Deleted node: Node(value=20, next=40)  at index:  2
Head: Node(value=50, next=10)           Tail: Node(value=40, next=None)         Length: 3
List: [50, 10, 40]

Deleted node: Node(value=10, next=40)  at index:  1
Head: Node(value=50, next=40)           Tail: Node(value=40, next=None)         Length: 2
List: [50, 40]

Deleted node: Node(value=40, next=None)  at index:  1
Head: Node(value=50, next=None)         Tail: Node(value=50, next=None)         Length: 1
List: [50]

Deleted node: Node(value=50, next=None)  at index:  0
Head: None                              Tail: None                              Length: 0
List: []
ERROR: Index: 1 out of range.

Get Item at index 0:
ERROR: Index: 0 out of range.
```

[1]: https://www.udemy.com/share/104YM0/
[2]: https://www.udemy.com/user/scott-barrett-16/
