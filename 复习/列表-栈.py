class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def peek(self,data):
        self.stack.append(data)
        self.size += 1

    def pop(self):
        self.stack.pop()

    def output(self):
        print(self.stack[-1])

if __name__ == '__main__':
    s = Stack()
    s.peek(1)
    s.peek(2)
    s.peek(3)
    s.peek(4)
    s.peek(5)
    s.pop()
    s.output()
