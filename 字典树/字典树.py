class TrieNode:
    def __init__(self):
        self.data = {}
        self.is_word = False

    def __repr__(self):
        return str(self.data)


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,word):
        node = self.root
        for char in word:
            child = node.data.get(char)
            if child is None:
                node.data[char] = TrieNode()
            node = node.data[char]
        node.is_word = True

    def search(self,word):
        node = self.root
        for i in word:
            node = node.data.get(i)
            if node is None:
                return False
        return node.is_word

    def startsWith(self,prefix):
        node = self.root
        for i in prefix:
            node = node.data.get(i)
            if node is None:
                return False
        return True

    def get_start(self, prefix: str):
        pass

    def get_key(self):
        pass


if __name__ == '__main__':
    t = Trie()
    t.insert('hellow word')
    t.insert('hellow boy')
    t.insert('hellow girl')
    print(t.root.data)
    print(t.search('hellow'))
    print(t.startsWith('hellow'))