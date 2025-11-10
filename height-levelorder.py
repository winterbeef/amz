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
    root.left = TreeNode(22)
    root.right = TreeNode(23)
    
    # Level 3
    root.left.left = TreeNode(34)
    root.left.right = TreeNode(35)
    root.right.left = TreeNode(36)
    root.right.right = TreeNode(37)
    
    # Level 4
    root.right.left.left = TreeNode(42)
    root.right.right.left = TreeNode(44)
    root.right.right.right = TreeNode(49)

    root.right.right.right.left = TreeNode(52)
    
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
    q = deque([(root, 1)])
    maxheight = 0

    while q:
        ## Can NOT iterate on the q directly, since it mutates.
        qq = getq(q)
        print(f"======\nqIN : {qq}")
        for _ in range(len(q)): 
            (cur, curh) = q.popleft()

            maxheight = max(maxheight, curh)
            if cur.left:
                q.append( (cur.left, curh+1) )
            if cur.right:
                q.append( (cur.right, curh+1) )
            qq = getq(q)
            print(f"qOUT: {qq}")

    return maxheight

def getq(q):
    vals = ", ".join([str(n.val) for (n,h) in q])
    return f"[{vals}]"

if __name__ == "__main__":
    # Generate the binary tree
    tree = create_binary_tree()
    
    # Display the tree
    print("Binary Tree Structure:")
    print_tree(tree)
    
    # Show the height
    height = get_tree_height(tree)
    print(f"\nTree height: {height} levels")
    