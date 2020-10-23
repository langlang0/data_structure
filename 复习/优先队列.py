class PriorityQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self,data):
        self.array.append(data)
        self.size += 1
        self.heapify_up()

    def dequeue(self):
        if self.size <= 0:
            raise Exception('空队列')
        remove_data = self.array[0]
        self.array[0] = self.array[-1]
        del self.array[-1]
        self.size -= 1
        self.heapify_down()
        return remove_data

    def heapify_up(self):
        index = self.size - 1
        parent = (index - 1) >> 1
        new = self.array[index]
        while index > 0 and new > self.array[parent]:
            self.array[index] = self.array[parent]
            index = parent
            parent = (index - 1) >> 1
        self.array[index] = new

    def heapify_down(self):
        total_index = self.size - 1
        index = 0
        while True:
            maxvalue_index = index
            if 2 * index + 1 <= total_index and self.array[2 * index + 1] > self.array[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.array[2 * index + 2] > self.array[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.array[index], self.array[maxvalue_index] = self.array[maxvalue_index], self.array[index]
            index = maxvalue_index


if __name__ == '__main__':
    p = PriorityQueue()
    p.enqueue(1)
    p.enqueue(2)
    p.enqueue(3)
    p.enqueue(4)
    p.enqueue(5)
    p.enqueue(6)
    print(p.array)
    print(p.dequeue())
    print(p.array)





