class Node:
    def __init__(self, key, val, prev=None, nxt=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.nxt = nxt

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.mru = Node(0, 0)
        self.lru = Node(0, 0)

        self.lru.nxt = self.mru
        self.mru.prev = self.lru
        

    def get(self, key: int) -> int:
        cache = self.cache
        if key in cache:
            node = cache[key]
            self.remove(node)
            self.insert_end(node)
            return node.val
        else: return -1
       
        
    def put(self, key: int, value: int) -> None:
        cache, capacity = self.cache, self.capacity

        if key not in cache:
            cache[key] = Node(key, value)
            self.insert_end(cache[key])
        else:
            node = cache[key]
            self.remove(node)
            self.insert_end(node)
            node.val = value

        if len(cache) > capacity:
            least_recent = self.lru.nxt
            self.remove(least_recent)

            del cache[least_recent.key]

    def insert_end(self, node):
        mru = self.mru
        last = mru.prev

        last.nxt = node
        node.prev = last

        node.nxt = mru
        mru.prev = node

    def remove(self, node):
        prev, nxt = node.prev, node.nxt

        prev.nxt = nxt
        nxt.prev = prev


        
