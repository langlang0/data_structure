class Node:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return str(self.data)


class Tire:
    def __init__(self):
        self.root = Node()

    def insert(self, word):
        node = self.root
        for i in word:
            flag = node.data.get(i)
            if flag is None:
                node.data[i] = Node()
            node = node.data[i]
        node.is_word = True

    def search(self, word):
        node = self.root
        for i in word:
            flag = node.data.get(i)
            if flag is None:
                return False
        return node.is_word

    def startsWith(self,prefix):
        node = self.root
        for i in prefix:
            node = node.data.get(i)
            if node is None:
                return False
        return True



