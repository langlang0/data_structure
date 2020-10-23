class QueueList:
    def __init__(self):
        self.entries = []
        self.size = 0

    def __repr__(self):
        printed = "< " + str(self.entries)[1:-1] + " >"
        return printed

    def push(self, data):
        self.entries.append(data)
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("索引越界")
        move = self.entries[0]
        self.entries.pop(0)
        return move

    def get(self,index):
        return self.entries[index]

    def set(self,index,data):
        self.entries[index] = data

    def reverse(self):
        self.entries.reverse()


if __name__ == '__main__':
    q = QueueList()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)
    q.push(5)
    q.pop()
    print(q)
    print(q.get(2))
    q.set(1,324)
    print(q)
    q.reverse()
    print(q)