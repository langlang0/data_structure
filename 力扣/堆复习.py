class Heap:
    def __init__(self):
        self.data_list = []

    def get_parent(self,index):
        if index < 0 or index > len(self.data_list) - 1:
            return None
        else:
            return (index - 1) >> 1

    def swap(self,a,b):
        self.data_list[a],self.data_list[b] = self.data_list[b],self.data_list[a]

    def insert(self,data):
        self.data_list.append(data)
        