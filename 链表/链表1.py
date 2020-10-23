class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return "Node({})".format(self.data)


class LinkList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        if self.head is not None:
            new_node.next = self.head
        self.head = new_node

    def append(self, data):
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = Node(data)

    def __repr__(self):
        string_repr = ''
        current = self.head
        while current:
            string_repr += '{} --> '.format(current)
            current = current.next
        return string_repr + 'END'

    # def shuchu(self):
    #     temp = self.head
    #     while temp:
    #         print(temp.data)
    #         temp = temp.next

l = LinkList()
l.insert_head(99)
l.append(100)
l.append(101)
l.insert_head(98)
# l.shuchu()
print(l)
