class Node:
    def __init__(self, key=0, val=0, prev=None, next=None):
        self.key = key
        self.val = val
        self.prev = prev
        self.next = next

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity

        self.lru = Node()
        self.mru = Node()

        self.lru.next = self.mru
        self.mru.prev = self.lru

        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        else: return -1

        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)     

        if len(self.cache) > self.capacity:
            to_remove = self.lru.next
            del self.cache[to_remove.key]
            self.remove(to_remove)

    
    def insert(self, node):
        prv = self.mru.prev

        prv.next = node
        node.prev = prv

        node.next = self.mru
        self.mru.prev = node

    def remove(self, node):
        prv, nxt = node.prev, node.next

        prv.next = nxt
        nxt.prev = prv
        
  
        
