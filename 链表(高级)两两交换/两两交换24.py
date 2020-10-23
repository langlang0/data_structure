class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head):
        node = ListNode()           # 添加虚拟头部
        node.next = head
        prev = node
        while prev.next and prev.next.next:
            curr = prev.next
            temp = prev.next.next
            curr.next = temp.next
            temp.next = curr
            prev.next = temp
            prev = prev.next.next
        return node.next







