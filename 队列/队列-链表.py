class Node:
    def __init__(self, data):
        self.val = data
        self.next = None

    def __repr__(self):
        return f"Node({self.val})"


class LinkQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):                   # 查询
        if index < 0 or index > self.size - 1:
            raise IndexError("索引越界")
        output = self.head
        for _ in range(index):
            output = output.next
        return output

    def enqueue(self, data):                # 入队
        node = Node(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.size += 1

    def dequeue(self):                      # 出队
        if self.size == 0:
            raise Exception("空队列")
        move = self.head
        self.head = self.head.next
        move.next = None
        self.size -= 1
        return move

    def is_empty(self):
        if self.size == 0:
            return True
        else:
            return False
