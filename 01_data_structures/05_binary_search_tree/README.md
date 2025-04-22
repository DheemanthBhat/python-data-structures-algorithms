# Binary Search Tree (BST)

## 1 Testing

### 1.1 Commands

Test BST using below commands:

> **Note**:  
> Run the command from project root folder `python-data-structures-algorithms`.

```sh
python 01_data_structures/05_binary_search_tree/main.py
```

### 1.2 Output

#### Case 1: When duplicates are NOT allowed in Binary Search Tree

```log
************************* Case 1: Reject duplicates *************************
Initialize empty Binary Search Tree:

Insert below 15 values into Binary Search Tree:
[50, 70, 55, 30, 40, 56, 80, 41, 35, 75, 54, 20, 90, 0, 25]

Display Binary Search Tree:
Root: Node(left=30, value=50, right=70)
Max level: 4

                     50
         30                      70
   20          40          55          80
 0    25    35    41    54    56    75    90


Check if values: [56, 0, -20] exists in Binary Search Tree:
Value: '56' found in BST.
Value: '0' found in BST.
Value: '-20' NOT found in BST.
********************************************************************************
```

#### Case 2: When duplicates are allowed in Binary Search Tree

```log
************************* Case 2: Allow duplicates *************************
Initialize empty Binary Search Tree:

Insert below 7 values into Binary Search Tree:
[50, 60, 40, 50, 60, 45, 60]

Display Binary Search Tree:
Root: Node(left=40, value=50, right=60)
Max level: 4

                     50
         40                      60
               45          50          60
                                          60


Check if values: [60, 0, 45] exists in Binary Search Tree:
Value: '60' found in BST.
Value: '0' NOT found in BST.
Value: '45' found in BST.
********************************************************************************
```
