class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += f"{temp} --> "
            temp = temp.next
        return string_repr + "END"

    def reverse(self, node: Node):
        pre = None
        cur = node
        temp = cur.next
        while cur:
            cur.next = pre
            pre = cur
            cur = temp
            temp = temp.next
        self.head = pre


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    node6.next = node7
    l = LinkList()
    l.reverse(node1)