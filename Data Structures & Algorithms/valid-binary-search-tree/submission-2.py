# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    """
          50
       40    60
      35 52 41

    범위: 40 <= x <= 50

    to the right subtree -> min = root.val, max = given from parent node
    to the left subtree -> min = None, max root.val

    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root == None:
            return True
        return self.dfs(root, float('-inf'), float('inf'))
    
    def dfs(self, root, left, right) -> bool:
        if root == None:
            return True
        if not (root.val > left and root.val < right): 
            return False
        
        return self.dfs(root.left, left, root.val) and self.dfs(root.right, root.val, right)


        