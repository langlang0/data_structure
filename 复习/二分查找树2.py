from pprint import pformat


class Node:
    def __init__(self, value, parent=None):
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

    def __insert(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            temp = self.root
            while True:
                if node.value < temp.value:
                    if temp.left is None:
                        temp.left = node
                        break
                    else:
                        temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = node
                        break
                    else:
                        temp = temp.right
            node.parent = temp

    # def __insert(self, value):
    #     new_node = Node(value, None)
    #     if self.root is None:
    #         self.root = new_node
    #     else:
    #         parent_node = self.root
    #         while True:
    #             if new_node.value < parent_node.value:
    #                 if parent_node.left is None:
    #                     parent_node.left = new_node
    #                     break
    #                 else:
    #                     parent_node = parent_node.left
    #             else:
    #                 if parent_node.right is None:
    #                     parent_node.right = new_node
    #                     break
    #                 else:
    #                     parent_node = parent_node.right
    #         new_node.parent = parent_node

    def insert(self, *valuers):
        for i in valuers:
            self.__insert(i)
        return self

    def search(self, data):
        if self.root is None:
            raise Exception("空树")
        else:
            temp = self.root
            while temp:
                if data < temp.value:
                    temp = temp.left
                elif data > temp.value:
                    temp = temp.right
                else:
                    return temp

    def remove(self, data):
        curr = self.search(data)
        if curr is None:
            raise Exception("查无此节点")
        else:
            if curr.left is None and curr.right is None:
                self.__sear_two(curr, None)
            elif curr.left is None:
                self.__sear_two(curr, curr.right)
            elif curr.right is None:
                self.__sear_two(curr, curr.left)
            else:
                temp = self.__ismax_left(curr.left)
                self.remove(temp.value)
                curr.value = temp.value

    def __sear_two(self, curr, new_child):
        if new_child:
            new_child.parent = curr.parent
        if curr.parent:
            if self.__isright(curr):
                curr.parent.right = new_child
            else:
                curr.parent.left = new_child
        else:
            self.root = new_child

    def __ismax_left(self, node):
        while node.right:
            node = node.right
        return node

    def __isright(self, curr):
        return curr == curr.parent.right

    def pre_order(self, node):
        if node is None:
            return None
        else:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def pre_order1(self, node):
        start = [node]
        while start:
            print(node.value)
            if node.right:
                start.append(node.right)
            if node.left:
                start.append(node.left)
            node = start.pop()

    def in_order1(self, node):
        stack = []
        while node or len(stack) > 0:
            while node:
                stack.append(node)
                node = node.left
            if len(stack) > 0:
                node = stack.pop()
                print(node.value)
                node = node.right

    def post_order(self, node):
        if node is None:
            return False
        stack1 = []
        stack2 = []
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


if __name__ == '__main__':
    t = Tree()
    t.insert(4, 2, 6, 1, 3, 5, 7)
    print(t)
    print(t.search(2))
    t.remove(4)
    print(t)
