import collections

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def rightSideView(self, root):
        res = []
        queue = collections.deque([root])

        while queue:
            rightNode = None

            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    rightNode = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightNode:
                res.append(rightNode.val)

        return res