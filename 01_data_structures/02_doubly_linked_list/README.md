# Doubly linked list

## 1 Testing

### 1.1 Commands

Test doubly linked list using below commands:

> **Note**:  
> Run the command from project root folder `python-data-structures-algorithms`.

```sh
python 01_data_structures/02_doubly_linked_list/main.py
```

### 1.2 Output

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
