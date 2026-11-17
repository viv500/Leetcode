
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)

        self.lru.next = self.mru
        self.mru.prev = self.lru

        self.cache = {}
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        k = self.cache[key]

        self.remove(k)
        self.insert(k)

        return k.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        self.cache[key] = Node(key, value)

        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            to_remove = self.lru.next
            self.remove(to_remove)
            del self.cache[to_remove.key]

    def remove(self, node):
        p = node.prev
        n = node.next

        p.next = n
        n.prev = p

    def insert(self, node):
        m = self.mru
        p = m.prev

        p.next = node
        node.prev = p

        node.next = m
        m.prev = node

        
