class Node:
    def __init__(self,data):
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

    def get(self,index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self,index,data):
        temp = Node(data)
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        if self.size == 0:
            self.head = temp
            self.tail = temp
        elif index == 0:
            temp.next = self.head
            self.head = temp
        elif index == self.size:
            self.tail.next = temp
            self.tail = temp
        else:
            curr = self.get(index - 1)
            temp.next = curr.next
            curr.next = temp
        self.size += 1

    def remove(self,index):
        if index < 0 or index >=self.size:
            raise Exception("索引越界")
        if index == 0:
            remove_node = self.head
            self.head = self.head.next
            remove_node.next = None
        elif index == self.size:
            remove_node = self.tail
            temp = self.get(index - 1)
            temp.next = None
            self.tail = temp
        else:
            remove_node = self.get(index)
            temp = self.get(index - 1)
            temp.next = temp.next.next
            remove_node.next = None
        self.size -= 1
        return remove_node

    def reciprocal(self,index):
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        temp = self.get(self.size - index)
        return temp
