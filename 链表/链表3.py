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
        temp = self.head
        string_repr = ""
        while temp:
            string_repr += "{} --> ".format(temp)
            temp = temp.next
        return string_repr + "END"

    def insert_head(self, data):            # 头部插入数据
        node = Node(data)
        if self.head:
            node.next = self.head
        self.head = node

    def append(self, data):                  # 尾部插入数据
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def insert(self, index, data):            # 固定位置插入数据
        node = Node(data)
        if index == 1 or self.head is None:
            self.head = node
        else:
            temp = self.head
            pre = temp.next
            for i in range(1, index):
                temp = temp.next
                pre = temp.next
            temp.next = node
            node.next = pre

    def del_head(self):                        # 删除头部
        if self.head is None:
            return "空链表"
        else:
            self.head = self.head.next

    def del_end(self):                          # 删除尾部
        temp = self.head
        if temp:
            if temp.next is None:
                self.head = None
            else:
                while temp.next.next:
                    temp = temp.next
                temp.next = None

    def linklist(self, data: list):
        self.head = Node(data[0])
        node = self.head
        for i in data[1:]:
            node.next = Node(i)
            node = node.next


ll = LinkList()
ll.insert_head(11)
ll.insert_head(12)
ll.insert_head(13)
ll.append(14)
ll.insert(2, 15)
print(ll)
ll.del_head()
print(ll)
ll.del_end()
print(ll)


lp = LinkList()
a = [0,1,2,3,4,5]
lp.linklist(a)
print(lp)