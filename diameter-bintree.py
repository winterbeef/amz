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
    root.right.left.right = TreeNode(13)
    root.right.right.left = TreeNode(14)
    root.right.right.right = TreeNode(15)

    root.right.right.left.left = TreeNode(44)
    root.right.right.left.right = TreeNode(48)

    root.right.right.left.left.left = TreeNode(51)
    root.right.right.left.left.right = TreeNode(53)
    root.right.right.left.right.left = TreeNode(59)
    root.right.right.left.right.right = TreeNode(58)
    root.right.right.left.right.right.left = TreeNode(60)
    root.right.right.left.right.right.right = TreeNode(62)
    
    return root
def print_tree(node, level=0, prefix="Root: "):
    """Print the tree structure"""
    if node is not None:
        print(" " * (level * 4) + prefix + str(node.val))
        if node.left is not None or node.right is not None:
            print_tree(node.left, level + 1, "L--- ")
            print_tree(node.right, level + 1, "R--- ")
            
def diameterOfBinaryTree(root):
    maxdiameter = -1
    # returns 'height"; int
    def dfs(curr):
        nonlocal maxdiameter
        if not curr: 
            return 0
        
        left = dfs(curr.left)
        right = dfs(curr.right)

        maxdiameter = max(maxdiameter, left+right)
        return 1 + max(left, right)

    return dfs(root)
    

if __name__ == "__main__":
    # Generate the binary tree
    tree = create_binary_tree()    
    print_tree(tree)
    dia = diameterOfBinaryTree(tree)
    print(f"Diameter: {dia}")
