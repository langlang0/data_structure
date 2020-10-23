from pprint import pformat


class Node:
    def __init__(self, data):
        self.val = data
        self.parent = None
        self.left = None
        self.right = None

    def __repr__(self):
        if self.left is None and self.right is None:
            return str(self.val)
        return pformat({"%s" % (self.val): (self.left, self.right)}, indent=1)


class Tree:
    def __init__(self):
        self.root = None

    def add(self, data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            parent = self.root
            while True:
                if data < parent.val:
                    if parent.left is None:
                        parent.left = node
                        break
                    else:
                        parent = parent.left
                else:
                    if parent.right is None:
                        parent.right = node
                        break
                    else:
                        parent = parent.right
            node.parent = parent

    def search(self, data):
        if self.root is None:
            raise IndexError("空树")
        temp = self.root
        while temp:
            if data > temp.val:
                temp = temp.right
            elif data < temp.val:
                temp = temp.left
            else:
                return temp

    def remove(self, data):
        node = self.search(data)
        if node is not None:
            if node.left is None and node.rigth is None:
                self.__reassign_nodes(node, None)
            elif node.left is None:
                self.__reassign_nodes(node, node.rigth)
            elif node.rigth is None:
                self.__reassign_nodes(node, node.left)
            else:
                temp = self.ismax(node.left)
                self.remove(temp.val)
                node.val = temp.val
        else:
            raise Exception("没有该结点")

    def __reassign_nodes(self, node, new_children):
        if new_children:
            new_children.parent = node.parent
        if node.parent:
            if self.is_right(node):
                node.parent.right = new_children
            else:
                node.parent.left = new_children
        else:
            self.root = new_children

    def is_right(self,node):
        return node == node.parent.right

    def ismax(self, node):
        if node is None:
            raise Exception("无左树最大值")
        while node.right:
            node = node.right
        return node


if __name__ == '__main__':
    t = Tree()
    t.add(5)
    t.add(2)
    t.add(4)
    t.add(7)
    t.add(9)
    t.add(3)
    print(t.root)
    print(t.search(4))
