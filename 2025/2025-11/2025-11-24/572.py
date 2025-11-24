class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        if not subRoot:
            return True
        
        if not root:
            return False

        if self.sameTree(root, subRoot):
            return True

        left = self.isSubtree(root.left, subRoot)
        right = self.isSubtree(root.right, subRoot)
        return left or right

    def sameTree(self, p, q):
        if not p and not q:
            return True
            
        if p and q and p.val == q.val:
            left = self.sameTree(p.left, q.left)
            right = self.sameTree(p.right, q.right)
            return left and right
        else:
            return False