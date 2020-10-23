class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent(self, index):   # 传入子节点索引,输出父节点的索引
        if index == 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self, index_a, index_b):  # 交换两个元素
        self.data_list[index_a], self.data_list[index_b] = self.data_list[index_b], self.data_list[index_a]

    def insert(self, data):
        self.data_list.append(data)
        index = len(self.data_list) - 1
        parent = self.get_parent(index)
        while parent is not None and self.data_list[index] > self.data_list[parent]:
            self.swap(index, parent)
            index = parent
            parent = self.get_parent(parent)

    def pop(self):
        remove_data = self.data_list[0]
        self.data_list[0] = self.data_list[-1]
        del self.data_list[-1]
        self.heapify(0)
        return remove_data

    def heapify(self, index):
        total_index = len(self.data_list) - 1
        while True:
            maxvalue_index = index
            if 2 * index + 1 <= total_index and self.data_list[2 * index + 1] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 1
            if 2 * index + 2 <= total_index and self.data_list[2 * index + 2] > self.data_list[maxvalue_index]:
                maxvalue_index = 2 * index + 2
            if maxvalue_index == index:
                break
            self.swap(index, maxvalue_index)
            index = maxvalue_index


if __name__ == '__main__':
    h = Heap()
    for i in range(10):
        h.insert(i)
    print("建堆: ", h.data_list)
    h.pop()
    print(h.data_list)
