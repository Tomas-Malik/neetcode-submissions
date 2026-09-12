class Node:

    def __init__(self,key,val):
        self.key, self.val = key, val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.capacity = capacity

        self.left, self.right = Node(0,0),Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left

    def insert(self, node):
        temp = self.right.prev
        temp.next = node
        self.right.prev = node
        node.prev = temp
        node.next = self.right
        



    def remove(self, node):
        l = node.prev
        r = node.next
        l.next = r
        r.prev = l
            
            

    def get(self, key: int) -> int:
        
        if key in self.cache:
            temp = self.cache[key]
            self.remove(self.cache[key])
            self.insert(temp)
            
            return temp.val
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        node = Node(key, value)

        

        if key not in self.cache:
            self.cache[key] = node
            self.insert(node)
            self.capacity = self.capacity - 1
            if self.capacity < 0:
                node = self.left.next
                self.cache.pop(node.key)
                self.remove(node)
        else:
            self.remove(self.cache[key])
            self.insert(node)
            self.cache[key] = node
        
        
        




        


        
            
        
        
