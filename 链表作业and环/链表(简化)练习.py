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
        new_nota = Node(data)
        if index < 0 or index > self.size:
            raise Exception("索引越界")
        if self.size == 0 and index == 0:
            self.head = new_nota
            self.tail = new_nota
        elif index == 0:
            new_nota.next = self.head
            self.head = new_nota
        elif index == self.size:
            self.tail.next = new_nota
            self.tail = new_nota
        else:
            current = self.get(index - 1)
            new_nota.next = current.next
            current.next = new_nota
        self.size += 1

    def remove(self,index):
        if index < 0 or index >= self.size:
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
            current = self.get(index - 1)
            current.next = current.next.next
            remove_node.next = None
        self.size -= 1
        return remove_node

    def reverse(self):
        prev = None
        temp = self.head
        self.tail = temp
        while temp.next:
            curr = temp.next
            temp.next = prev
            prev = temp
            temp = curr
        self.head = prev



if __name__ == '__main__':
    ll = LinkList()
    ll.insert(0,1)
    ll.insert(0,2)
    ll.insert(0, 3)
    ll.insert(0, 4)
    ll.insert(0, 5)
    print(ll)
    ll.remove(0)
    print(ll)
    ll.remove(3)
    print(ll)
    ll.reverse()
    print(ll)