# Hash Table

## Testing

### 1.1 Commands

Test Hash Table using below commands:

> **Note**:  
> Below command is run from project root folder `python-data-structures-algorithms`.

```sh
python 01_data_structures/06_hash_table/main.py
```

### 1.2 Output

#### Case 1: When duplicates are allowed in Hash Table

```log
************************* Case 1: Allow duplicates *************************

Initialize Hash Table of size: 5
+-----+--------+
| Key | Values |
+-----+--------+
| 0   | None   |
| 1   | None   |
| 2   | None   |
| 3   | None   |
| 4   | None   |
+-----+--------+

Add 5 items into Hash Table.
Adding item: {item_1: 40}
Adding item: {item_2: 20}
Adding item: {item_3: 1}
Adding item: {item_4: 0}
Adding item: {item_5: 40}

Trying to add duplicate item: {item_3: 10}

Display Hast Table:
+-----+-----------------------------------+
| Key | Values                            |
+-----+-----------------------------------+
| 0   | [                                 |
|     |     Node(key='item_2', value=20), |
|     |     Node(key='item_5', value=40)  |
|     | ]                                 |
| 1   | [                                 |
|     |     Node(key='item_4', value=0)   |
|     | ]                                 |
| 2   | None                              |
| 3   | [                                 |
|     |     Node(key='item_1', value=40)  |
|     | ]                                 |
| 4   | [                                 |
|     |     Node(key='item_3', value=1),  |
|     |     Node(key='item_3', value=10)  |
|     | ]                                 |
+-----+-----------------------------------+

List keys in Hash Table:
['item_5', 'item_2', 'item_3', 'item_1', 'item_4']

Fetch values from Hash Table using below keys:
['item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_6']
Key: item_1, Value: [Node(key='item_1', value=40)]
Key: item_2, Value: [Node(key='item_2', value=20)]
Key: item_3, Value: [Node(key='item_3', value=1), Node(key='item_3', value=10)]
Key: item_4, Value: [Node(key='item_4', value=0)]
Key: item_5, Value: [Node(key='item_5', value=40)]
Key: item_6, Value: None
******************************************************************************** 
```

#### Case 2: When duplicates are NOT allowed in Hash Table

```log
************************* Case 2: Reject duplicates *************************

Initialize Hash Table of size: 5
+-----+--------+
| Key | Values |
+-----+--------+
| 0   | None   |
| 1   | None   |
| 2   | None   |
| 3   | None   |
| 4   | None   |
+-----+--------+

Add 5 items into Hash Table.
Adding item: {item_1: 40}
Adding item: {item_2: 20}
Adding item: {item_3: 1}
Adding item: {item_4: 0}
Adding item: {item_5: 40}

Trying to add duplicate item: {item_3: 10}
ERROR: "Duplicate key: 'item_3'."

Display Hast Table:
+-----+-----------------------------------+
| Key | Values                            |
+-----+-----------------------------------+
| 0   | [                                 |
|     |     Node(key='item_2', value=20), |
|     |     Node(key='item_5', value=40)  |
|     | ]                                 |
| 1   | [                                 |
|     |     Node(key='item_4', value=0)   |
|     | ]                                 |
| 2   | None                              |
| 3   | [                                 |
|     |     Node(key='item_1', value=40)  |
|     | ]                                 |
| 4   | [                                 |
|     |     Node(key='item_3', value=1)   |
|     | ]                                 |
+-----+-----------------------------------+

List keys in Hash Table:
['item_5', 'item_2', 'item_3', 'item_1', 'item_4']

Fetch values from Hash Table using below keys:
['item_1', 'item_2', 'item_3', 'item_4', 'item_5', 'item_6']
Key: item_1, Value: [Node(key='item_1', value=40)]
Key: item_2, Value: [Node(key='item_2', value=20)]
Key: item_3, Value: [Node(key='item_3', value=1)]
Key: item_4, Value: [Node(key='item_4', value=0)]
Key: item_5, Value: [Node(key='item_5', value=40)]
Key: item_6, Value: None
********************************************************************************
```
