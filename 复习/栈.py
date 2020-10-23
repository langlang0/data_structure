class StackList:
    def __init__(self):
        self.list = []
        self.size = 0

    def puck(self,data):
        self.list.append(data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("索引越界")
        move = self.list[-1]
        self.list.pop()
        self.size -= 1
        return move

class Node:
    def __init__(self,data):
        self.val = data
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"




class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def __str__(self):
        return str(self.top)

    def puck(self,data):
        node = Node(data)
        if self.size == 0:
            self.top = node
        else:
            node.next = self.top
            self.top = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("索引越界")
        move = self.top
        self.top = self.top.next
        move.next = None
        self.size -= 1
        return move