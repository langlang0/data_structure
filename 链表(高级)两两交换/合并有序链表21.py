class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        cur = dummy
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if l1 is None:
            cur.next = l2
        if l2 is None:
            cur.next = l1
        return dummy.next


a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(4)
b1 = ListNode(1)
b2 = ListNode(3)
b3 = ListNode(4)
a1.next = a2
a2.next = a3
b1.next = b2
b2.next = b3
s = Solution()
print(s.mergeTwoLists(a1, b1))
