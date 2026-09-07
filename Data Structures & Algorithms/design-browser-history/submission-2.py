class ListNode:

    def __init__(self,s):
        self.val = s
        self.next = None
        self.prev = None

class BrowserHistory:

    def __init__(self, homepage: str):
        self.left = ListNode("left")
        self.right = ListNode("right")

        self.homepage = ListNode(homepage)
        self.left.next = self.homepage
        self.right.prev= self.homepage
        self.homepage.prev = self.left
        self.homepage.next = self.right
        self.pt = self.homepage

        

    def visit(self, url: str) -> None:
        node, prev, next = ListNode(url), self.pt, self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next
        self.pt = node

        

    def back(self, steps: int) -> str:
        cur = self.pt
        while cur and steps > 0:
            cur = cur.prev
            
            steps -=1
        if not cur or cur == self.left:
            cur = self.left.next
        self.pt = cur
        return cur.val


        

    def forward(self, steps: int) -> str:
        cur = self.pt
        while cur and steps > 0:
            cur = cur.next
            steps -= 1
        if not cur or cur == self.right:
            cur = self.right.prev
        self.pt = cur
        return cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)