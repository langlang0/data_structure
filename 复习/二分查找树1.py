from pprint import pformat


class Node:
    def __init__(self, data):
        self.value = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.value)
        return pformat({"%s" % (self.value): (self.left, self.right)}, indent=1)


class Tree:
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
                if data < temp.value:
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

    def insert(self, *values):
        for i in values:
            self.__insert(i)
        return self

    def search(self, data):                 # def search(self, data):
        if self.root is None:               #     if self.root is None:
            raise IndexError("空树")        #         raise Exception("空树")
        else:                               #     else:
            if self.root.value == data:     #         if self.root.value == data:
                return self.root            #             return self.root
            parent = self.root              #         temp = self.root
            while parent:                   #         while temp:
                if data < parent.value:     #             if data < temp.value:
                    parent = parent.left    #                 temp = temp.left
                elif data > parent.value:   #             elif data > temp.value:
                    parent = parent.right   #                 temp = temp.left
                else:                       #             else:
                    return parent           #                 return temp

    # def search(self, data):
    #     if self.root is None:
    #         raise Exception("空树")
    #     else:
    #         if self.root.value == data:
    #             return self.root
    #         temp = self.root
    #         while temp:
    #             if data < temp.value:
    #                 temp = temp.left
    #             elif data > temp.value:
    #                 temp = temp.left
    #             else:
    #                 return temp

    def remove(self, data):
        pop_node = self.search(data)
        if pop_node is not None:
            if pop_node.left is None and pop_node.right is None:
                self.__arrs_node(pop_node, None)
            elif pop_node.left is None:
                self.__arrs_node(pop_node, pop_node.right)
            elif pop_node.right is None:
                self.__arrs_node(pop_node, pop_node.left)
            else:
                temp = self.__ismax(pop_node.left)
                self.remove(temp.value)
                pop_node.value = temp.value
        else:
            raise Exception("无该节点")

    def __arrs_node(self, pop_node, new_child):
        if new_child is not None:
            new_child.parent = pop_node.parent
        if pop_node.parent is not None:
            if self.is_right(pop_node):
                pop_node.parent.right = new_child
            else:
                pop_node.parent.left = new_child
        else:
            self.root = new_child

    def __ismax(self, node):
        while node.right:
            node = node.right
        return node

    def is_right(self, pop_node):
        return pop_node == pop_node.parent.right


if __name__ == '__main__':
    t = Tree()
    t.insert(5, 3, 7, 2, 4, 6, 8)
    print(t)
    print(t.search(3))
    t.remove(3)
    print(t.root)
