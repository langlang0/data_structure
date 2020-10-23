class Array:
    def __init__(self, capacity):
        self.array = [None] * capacity
        self.size = 0

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("索引越界")
        if index >= len(self.array) or self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("索引越界")
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1


