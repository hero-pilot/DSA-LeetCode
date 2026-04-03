class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def _left_child(self, parent_index):
        return 2 * parent_index +1
    
    def _right_child(self, parent_index):
        return 2 * parent_index +2
    
    def _parent(self, child_index):
        return int((child_index-1) /2)
    
    def _swap(self, index1, index2):
        self.heap[index1] , self.head[index2] = self.heap[index2] , self.heap[index1]
    
    def insert(self,value):
        self.heap.append(value)
        index = len(self.heap)  - 1
        parent_index = self._parent(index)
        while index >0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            index = self._parent(index)
            parent_index = self._parent(index)