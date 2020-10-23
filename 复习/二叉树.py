class Node:
    def __init__(self,data):
        self.val = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f"Node({self.val})"


class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        node = Node(data)
        if self.root is None:
            self.root = node
        else:
            temp = [self.root]
            while True:
                cur = temp.pop(0)
                if cur.left is None:
                    cur.left = node
                    break
                elif cur.right is None:
                    cur.right = node
                    break
                else:
                    temp.append(cur.left)
                    temp.append(cur.right)

    def parent(self,data):
        if self.root.val == data:
            return None
        temp = [self.root]
        while temp:
            parent = temp.pop(0)
            if parent.left.val == data or parent.right.val == data:
                return parent
            else:
                temp.append(parent.left)
                temp.append(parent.right)
        return False


if __name__ == '__main__':
    t = Tree()
    t.insert(1)
    t.insert(2)
    t.insert(3)
    t.insert(4)
    t.insert(5)
    t.insert(6)
    t.insert(7)
    print(t.root.right.right)

