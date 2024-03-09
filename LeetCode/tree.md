# Trees

## Explanation

A tree is a hierarchical data structure consisting of nodes, where each node has a value and a list of references to other nodes (its children). Trees are used to represent hierarchies and facilitate efficient information storage and retrieval operations.

## Example Problems

- **Binary Tree Traversal:** Perform in-order, pre-order, or post-order traversal of a binary tree.
- **Binary Search Tree (BST) Insertion and Search:** Insert a new node into a BST, and search for a value in a BST.

## Time Complexity

- The time complexity for traversing a tree is O(n), where n is the number of nodes, as each node is visited once.
- For a balanced BST, operations like insertion, deletion, and search can be done in O(log n) time.

## Space Complexity

- The space complexity is O(h) for recursive tree traversals, where h is the height of the tree, due to the call stack.
- For iterative traversal using an explicit stack, the space complexity is also O(h).

## Implementation

```python
# Python implementation for Tree Traversal (In-Order)

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorder_traversal(root):
    if root is not None:
        inorder_traversal(root.left)
        print(root.val, end=' ')
        inorder_traversal(root.right)
