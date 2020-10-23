class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def __str__(self):
        return str(self.stack)

    def push(self, data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        if self.stack:
            temp = self.stack[-1]
            self.stack.pop()
            self.size -= 1
            return temp
        else:
            raise IndexError("索引越界")

    def peek(self):
        if self.stack:
            return self.stack[-1]

    def is_empty(self):
        if self.stack:
            return False
        else:
            return True


    def length(self):
        return self.size


if __name__ == '__main__':
    s = Stack()
    s.push(12)
    s.push(14)
    s.push(16)
    s.push(18)
    s.push(20)
    print(s.peek())
    print(s.length())
    print(s.is_empty())
    print(s)
