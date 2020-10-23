class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def __repr__(self):
        return f"Node({self.data})"


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self,data):
        node = Node(data)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("空栈")
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.size -= 1

    def output(self):
        print(self.top)

if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    s.pop()
    s.output()
