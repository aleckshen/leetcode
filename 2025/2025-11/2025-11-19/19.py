class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def removeNthFromEnd(self, head, n):
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        if count == 1:
            return None

        curr = head
        node_count = count - n
        prev = None

        while node_count > 0:
            node_count -= 1
            prev = curr
            curr = curr.next

        if prev == None:
            nxt = head.next
            head.next = None
            return nxt
            
        prev.next = curr.next

        return head