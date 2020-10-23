class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


def exchange(node: Node):
    dummy = Node(0)
    pre = dummy
    dummy.next = node
    while node and node.next:
        cur = node
        temp = node.next

        cur.next = temp.next
        temp.next = cur
        pre.next = temp

        pre = pre.next.next
        node = pre.next
    return dummy.next


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
    print(exchange(node1).next.next.next.next.next.next)
