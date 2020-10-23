from typing import List             # 导入列表模块


class Node:                         # 定义结点函数
    def __init__(self, data):       # 结点函数的类属性
        self.data = data            # 结点当前值
        self.next = None            # 结点指针

    def __repr__(self):             # 实例化输出
        return "Node({})".format(self.data)


class LinkList:                     # 定义链表函数
    def __init__(self):             # 链表属性(头部)
        self.head = None

    def insert_head(self, data):    # 往链表头部插入数据
        node = Node(data)           # 要插入的结点
        if self.head:               # 如果链表头部有值,则执行的函数
            node.next = self.head
        self.head = node

    def append(self, data):         # 往链表尾部添加数据
        node = Node(data)
        if self.head is None:
            self.insert_head(data)
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = node

    def insert(self, index, data):  # 往链表固定位置添加结点
        if index == 1 or self.head is None:
            self.insert_head(data)
        else:
            node = Node(data)
            temp = self.head
            pre = temp
            for i in range(1, index):
                pre = temp
                temp = temp.next
            pre.next = node
            node.next = temp

    def __repr__(self):                # 实例化输出链表
        current = self.head
        string_repr = ""
        while current:
            string_repr += "{} --> ".format(current)
            current = current.next
        return string_repr + "END"

    def link_list(self, data: List):     # 传入列表,生成链表
        self.head = Node(data[0])
        temp = self.head
        for i in data[1:]:
            node = Node(i)
            temp.next = node
            temp = temp.next

    def del_head(self):                 # 删除头部结点
        if self.head is None:
            print("该链表为空")
        else:
            self.head = self.head.next

    def del_end(self):                  # 删除尾部结点
        temp = self.head
        if temp:
            if self.head.next is None:
                self.head = None
            else:
                while temp.next.next is not None:
                    temp = temp.next
                temp.next = None
        else:
            return "空链表"

    def del_index(self, index):          # 删除指定下标结点
        if index == 1:
            self.del_head()
        else:
            temp = self.head
            pre = temp
            end = temp.next.next
            for i in range(1, index):
                pre = temp
                temp = temp.next
                end = temp.next
            pre.next = end

    def reverse(self):                      # 翻转链表
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def __getitem__(self, index):           # 查找结点(索引)
        current = self.head

        if current is None:
            raise IndexError("The Linked List is empty.")

        for _ in range(1, index):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        return current

    def get(self, index):                    # 修改结点数据
        return self.__getitem__(index)

    def __setitem__(self, index: int, data):
        current = self.head

        if current is None:
            raise IndexError("The Linked List is empty")

        for _ in range(1, index):
            if current.next is None:
                raise IndexError("Index out of range.")
            current = current.next
        current.data = data

    def set(self, index, data):
        self.__setitem__(index, data)


if __name__ == '__main__':
    ll = LinkList()
    ll.insert_head(11)
    ll.insert_head(12)
    ll.insert_head(13)
    ll.append(14)
    ll.append(15)
    ll.insert(2, 99)
    print(ll)
    ll.del_head()
    print(ll)
    ll.del_end()
    print(ll)
    ll.del_index(2)
    print(ll)
    ll.reverse()
    print(ll)
    print(ll.get(2))
    ll.set(2, 999)
    print(ll)
