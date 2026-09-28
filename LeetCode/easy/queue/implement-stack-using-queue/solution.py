class MyStack:

    def __init__(self):
        self.q = deque()
        

    def push(self, x: int) -> None:
        self.q.append(x)
        

    def pop(self) -> int:
        for i in range(len(self.q) -1):
            self.q.append(self.q.popleft())
        return self.q.popleft()

    def top(self) -> int:
        for i in range(len(self.q) -1):
                self.q.append(self.q.popleft())
            
        lol = self.q.popleft()
        self.q.append(lol)
        return lol

    def empty(self) -> bool:
        return False if self.q else True