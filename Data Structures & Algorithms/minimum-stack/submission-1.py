class MinStack:

    stack = None
    minstack = None
    length = 0

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.length = 0

    def push(self, val: int) -> None:
        if self.length == 0:
            self.stack.append(val)
            self.minstack.append(val)
        else:
            if self.minstack[-1] > val:
                self.stack.append(val)
                self.minstack.append(val)
            else:
                self.stack.append(val)
                self.minstack.append(self.minstack[-1])
        self.length += 1
                    

    def pop(self) -> None:
        if len(self.stack) == 0:
            return
        self.stack.pop()
        self.minstack.pop()
        self.length -= 1
    
    def top(self) -> int:
        if len(self.stack) == 0:
            return
        return self.stack[-1]
        

    def getMin(self) -> int:
        if len(self.minstack) == 0:
            return
        return self.minstack[-1]
        
