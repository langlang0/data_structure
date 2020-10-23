from pprint import pformat


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (
            self.left, self.right)}, indent=1)


class Tree:     # BinarySearchTree
    def __init__(self):
        self.root = None

    def __str__(self):
        return str(self.root)

    def is_empty(self):
        if self.root is None:
            return True
        else:
            return False

    def __insert(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self.root = new_node
        else:
            parent_node = self.root
            while True:
                if new_node.value < parent_node.value:
                    if parent_node.left is None:
                        parent_node.left = new_node
                        break
                    else:
                        parent_node = parent_node.left
                else:
                    if parent_node.right is None:
                        parent_node.right = new_node
                        break
                    else:
                        parent_node = parent_node.right
            new_node.parent = parent_node

    def insert(self, *args):
        for i in args:
            self.__insert(i)
        return self

    def search(self, data):
        if self.root is None:
            raise IndexError("空树")
        else:
            if self.root.value == data:
                return self.root
            parent = self.root
            while parent:
                if data < parent.value:
                    parent = parent.left
                elif data > parent.value:
                    parent = parent.right
                else:
                    return parent

    def is_right(self, node):       # 判断当前结点是否为其父结点右侧结点
        return node == node.parent.right

    def __reassign_nodes(self, node, new_children):
        if new_children is not None:        # 当前结点的子结点不为空
            new_children.parent = node.parent       # 子结点取代当前结点指向当前结点的父结点
        if node.parent is not None:     # 当前结点的父结点不为空
            if self.is_right(node):     # 判断当前结点是否为其父结点右侧结点
                node.parent.right = new_children    # 将父结点的右侧结点替换为子结点
            else:
                node.parent.left = new_children     # 将父结点的左侧结点替换为子结点
        else:
            self.root = new_children

    def remove(self, value):
        node = self.search(value)     # 查询当前结点
        if node is not None:
            if node.left is None and node.right is None:    # 当前结点没有子结点时
                self.__reassign_nodes(node, None)
            elif node.left is None:             # 当前结点只有右结点时
                self.__reassign_nodes(node, node.right)
            elif node.right is None:            # 当前结点只有左结点时
                self.__reassign_nodes(node, node.left)
            else:                               # 当前结点有左右结点时
                tmp_node = self.get_max(node.left)        # 找到左子树中的最大结点
                self.remove(tmp_node.value)     # 删除左子树中的最大结点
                node.value = tmp_node.value     # 将左子树中最大结点的值替换掉当前结点的值
        else:
            raise IndexError("当前树中没有该结点")

    def get_max(self, node=None):
        if node is None:
            node = self.root
        if self.root:
            while node.right:
                node = node.right
        return node

    def pre_order1(self, node):   # 中序遍历
        if node.left is None and node.right is None:
            return [node.value]
        elif node.right is None:
            return self.pre_order1(node.left) + [node.value]
        elif node.left is None:
            return [node.value] + self.pre_order1(node.right)
        else:
            return self.pre_order1(node.left) + [node.value] + self.pre_order1(node.right)

    def pre_order2(self, node):  # 前序遍历  递归
        if node is None:
            return None
        print(node.value, end=" ")
        self.pre_order2(node.left)
        self.pre_order2(node.right)

    def pre_order3(self, node):   # 前序遍历,非递归
        stack = [node]
        while len(stack) > 0:
            print(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            node = stack.pop()

    def in_order(self, node):               # 栈实现中序遍历,非递归
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.value,end=" ")
                node = node.right

    def post_order(self, node):
        if node is None:
            return False
        stack1 = []   # 方便遍历
        stack2 = []   # 方便输出
        stack1.append(node)
        while stack1:
            node = stack1.pop()
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
            stack2.append(node)
        while stack2:
            print(stack2.pop().value, end=" ")

    def level_order(self):
        if self.root is None:
            return None
        else:
            temp = [self.root]
            while temp:
                node = temp.pop(0)
                print(node.value,end=" ")
                if node.left:
                    temp.append(node.left)
                if node.right:
                    temp.append(node.right)

    def level_order1(self):
        from queue import Queue
        queue = Queue()
        queue.put(0)
        while not queue.empty():
            node = queue.get()
            print(node.value)
            if node.left:
                queue.put(node.left)
            if node.right:
                queue.put(node.right)









if __name__ == '__main__':
    t = Tree()
    t.insert(4, 2, 6, 1, 3, 5, 7)
    print(t)
    print(t.search(5))
    print(t.root)
    print(t.pre_order1(t.root))
    t.in_order(t.root)
    print()
    t.pre_order2(t.root)
    print()
    t.level_order()
