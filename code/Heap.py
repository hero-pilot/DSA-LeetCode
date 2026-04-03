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
    
    def _sink_down(self,indeX):
        left_child= self._left_child(indeX)
        right_child = self._right_child(index)
        max_index = indeX
        while True:
            if len(self._left_child) < len(self.heap) and self.heap[max_index] < self.heap[left_child] :
                max_index = left_child
                
            if len(self._right_child) < len(self.heap) and self.heap[max_index] < self.heap[right_child]:
                max_index = right_child
            
            
            if max_index !=indeX:
                self._swap(max_index, indeX)
                index = max_index
            else:
                return
    def insert(self,value):
        self.heap.append(value)
        index = len(self.heap)  - 1
        parent_index = self._parent(index)
        while index >0 and self.heap[index] > self.heap[parent_index]:
            self._swap(index, parent_index)
            index = self._parent(index)
            parent_index = self._parent(index)
    
    def remove(self):
        if len(self.heap) == 0:
            return None
        elif len(self.heap) == 1:
            return self.heap.pop()
        temp = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return temp