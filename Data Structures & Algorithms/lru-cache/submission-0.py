class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):

        self.cache = {}
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def insert(self, node):
        previous = self.tail.prev
        nxt = self.tail

        previous.next = nxt.prev = node
        node.next = nxt
        node.prev = previous
    
    def remove(self, node):
        previous = node.prev
        nxt = node.next
        previous.next = nxt
        nxt.prev = previous
    
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del self.cache[lru.key]
