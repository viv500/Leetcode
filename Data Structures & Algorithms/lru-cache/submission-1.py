class Node:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val

        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.lru = Node(0, 0)
        self.mru = Node(0, 0)
        self.capacity = capacity

        self.lru.next = self.mru
        self.mru.prev = self.lru

    def remove(self, node: Node):
        prev = node.prev
        nxt = node.next

        prev.next = nxt
        nxt.prev = prev

        node.next = None
        node.prev = None

    def insert(self, node: Node):
        mru = self.mru
        prev = mru.prev

        prev.next = node
        node.prev = prev

        node.next = mru
        mru.prev = node
        
        
    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        
        newNode = Node(key, value)
        self.insert(newNode)
        self.cache[key] = newNode

        if len(self.cache) > self.capacity:
            del self.cache[self.lru.next.key]
            self.remove(self.lru.next)


        
