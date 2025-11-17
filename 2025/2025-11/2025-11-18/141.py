class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        nodes = set()
        curr = head

        while curr:
            if curr in nodes:
                return True
            nodes.add(curr)
            curr = curr.next

        return False