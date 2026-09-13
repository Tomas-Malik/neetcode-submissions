class Node:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next, self.prev = None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.right.prev = self.left
        self.left.next = self.right
    
    def insert(self, node):
        prev = self.right.prev
        next = self.right
        node.next = next
        node.prev = prev
        prev.next = node
        self.right.prev = node

    def remove(self, node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

        

    def get(self, key: int) -> int:
        if key in self.cache:
            temp = self.cache[key]
            self.remove(temp)
            self.insert(temp)
            return temp.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        node = Node(key,value)
        
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(node)
            self.cache[key] = node
        else:
            self.cache[key] = node
            self.insert(node)
            self.cap -= 1
            if self.cap < 0:
                temp = self.left.next
                self.remove(temp)
                self.cache.pop(temp.key)
                # del temp








        
