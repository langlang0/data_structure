class ListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


def insertSortList(head:ListNode):
    dummy = ListNode(0)
    pre = dummy
    cur = head
    while cur is not None:
        temp = cur.next
        while pre.next is not None and pre.next.data < cur.data:
            pre = pre.next

        cur.next = pre.next
        pre.next = cur

        cur = temp
        pre = dummy
    return dummy.next



