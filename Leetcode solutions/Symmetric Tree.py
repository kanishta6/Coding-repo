# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.isMirror(root.left,root.right)

    def isMirror(self,leftroot,rightroot):
        if leftroot==None and rightroot==None:
            return True
        if leftroot==None or rightroot==None:
            return False
        if leftroot.val!=rightroot.val:
            return False
        return self.isMirror(leftroot.left,rightroot.right) and self.isMirror(leftroot.right,rightroot.left)
        