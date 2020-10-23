class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


def remove(head, val):
    dummy = Node(0)
    dummy.next = head
    curr = dummy
    while curr.next:
        if curr.next.data == val:
            temp = curr.next
            curr.next = curr.next.next
            temp.next = None
        else:
            curr = curr.next
    return dummy.next


