class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f"Node({self.data})"


class LinkStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top is None:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("空栈")
        else:
            top = self.top
            self.top = self.top.next
            top.next = None
            self.size -= 1

    def peek(self):
        if self.top:
            return self.top

if __name__ == '__main__':
    l = LinkStack()
    l.push(12)
    l.push(23)
    print(l.peek())