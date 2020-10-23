class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"Node({self.val})"


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode()
        pree = node
        while l1 or l2:
            if l1 is None:
                node.next = l2
                break
            if l2 is None:
                node.next = l1
                break
            if l1.val < l2.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            else:
                node.next = l2
                node = node.next
                l2 = l1.next
        return pree.next


class Solution1:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode()
        pree = node
        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                node = node.next
                l1 = l1.next
            else:
                node.next = l2
                node = node.next
                l2 = l1.next
        if l1 is None:
            node.next = l2
        if l2 is None:
            node.next = l1
        return pree.next
