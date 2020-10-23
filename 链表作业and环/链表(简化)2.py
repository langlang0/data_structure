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

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise Exception("索引越界")
        if index == 0:
            remove_data = self.head
            self.head = self.head.next
            remove_data.next = None
        elif index == self.size - 1:
            temp = self.get(index - 1)
            remove_data = temp.next
            temp.next = None
            self.tail = temp
        else:
            temp = self.get(index - 1)
            remove_data = temp.next
            temp.next = temp.next.next
            remove_data.next = None
        self.size -= 1
        return remove_data

    def reverse(self):
        prev = None
        curr = self.head
        self.tail = curr
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        self.head = prev


if __name__ == '__main__':
    ll = LinkList()
    ll.insert(0, 1)
    ll.insert(0, 2)
    ll.insert(2, 3)
    ll.insert(1, 5)
    print(ll)
    ll.remove(3)
    print(ll)
    ll.reverse()
    print(ll)
    print(ll.get(2))
