class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isBalanced(self, root):
        self.isBalanced = True

        def dfs(node):
            if not node:
                return 0

            left = dfs(node.left) 
            right = dfs(node.right) 

            if abs(left - right) > 1:
                self.isBalanced = False
            
            return 1 + max(left, right)

        dfs(root)
        return self.isBalanced