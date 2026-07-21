# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # A
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True

        left = self.calcHeight(root.left)
        right = self.calcHeight(root.right)

        if abs(left - right) > 1:
            return False
        
        if not self.isBalanced(root.left):
            return False

        if not self.isBalanced(root.right):
            return False

        return True


    
    def calcHeight(self, root: Optional[TreeNode]) -> int:
        if root == None:
            return 0

        left = self.calcHeight(root.left)
        right = self.calcHeight(root.right)

        return max(left, right) + 1 
        