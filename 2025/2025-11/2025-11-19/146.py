class Node(object):

    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev, self.next = None, None

class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {} # maps key to nodes
        self.left, self.right = Node(0, 0), Node(0, 0) #left pointer will represent least recently used and right will represent most recently used
        self.left.next = self.right
        self.right.prev = self.left

    # insert to right (most recently used)
    def insert(self, node):
        left = self.right.prev
        left.next = node
        node.prev = left
        node.next = self.right
        self.right.prev = node

    # remove node from list
    def remove(self, node):
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
    def get(self, key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]