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

    def select(self,data):
        if self.root is None:
            raise Exception("空树")
        else:
            temp = self.root
            while temp:
                if temp.value == data:
                    return temp
                elif temp.value > data:
                    temp = temp.left
                else:
                    temp = temp.right

    def pre_order(self,node:Node):
        if node is None:
            return None
        else:
            print(node.value)
            self.pre_order(node.left)
            self.pre_order(node.right)

    def pre_order1(self):
        if self.root is None:
            return None
        else:
            temp = [self.root]
            while temp:
                curr = temp.pop()
                print(curr.value)
                if curr.right:
                    temp.append(curr.right)
                if curr.left:
                    temp.append(curr.left)




