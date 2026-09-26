class BrowserHistory:
    def __init__(self, homepage: str):
        self.curr = 0
        self.len = 1
        self.hist = [homepage]

    def visit(self, url: str) -> None:
        if len(self.hist) < self.curr +2:
            self.hist.append(url)
        else:
            self.hist[self.curr +1] = url
        
        self.curr +=1
        self.len = self.curr +1

    def back(self, steps: int) -> str:
        self.curr = max(self.curr - steps ,0)
        return self.hist[self.curr]
        

    def forward(self, steps: int) -> str:
        self.curr = min(self.curr + steps , self.len - 1)
        return self.hist[self.curr]

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)