class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.data})"


class Tree:
    def __init__(self):
        self.root = None

    def add(self,item):                                             # 添加树结点
        node = Node(item)
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]
            while True:
                pop_node = temp.pop(0)
                if pop_node.left is None:
                    pop_node.left = node
                    return
                elif pop_node.right is None:
                    pop_node.right = node
                    return
                else:
                    temp.append(pop_node.left)
                    temp.append(pop_node.right)

    def get_father(self,item):
        if self.root.data == item:
            return None
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left.data == item or pop_node.right.data == item:
                return pop_node
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        return None

    def get_father1(self,item):
        if self.root.data == item:
            return None
        res = []
        temp = [self.root]
        while temp:
            pop_node = temp.pop(0)
            if pop_node.left and pop_node.left.data == item:
                res.append(pop_node)
            if pop_node.right and pop_node.right.data == item:
                res.append(pop_node)
            if pop_node.left:
                temp.append(pop_node.left)
            if pop_node.right:
                temp.append(pop_node.right)
        return res


if __name__ == '__main__':
    t = Tree()
    t.add(1)
    t.add(2)
    t.add(3)
    t.add(6)
    t.add(5)
    t.add(6)
    t.add(7)
    print(t.root.right.right)
    print(t.get_father(6))