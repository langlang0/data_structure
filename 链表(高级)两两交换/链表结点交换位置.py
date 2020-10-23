class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __repr__(self):
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += f"{temp} --> "
            temp = temp.next
        return string_repr + "END"

    def get(self, index):
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        new_node = Node(data)
        if self.size == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            curr = self.get(index - 1)
            new_node.next = curr.next
            curr.next = new_node
        self.size += 1

    def exchange(self, index1, index2):
        node1 = Node(999999999)  # 虚拟结点,放置链表头部
        node1.next = self.head
        self.head = node1  # 将虚拟结点连接至链表头部

        prev1 = self.head
        for _ in range(index1 - 1):
            prev1 = prev1.next
        curr1 = prev1.next

        temp = Node(999999999)                 # 插入虚拟结点
        temp.next = curr1.next
        curr1.next = temp

        prev2 = self.head
        for _ in range(index2 + 1):
            prev2 = prev2.next
        curr2 = prev2.next

        prev1.next, prev2.next, curr1.next, curr2.next = curr2, curr1, curr2.next, curr1.next

        self.head = self.head.next  # 删除虚拟头部结点
        node1.next = None
        curr2.next = curr2.next.next        # 删除虚拟结点
        temp.next = None


if __name__ == '__main__':
    ll = LinkList()
    ll.insert(0, 1)
    ll.insert(1, 2)
    ll.insert(2, 3)
    ll.insert(3, 4)
    ll.insert(4, 5)
    print(ll)
    ll.exchange(0, 1)
    print(ll)
