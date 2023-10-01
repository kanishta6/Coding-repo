# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p and q:
            
            # Both p and q are non-empty
            # Check equality on both subtree
            return (p.val == q.val) and self.isSameTree( p.left, q.left) and self.isSameTree( p.right, q.right )
        
        else:
            
            # At least one of them is empty
            # Check whether both p and q are empty or not
            return p == q