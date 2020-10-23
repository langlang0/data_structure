class PriorityQueue:
    def __init__(self):
        self.array = []
        self.size = 0

    def enqueue(self, data):
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
        child_index = self.size - 1
        parent_index = (child_index - 1) >> 1
        temp = self.array[child_index]
        while child_index > 0 and temp > self.array[parent_index]:
            self.array[child_index] = self.array[parent_index]  # 孩子结点从新赋值
            child_index = parent_index  # 孩子结点上移,向着 0 移动
            parent_index = (child_index - 1) >> 1  # 父结点上移
        self.array[child_index] = temp

    def heapify_down(self):
        total_index = self.size - 1  # 数组的长度
        index = 0
        while True:
            maxvalue_index = index  #
            if 2 * index + 1 <= total_index and self.array[2 * index + 1] > self.array[maxvalue_index]:
                maxvalue_index = 2 * index + 1  # 如果左孩子结点大于当前最大节点,最大值索引等于左孩子索引
            if 2 * index + 2 <= total_index and self.array[2 * index + 2] > self.array[maxvalue_index]:
                maxvalue_index = 2 * index + 2  # 如果右孩子结点大于当前最大结点,最大值索引等于右孩子结点
            if maxvalue_index == index:  # 如果
                break
            self.array[index],self.array[maxvalue_index] = self.array[maxvalue_index],self.array[index]
            # self.swap(index, maxvalue_index)  # 交换最大值和和当前值
            index = maxvalue_index  # 当前值等于这一轮的最大值结点

if __name__ == '__main__':
    pq = PriorityQueue()
    pq.enqueue(3)
    pq.enqueue(5)
    pq.enqueue(10)
    pq.enqueue(2)
    pq.enqueue(7)
    print(pq.array)
    print(pq.dequeue())
    print(pq.array)