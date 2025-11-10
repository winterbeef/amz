#!/usr/bin/env python

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
    root.left.left.left = TreeNode(8)
    root.left.left.right = TreeNode(9)
    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(11)
    root.right.left.left = TreeNode(12)
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)
    
    return root

def print_tree(node, level=0, prefix="Root: "):
    """Print the tree structure"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")

def get_tree_height(node):
    """Calculate the height of the tree"""
    if node is None:
        return 0
    return 1 + max(get_tree_height(node.left), get_tree_height(node.right))

if __name__ == "__main__":
    # Generate the binary tree
    tree = create_binary_tree()
    
    # Display the tree
    print("Binary Tree Structure:")
    print_tree(tree)
    
    # Show the height
    height = get_tree_height(tree)
    print(f"\nTree height: {height} levels")