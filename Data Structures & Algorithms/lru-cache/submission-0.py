class Node:
    def __init__(self, key: int, val: int): # need key here so we can delete from the hasmap too
        self.key = key
        self.val = val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} # key -> Node()
        self.capacity = capacity

        self.lru = Node(0, 0)
        self.mru = Node(0, 0)

        self.lru.next = self.mru
        self.mru.prev = self.lru

    def insert(self, node: Node):
        last_node = self.mru.prev

        last_node.next = node
        node.prev = last_node

        node.next = self.mru
        self.mru.prev = node

    def remove(self, node: Node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])

            return self.cache[key].val
        return -1
        

    def put(self, key: int, value: int) -> None:
        capacity = self.capacity

        if key in self.cache:
            self.remove(self.cache[key])

        new_node = Node(key, value)
        self.cache[key] = new_node
        self.insert(new_node)

        if len(self.cache) > capacity:
            del self.cache[self.lru.next.key]
            self.remove(self.lru.next) # remove the LRU
        
