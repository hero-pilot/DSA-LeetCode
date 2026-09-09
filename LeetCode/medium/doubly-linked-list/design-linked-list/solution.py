class Node:
    def __init__(self, val=None, next = None, prev = None):
        self.val = val 
        self.next = next
        self.prev = prev

class MyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def get(self, index: int) -> int:
        if index >= self.length :
            return -1
        elif index== 0:
            return self.head.val
        elif index == self.length -1:
            return self.tail.val

        curr = self.head
        for i in range(index):
            curr = curr.next

        return curr.val


    def addAtHead(self, val: int) -> None:
        node = Node(val =val)
        if self.length == 0:  
            self.tail = node
            self.head = node
            
        else:
            self.head.prev = node
            node.next =self. head
            self.head = node
        self.length +=1

    def addAtTail(self, val: int) -> None:
        node = Node(val = val)
        if self.length == 0 :
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node
        self.length +=1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.length or index <0  :
            return 
        elif index == self.length :
            self.addAtTail(val)
        elif index == 0:
            self.addAtHead(val)
        else:
            node = Node(val = val)
            curr = self.head
            for _ in range(index):
                curr = curr.next
            before = curr.prev
            node.prev = before
            node.next = curr
            curr.prev = node
            before.next = node
            self.length +=1

    def deleteAtIndex(self, index: int) -> None:
        if index >= self.length :
            return
        if self.length == 1 and index == 0:
            self.tail = None
            self.head = None
            self.length -=1
            return
        elif index == self.length - 1:
            node = self.tail
            self.tail = node.prev
            self.tail.next = None
        elif index == 0 :
            self.head = self.head.next 
            self.head.prev = None
        else: 
            curr = self.head
            for _ in range(index):
                curr  = curr.next
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        self.length -=1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)