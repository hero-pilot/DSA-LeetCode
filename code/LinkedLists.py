class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        node= Node(value)
        self.head= node
        self.tail = node 
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def empty(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node
        self.length +=1
    def pop(self):
        if self.length ==0: return None
        elif self.length ==1 :
            temp = self.head
            self.head = None
            self.tail = None
            self.length -=1
            return temp
        temp =self.head
        while temp.next is not None:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -=1
        return temp
    
    def prepend(self,value):
        node = Node(value)
        if self.length == 0:
            self.append(value)
        else:
            node.next = self.head
            self.head = node
            self.length +=1
    
    def pop_first(self):
        if self.length ==0 or self.length ==1 :
            return self.pop()
        
        temp =self.head
        self.head = self.head.next
        temp.next =None
        self.length -=1
        return temp
    
    def get(self, index):
        if index <0 or index >= self.length :
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, value, index):
        node = self.get(index)
        if node is not None:
            node.value = value
        else:
            return None
    
    def insert(self, value, index):
        if index <0 or index > self.length:
            return None
        elif index == 0:
            self.prepend(value)
        elif index == self.length:
            self.append(value)
        else:
            node = Node(value)
            before= self.get(index - 1)
            node.next = before.next
            before.next = node
            self.length +=1
            return node
    def remove(self, index):
        if index<0 or index >= self.length :
            return None
        elif index ==0:
            return self.pop_first()
        elif index == self.length -1:
            return self.pop()
        before = self.get(index - 1)
        temp = before.next 
        before.next =  temp.next 
        self.length -=1
        temp.next = None
        return temp

    def reverse(self):
        if self.length ==0 or self.length == 1:
            return None
        temp = self.head
        before = None
        for _ in range(self.length):
            after = temp.next
            temp.next =  before
            before = temp 
            temp = after
        temp = self.head 
        self.head = self.tail
        self.tail = temp        

        
        
        
        
    
    