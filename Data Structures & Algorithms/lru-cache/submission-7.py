class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)

        self.lru.next = self.mru
        self.mru.prev = self.lru


    def get(self, key: int) -> int:
        cache = self.cache

        if key not in cache: return -1

        node = cache[key]
        self.remove(node)
        self.insert(node)

        return node.val
        

    def put(self, key: int, value: int) -> None:
        cache = self.cache

        if key in cache:
            node = cache[key]
            self.remove(node)

        node = Node(key, value)
        cache[key] = node
        self.insert(node)

        if len(cache) > self.capacity:
            node = self.lru.next
            self.remove(node)
            del cache[node.key]

    def remove(self, node):
        p, n = node.prev, node.next

        p.next = n
        n.prev = p
    
    def insert(self, node):
        mru = self.mru
        p = mru.prev

        p.next = node
        node.prev = p

        node.next = mru
        mru.prev = node
        
