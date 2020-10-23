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

    def get(self, index):                       # 查找
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, data):              # 插入结点
        new_node = Node(data)
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        if self.size == 0 and index == 0:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        elif index == self.size:
            self.tail.next = new_node
            self.tail = new_node
        else:
            temp = self.get(index - 1)
            new_node.next = temp.next
            temp.next = new_node
        self.size += 1

    def remove(self, index):                        # 移除结点
        if index < 0 or index >= self.size:
            raise Exception("索引越界")
        if index == 0:
            self.head = self.head.next
            remove_node = self.get(index)
        elif index == self.size - 1:
            prev = self.get(index - 1)
            remove_node = self.get(index)
            prev.next = None
            self.tail = prev
        else:
            prev = self.get(index - 1)
            remove_node = self.get(index)
            prev.next = prev.next.next
            remove_node.next = None
        self.size -= 1
        return remove_node

    def reverse(self):                              # 翻转链表
        prev = None
        current = self.head
        self.tail = current
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        self.head = prev


if __name__ == '__main__':
    ll = LinkList()
    ll.insert(0, 2)
    ll.insert(0, 3)
    ll.insert(0, 5)
    ll.insert(2, 999)
    print(ll, ll.size)
    ll.remove(2)
    print(ll, ll.size)
    ll.reverse()
    print(ll)
