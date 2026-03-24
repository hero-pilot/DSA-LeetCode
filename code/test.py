class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None


class Bst:
    def __init__(self, value):
        self.root = Node(value)
        
    
    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root = None
        temp = self.root
        while temp is not None:
            if node.value > temp.value:
                temp = temp.right
            elif node.value < temp.value:
                temp = temp.left
        temp = node
    
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if temp.value == value:
                return True
            elif temp.value > value:
                temp = temp.right
            else:
                temp = temp.left
        return False