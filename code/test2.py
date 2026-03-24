class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class Dll:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length =1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp)
            temp = temp.next
        
    def append(self, value):
        node = Node(value)
        if self.length == 0:
            self.head= node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail= node
        self.length +=1

    def preppend(self,value):
        node = Node(value)
        if self.length == 0:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            self.head.prev = node
            self.head = node
        self.length +=1 
    
    def pop(self):
        if self.length == 0:
            return None
        elif self.length ==1:
            temp = self.head 
            self.head = None
            self.tail =None
            self.length -=1
            return temp
        temp = self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev =None
        self.length -=1
        return temp
    
    def pop_first(self):
        if self.length ==0 or self.length == 1:
            return self.pop()
        temp = self.head
        self.head = self.head.next
        self.head.prev = None
        temp.next =None
        self.length -=1
        return temp
    
    def get(self,index):
        if index< 0 or index >= self.length :
            return None
        temp = self.head

        for _ in range(self.length):
            temp = temp.next
        return temp
    
    def set_value(self, value , index):
        node = self.get(index)
        if node is not None:
            node.value = value
            return True
        return False
    
    def insert(self, value, index):
        if index <0 or index > self.length:
            return None
        elif index == self.length:
            return self.append(value)
        elif index== 0:
            return self.preppend(value)
        node = Node(value)
        after = self.get(index)
        before= temp.prev 
        node.next = after
        node.prev = before
        after.prev= node
        before.next = node
        self.length +=1
    

    def remove(self, index):
        if index == 0:
            return self.pop_first()
        elif index == self.length-1 :
            return self.pop()
        node = self.get(index)
        if node is not None:
            before = node.prev 
            after = node.next 
            before.next = after 
            after.prev = before 
            node.next = None
            node.before = None 
            self.length -=1
            return node
        return None
        

        