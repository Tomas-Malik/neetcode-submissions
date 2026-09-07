class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.append(0)
        l = len(self.stack)
        
        temp1 = self.stack[0]
        for i in range(l-1):
            y = self.stack[i+1]
            self.stack[i+1] = temp1
            temp1 = y
        self.stack[0] = x


            
        

            
        

    def pop(self) -> int:
        if not self.empty():
            return self.stack.pop(0) 
        

    def top(self) -> int:
        if not self.empty():
            return self.stack[0]
        

    def empty(self) -> bool:
        if len(self.stack) == 0:
            return True
        else:
            return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()