class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    

class Bst:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        node = Node(value)
        if self.root is None:
            self.root= node
        else:
            temp = self.root
            while temp is not None:
                if temp.value == node.value:
                    return False
                if node.value > temp.value:
                    if temp.right is None:
                        temp.right = node
                    temp = temp.right
                else:
                    if temp.left is None:
                        temp.left = node
                    temp = temp.left
        
    def contains(self, value):
        temp = self.root
        while temp is not None:
            if temp.value == value: 
                return True
            elif value > temp.value :
                temp = temp.right
            else:
                temp = temp.left
        return False
                


bst = Bst()
bst.insert(29)
bst.insert(24)
bst.insert(30)

print(bst.contains(29))
