# python-data-structures-algorithms

## 1 Introduction

### 1.1 About

#### 1.1.1 Summary

1. This repository contains implementation for Data Structures and Algorithms in Python programming language.
2. Goal of this implementation is to use language specific features like Generators, Function tools, Dunder methods, Closures etc.
3. This implementation is based on Udemy course [Python Data Structures & Algorithms + LEETCODE Exercises][1] by [Scott Barrett][2].

> Note: Not optimized for production environment.

#### 1.1.2 Index

This repository covers following data structures and algorithms:

##### Data Structures

1. [Singly Linked List](01_data_structures/01_singly_linked_list)
2. [Doubly Linked List](01_data_structures/02_doubly_linked_list)
3. [Stack](01_data_structures/03_stack)
4. [Queue](01_data_structures/04_queue)
5. [Binary Search Tree](01_data_structures/05_binary_search_tree)

##### Algorithms

W.I.P

### 1.2 Technologies

1. Python: Programming language.

### 1.3 Setup

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

## 2 Data Structures

### 2.1 Singly linked list

Test singly linked list using below commands:

#### 2.1.1 Commands

```sh
python 01_data_structures/01_singly_linked_list/main.py
```

#### 2.1.2 Output

<details>

<summary>Singly linked list output</summary>

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

</details>

### 2.2 Doubly linked list

Test doubly linked list using below commands:

#### 2.2.1 Commands

```sh
python 01_data_structures/02_doubly_linked_list/main.py
```

#### 2.2.2 Output

<details>

<summary>Doubly linked list output</summary>

```log
Initialize empty Linked list:
Head: None                                     Tail: None                                     Length: 0
List: []

Append value 10:
Head: Node(prev=None, value=10, next=None)     Tail: Node(prev=None, value=10, next=None)     Length: 1
List: [10]

Prepend value 40:
Head: Node(prev=None, value=40, next=10)       Tail: Node(prev=40, value=10, next=None)       Length: 2
List: [40, 10]

Insert value 20 at index 1:
Head: Node(prev=None, value=40, next=20)       Tail: Node(prev=20, value=10, next=None)       Length: 3
List: [40, 20, 10]

Insert value 1 at index 0:
Head: Node(prev=None, value=1, next=40)        Tail: Node(prev=20, value=10, next=None)       Length: 4
List: [1, 40, 20, 10]

Insert value 0 at index: 4
Head: Node(prev=None, value=1, next=40)        Tail: Node(prev=10, value=0, next=None)        Length: 5
List: [1, 40, 20, 10, 0]

Insert value 50 at index 4:
Head: Node(prev=None, value=1, next=40)        Tail: Node(prev=50, value=0, next=None)        Length: 6
List: [1, 40, 20, 10, 50, 0]

Insert value 100 at index 100:
ERROR: Index: 100 out of range.

Update to value 5 at index 0:
Head: Node(prev=None, value=5, next=40)        Tail: Node(prev=50, value=0, next=None)        Length: 6
List: [5, 40, 20, 10, 50, 0]

Update to value 15 at index -1:
ERROR: Index: -1 out of range.

Update to value -10 at index 6:
ERROR: Index: 6 out of range.

Get 8 from 6 items by index:
Item at index 0: Node(prev=None, value=5, next=40)
Item at index 1: Node(prev=5, value=40, next=20)
Item at index 2: Node(prev=40, value=20, next=10)
Item at index 3: Node(prev=20, value=10, next=50)
Item at index 4: Node(prev=10, value=50, next=0)
Item at index 5: Node(prev=50, value=0, next=None)
ERROR: Index: 6 out of range.

List values between indices [1, 4):
[40, 20, 10]

Representation of Linked list (Before reverse):
Node(prev=None, value=5, next=40)->
  Node(prev=5, value=40, next=20)->
    Node(prev=40, value=20, next=10)->
      Node(prev=20, value=10, next=50)->
        Node(prev=10, value=50, next=0)->
          Node(prev=50, value=0, next=None)->


Reversed Linked list:
Head: Node(prev=None, value=0, next=50)        Tail: Node(prev=40, value=5, next=None)        Length: 6
List: [0, 50, 10, 20, 40, 5]

Representation of Linked list (After reverse):
Node(prev=None, value=0, next=50)->
  Node(prev=0, value=50, next=10)->
    Node(prev=50, value=10, next=20)->
      Node(prev=10, value=20, next=40)->
        Node(prev=20, value=40, next=5)->
          Node(prev=40, value=5, next=None)->


Try to pop 8 elements from the linked list containing 6 elements:

Deleted node: Node(prev=None, value=0, next=50)  at index:  0
Head: Node(prev=None, value=50, next=10)       Tail: Node(prev=40, value=5, next=None)        Length: 5
List: [50, 10, 20, 40, 5]

Deleted node: Node(prev=40, value=5, next=None)  at index:  4
Head: Node(prev=None, value=50, next=10)       Tail: Node(prev=20, value=40, next=None)       Length: 4
List: [50, 10, 20, 40]

Deleted node: Node(prev=10, value=20, next=40)  at index:  2
Head: Node(prev=None, value=50, next=10)       Tail: Node(prev=10, value=40, next=None)       Length: 3
List: [50, 10, 40]

Deleted node: Node(prev=50, value=10, next=40)  at index:  1
Head: Node(prev=None, value=50, next=40)       Tail: Node(prev=50, value=40, next=None)       Length: 2
List: [50, 40]

Deleted node: Node(prev=50, value=40, next=None)  at index:  1
Head: Node(prev=None, value=50, next=None)     Tail: Node(prev=None, value=50, next=None)     Length: 1
List: [50]

Deleted node: Node(prev=None, value=50, next=None)  at index:  0
Head: None                                     Tail: None                                     Length: 0
List: []
ERROR: Index: 1 out of range.

Get Item at index 0:
ERROR: Index: 0 out of range.
```

</details>

### 2.3 Stack

#### 2.3.1 Commands

Test Stack using below commands:

```sh
python 01_data_structures/03_stack/main.py
```

#### 2.3.2 Output

<details>

<summary>Stack output</summary>

```log
Initialize empty Stack:
Top: None                              Length: 0
Stack: []

Push values [1, 40, 20, 10, 50, 0] into Stack:
Top: Node(value=0, next=50)            Length: 6
Stack: [0, 50, 10, 20, 40, 1]

Update to value 5 at index 0:
Top: Node(value=5, next=50)            Length: 6
Stack: [5, 50, 10, 20, 40, 1]

Update to value 15 at index -1:
ERROR: Index: -1 out of range.

Update to value -10 at index 6:
ERROR: Index: 6 out of range.

Get 8 from 6 items by index:
Item at index 0: Node(value=5, next=50)
Item at index 1: Node(value=50, next=10)
Item at index 2: Node(value=10, next=20)
Item at index 3: Node(value=20, next=40)
Item at index 4: Node(value=40, next=1)
Item at index 5: Node(value=1, next=None)
ERROR: Index: 6 out of range.

List values between indices [1, 4):
[50, 10, 20]

Representation of Stack (Before reverse):
Node(value=5, next=50)->
  Node(value=50, next=10)->
    Node(value=10, next=20)->
      Node(value=20, next=40)->
        Node(value=40, next=1)->
          Node(value=1, next=None)->


Reversed Stack:
Top: Node(value=1, next=40)            Length: 6
Stack: [1, 40, 20, 10, 50, 5]

Representation of Stack (After reverse):
Node(value=1, next=40)->
  Node(value=40, next=20)->
    Node(value=20, next=10)->
      Node(value=10, next=50)->
        Node(value=50, next=5)->
          Node(value=5, next=None)->


Try to pop 8 elements from Stack containing 6 elements:

Deleted node: Node(value=1, next=40)
Top: Node(value=40, next=20)           Length: 5
Stack: [40, 20, 10, 50, 5]

Deleted node: Node(value=40, next=20)
Top: Node(value=20, next=10)           Length: 4
Stack: [20, 10, 50, 5]

Deleted node: Node(value=20, next=10)
Top: Node(value=10, next=50)           Length: 3
Stack: [10, 50, 5]

Deleted node: Node(value=10, next=50)
Top: Node(value=50, next=5)            Length: 2
Stack: [50, 5]

Deleted node: Node(value=50, next=5)
Top: Node(value=5, next=None)          Length: 1
Stack: [5]

Deleted node: Node(value=5, next=None)
Top: None                              Length: 0
Stack: []
ERROR: Cannot pop from empty Stack.

Get Item at index 0:
ERROR: Index: 0 out of range.
```

</details>

### 2.4 Queue

#### 2.4.1 Commands

Test Queue using below commands:

```sh
python 01_data_structures/04_queue/main.py
```

#### 2.4.2 Output

<details>

<summary>Queue output</summary>

```log
Initialize empty Queue:
Top: None                              Tail: None                              Length: 0
Queue: []

Enqueue values [1, 40, 20, 10, 50, 0] into Queue:
Top: Node(value=1, next=40)            Tail: Node(value=0, next=None)          Length: 6
Queue: [1, 40, 20, 10, 50, 0]

Update to value 5 at index 0:
Top: Node(value=5, next=40)            Tail: Node(value=0, next=None)          Length: 6
Queue: [5, 40, 20, 10, 50, 0]

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

Representation of Queue (Before reverse):
Node(value=5, next=40)->
  Node(value=40, next=20)->
    Node(value=20, next=10)->
      Node(value=10, next=50)->
        Node(value=50, next=0)->
          Node(value=0, next=None)->


Reversed Queue:
Top: Node(value=0, next=50)            Tail: Node(value=5, next=None)          Length: 6
Queue: [0, 50, 10, 20, 40, 5]

Representation of Queue (After reverse):
Node(value=0, next=50)->
  Node(value=50, next=10)->
    Node(value=10, next=20)->
      Node(value=20, next=40)->
        Node(value=40, next=5)->
          Node(value=5, next=None)->


Try to dequeue 8 elements from Queue containing 6 elements:

Deleted node: Node(value=0, next=50)
Top: Node(value=50, next=10)           Tail: Node(value=5, next=None)          Length: 5
Queue: [50, 10, 20, 40, 5]

Deleted node: Node(value=50, next=10)
Top: Node(value=10, next=20)           Tail: Node(value=5, next=None)          Length: 4
Queue: [10, 20, 40, 5]

Deleted node: Node(value=10, next=20)
Top: Node(value=20, next=40)           Tail: Node(value=5, next=None)          Length: 3
Queue: [20, 40, 5]

Deleted node: Node(value=20, next=40)
Top: Node(value=40, next=5)            Tail: Node(value=5, next=None)          Length: 2
Queue: [40, 5]

Deleted node: Node(value=40, next=5)
Top: Node(value=5, next=None)          Tail: Node(value=5, next=None)          Length: 1
Queue: [5]

Deleted node: Node(value=5, next=None)
Top: None                              Tail: None                              Length: 0
Queue: []
ERROR: Cannot pop from empty Queue.

Get Item at index 0:
ERROR: Index: 0 out of range.
```

</details>

### 2.5 Binary Search Tree (BST)

#### 2.5.1 Commands

Test BST using below commands:

```sh
python 01_data_structures/05_binary_search_tree/main.py
```

#### 2.5.2 Output

<details>

<summary>BST output</summary>

```log
Initialize empty Binary Search Tree:

Insert below values into Binary Search Tree:
[50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25]

Display Binary Search Tree:
Root: Node(left=30, value=50, right=70)
Max level: 4

                     50
         30                      70
   20          40          55          80
 0    25    35    41    54    56    75    90

Check if values: [56, 0, -20] exists in Binary Search Tree:
Value: 56 present
Value: 0 present
Value: -20 absent
```

</details>

[1]: https://www.udemy.com/share/104YM0/
[2]: https://www.udemy.com/user/scott-barrett-16/
