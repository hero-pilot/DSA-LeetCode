class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node
        self.tail = node
        self.length = 1
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        node = Node(value)
        if self.length == 0 :
            self.head = node
            self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            node.next = None
            self.tail = node
        self.length +=1
    def pop(self):
        if self.length ==0 : return None
        elif self.length ==1 :
            temp = self.head
            self.head= None
            self.tail = None
            self.length -=1
            return temp
        temp= self.tail
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -=1
        return temp
    
    def prepend(self, value):
        node = Node(value)
        if self.length ==0 :
            self.head = node
            self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
        self.length +=1
    def pop_first(self):
        if self.length == 0: return None
        elif self.length ==1:
            return self.pop()
        temp = self.head 
        self.head = self.head.next
        self.head.prev = None
        self.length -=1 
        temp.next = None
        return temp
    
    def get(self, index):
        if index <0 or index >= self.length:
            return None
        temp = self.head
        if index < self.length / 2:
            for _ in range(index):
                temp = temp.next
        else: 
            temp = self.tail
            for _ in range(self.length - 1 , index , -1):
                temp = temp.prev
        return temp

    def set_value(self, index, value):
        node = self.get(index)
        if node is not None:
            node.value = value
        else:
            return None
    
    def insert(self, value, index):
        if index <0 or index > self.length :
            return None
        elif index == self.length:
            self.append(value)
        elif index== 0 :
            self.prepend(value)
        else:
            node = Node(value)
            curr = self.get(index)
            before = curr.prev
            node.prev = before
            node.next = curr
            before.next = node
            curr.prev = node
            self.length +=1

    def remove(self, index):
        node = self.get(index)
        if node is not None:
            before = node.prev
            after = node.next
            before.next = after
            after.prev = before
            node.next = None
            node.prev = None
            self.length -=1
            return node
        return None
myl = DoublyLinkedList(1)
myl.append(2)
myl.append(3)
myl.append(4)

print(myl.remove(2).value)
myl.print_list()
print(myl.get(0).value)