class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)


class LinkList:
    def __init__(self):
        self.head = None

    def __repr__(self):
        current = self.head
        string_repr = ""
        while current:
            string_repr += "{} --> ".format(current)
            current = current.next
        return string_repr + "END"

    def insert_head(self, data):         # 添加头
        node = Node(data)
        if self.head is not None:
            node.next = self.head
        self.head = node

    def append(self, data):              # 添加尾
        node = Node(data)
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def insert(self, index, data):
        node = Node(data)
        if index == 1 or self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            pre = temp
            for i in range(1, index):
                pre = temp
                temp = temp.next
            pre.next = node
            node.next = temp

    def del_head(self):
        if self.head is None:
            return "链表为空"
        else:
            self.head = self.head.next

    def del_end(self):
        temp = self.head
        if temp:
            if temp.next is None:
                self.head = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
        else:
            return "空链表"

    def linklist(self, data: list):
        self.head = Node(data[0])
        temp = self.head
        for i in data[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next


ll = LinkList()
ll.insert_head(11)
ll.insert_head(12)
ll.insert_head(13)
ll.append(14)
ll.insert(2,99)
print(ll)