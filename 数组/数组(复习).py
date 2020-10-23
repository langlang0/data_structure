class Array:
    def __init__(self, carapy):
        self.array = [None] * carapy
        self.size = 0

    def addcapacity(self):
        new_array = [None] * len(self.array) * 2
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("索引越界")
        if index >= len(self.array) and self.size >= len(self.array):
            self.addcapacity()
        for i in range(self.size - 1, index - 1, -1):
            self.array[i + 1] = self.array[i]
        self.array[index] = element
        self.size += 1

    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("索引越界")
        if self.size >= len(self.array):
            self.addcapacity()
        for i in range(index, self.size):
            self.array[i] = self.array[i + 1]
        self.size -= 1

    def output(self):
        string = ""
        for i in range(self.size - 1):
            string += f"{self.array[i]} --> "
        return string + f"{self.array[self.size - 1]}"


ll = Array(10)
ll.insert(0, 1)
ll.insert(0,19)
ll.remove(1)

print(ll.output())
