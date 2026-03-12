class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        self.top = Node(value)
        self.height = 1
    
    def print_stack(self):
        temp = self.top 
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self.height +=1
    
    def pop(self ):
        if self.height ==0:
            return None
        node = self.top
        self.top = self.top.next
        node.next = None
        self.height -=1
        return node

mys = Stack(2)
mys.push(1)
mys.print_stack()

mys.pop()
mys.print_stack()