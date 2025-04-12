# Queue

## 1 Testing

### 1.1 Commands

Test Queue using below commands:

> **Note**:  
> Run the command from project root folder `python-data-structures-algorithms`.

```sh
python 01_data_structures/04_queue/main.py
```

### 1.2 Output

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
