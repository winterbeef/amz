#!/usr/bin/env python
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def create_binary_tree():
    """Create a binary tree with 4 levels"""
    # Level 1 (root)
    root = TreeNode(1)
    
    # Level 2
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    
    # Level 3
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    
    # Level 4
    root.right.left.left = TreeNode(12)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(99)

    root.right.right.right.left = TreeNode(98)
    
    return root

def print_tree(node, level=0, prefix="Root: "):
    """Print the tree structure"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

def get_tree_height(root):
    """
    """
    q = deque([root])
    height = 0

    while q:
        for n in range(len(q)): ## Can NOT iterate on the q directly, since it mutates.
            cur = q.popleft()

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        height += 1
    
    return height



if __name__ == "__main__":
    # Generate the binary tree
    tree = create_binary_tree()
    
    # Display the tree
    print("Binary Tree Structure:")
    print_tree(tree)
    
    # Show the height
    height = get_tree_height(tree)
    print(f"\nTree height: {height} levels")
    