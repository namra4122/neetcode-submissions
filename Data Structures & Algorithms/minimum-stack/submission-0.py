class MinStack:

    def __init__(self):
        self.st = []

    def push(self, val: int) -> None:
        curr_min = self.st[-1][1] if self.st else None
        if curr_min is None or curr_min > val:
            curr_min = val
        
        self.st.append([val, curr_min])

    def pop(self) -> None:
        self.st.pop()
        

    def top(self) -> int:
        return self.st[-1][0] if self.st else None

    def getMin(self) -> int:
        return self.st[-1][1] if self.st else None
        
