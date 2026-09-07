class MinStack:

    def __init__(self):
        self.min_ele = []
        self.eles = []

        

    def push(self, val: int) -> None:
        self.eles.append(val)
        if self.min_ele:
            if val <= self.min_ele[-1]:
                self.min_ele.append(val)    
        else:
            self.min_ele.append(val)
        

    def pop(self) -> None:
        if self.eles[-1] == self.min_ele[-1]:
            self.min_ele.pop()
        self.eles.pop()

    def top(self) -> int:
        return self.eles[-1]

    def getMin(self) -> int:
        return self.min_ele[-1]
        
