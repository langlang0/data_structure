class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return  "Node({})".format(self.data)

class LinkedList:
    def __init__(self):
        self.head = None

    # 尾部添加结点
    def append(self,data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    # 头部插入结点
    def insert_head(self,data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node
