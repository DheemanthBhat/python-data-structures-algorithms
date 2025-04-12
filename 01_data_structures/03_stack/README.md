# Stack

## 1 Testing

### 1.1 Commands

Test Stack using below commands:

> **Note**:  
> Run the command from project root folder `python-data-structures-algorithms`.

```sh
python 01_data_structures/03_stack/main.py
```

### 1.2 Output

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
