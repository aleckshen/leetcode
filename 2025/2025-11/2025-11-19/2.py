class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l1_s = ""
        l2_s = ""
        
        while l1:
            l1_s += str(l1.val)
            l1 = l1.next

        while l2:
            l2_s += str(l2.val)
            l2 = l2.next

        res = str(int(l1_s[::-1]) + int(l2_s[::-1]))
        
        head = ListNode(int(res[-1]))
        curr = head

        res = res[:len(res) - 1]
        
        for s in res[::-1]:
            curr.next = ListNode(int(s))
            curr = curr.next

        return head