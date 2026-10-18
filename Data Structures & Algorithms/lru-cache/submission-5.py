class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.mru = Node(0, 0)
        self.lru = Node(0, 0)

        self.mru.prev = self.lru
        self.lru.next = self.mru

        self.capacity = capacity


    def get(self, key: int) -> int:
        cache = self.cache
        if key not in cache:
            return -1
        
        node = cache[key]
        self.remove(node)
        self.insert(node)

        return node.val

    def put(self, key: int, value: int) -> None:
        cache = self.cache
        node = Node(key, value)
        if key in cache:
            self.remove(cache[key])
        
        cache[key] = node

        self.insert(node)

        if len(cache) > self.capacity:
            node = self.lru.next
            self.remove(node)
            del cache[node.key]

    def remove(self, node):
        prv = node.prev
        nxt = node.next

        prv.next = nxt
        nxt.prev = prv
    
    def insert(self, node):
        mru = self.mru
        prv = mru.prev

        prv.next = node
        node.prev = prv

        mru.prev = node
        node.next = mru
        
