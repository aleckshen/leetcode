class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):

        def dfs(node, currMin, currMax):
            if not node:
                return True

            if currMin >= node.val or node.val >= currMax:
                return False

            return dfs(node.left, currMin, node.val) and dfs(node.right,    node.val, currMax)

        return dfs(root, float('-inf'), float('inf'))