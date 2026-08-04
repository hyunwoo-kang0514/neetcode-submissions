# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # find the value of the subroot
        self.arr = []
        self.findSubRootLoc(root, subRoot.val)
    
        if len(self.arr) == 0:
            return False
    
        for tree in self.arr:
            isSame = self.isSameTree(tree, subRoot)
            if isSame:
                return True
        return False


    def findSubRootLoc(self, root, val):
        if root == None:
            return None
        if root.val == val:
            self.arr.append(root)
        self.findSubRootLoc(root.left, val)
        self.findSubRootLoc(root.right, val)

    def isSameTree(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        