class TrieNode(object):
    def __init__(self):
        self.children = {}
        self.end = False

class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                current.children[ch] = TrieNode()
            current = current.children[ch]
        
        current.end = True

    def search(self, word):
        current = self.root

        for ch in word:
            if ch not in current.children:
                return False
            current = current.children[ch]

        if current.end:
            return True
        return False

    def startsWith(self, prefix):
        current = self.root

        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]

        return True