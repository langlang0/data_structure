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

    def delete(self,data):
        node1 = Node(999999999)     # 虚拟结点,放置链表头部
        node1.next = self.head
        self.head = node1   # 将虚拟结点连接至链表头部
        node2 = Node(999999999)     # 虚拟结点,放置链表尾部
        self.tail.next = node2
        self.tail = node2   # 将虚拟结点连接至链表尾部

        prev = self.head    # 当前结点的前一结点
        curr = prev.next    # 当前结点

        while prev and prev.next:
            if prev.next.data == data:
                prev.next = prev.next.next
                curr.next = None
                prev = prev.next
                curr = prev.next
                self.size -= 1
            else:
                prev = prev.next
                curr = prev.next
        self.head = self.head.next              # 删除虚拟头部结点
        node1.next = None
        self.tail = self.get(self.size - 1)     # 删除虚拟尾部结点
        self.tail.next = None

if __name__ == '__main__':
    ll = LinkList()
    ll.insert(0,1)
    ll.insert(0,2)
    ll.insert(0,3)
    ll.insert(0,4)
    ll.insert(0,5)
    ll.insert(0,1)
    print(ll)
    ll.delete(1)
    print(ll)
