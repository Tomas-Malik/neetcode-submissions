class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.left = ListNode(0)
        

    def get(self, index: int) -> int:
        cur = self.left.next
        while cur and index > 0:
            cur = cur.next
            index -= 1
        if cur and index == 0:
            return cur.val
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        node, next = ListNode(val), self.left.next
        node.next = next
        self.left.next = node
        

    def addAtTail(self, val: int) -> None:
        cur = self.left.next
        node = ListNode(val)
        if not cur:
            self.left.next = node
            return
        prev = cur
        while cur:
            prev = cur
            cur = cur.next
        
        prev.next = node

        

    def addAtIndex(self, index: int, val: int) -> None:
        cur = self.left.next
        prev = self.left
        while cur and index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        if cur and index == 0:
            node, previous, next = ListNode(val), prev, cur
            previous.next = node
            node.next = cur
        elif prev and index == 0:
            node, previous = ListNode(val), prev
            previous.next = node

            


        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.left.next
        prev = self.left
        while cur and index > 0:
            prev = cur
            cur = cur.next
            index -= 1
        if cur and index == 0:
            previous, next = prev, cur.next
            previous.next = next
            
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)