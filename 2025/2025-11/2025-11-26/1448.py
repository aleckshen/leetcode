class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        self.count = 0

        def dfs(node, max_val):
            if not node:
                return 0

            if node.val >= max_val:
                self.count += 1
                max_val = node.val

            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, root.val)

        return self.count