class CircularQuequ:

    class _Node:
        __slots__ = '_element','_next'
        def  __init__(self,element,next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._tail = None
        self._content = []
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def __str__(self):
        return str(self._content)
    
    def is_empty(self):
        return self._size == 0
    
    def first(self):
        if self.is_empty():
            raise Exception('CircularQueue is empty')
        return self._tail._next._element
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('CircularQueue is empty')
        oldhead = self._tail._next
        self._content.pop(0)
        if self._size == 1:
            self._tail = None
        else:
            self._tail._next = oldhead._next
        self._size -= 1
        return oldhead._element
    
    def enqueue(self,e):
        newest = self._Node(e,None)
        self._content.append(e)
        if self.is_empty():
            newest._next = newest
        else:
            newest._next = self._tail._next
            self._tail._next = newest
        self._tail = newest
        self._size += 1
    
    def rotate(self):
        if self._size > 0:
            self._tail = self._tail._next
            self._content = self._content[::-1]
            
if __name__ == "__main__":
    
    cq = CircularQuequ()
    cq.enqueue('hello')
    cq.enqueue('world')
    cq.enqueue("python")
    print(cq)
    cq.rotate()
    print(cq)
    cq.dequeue()
    print(cq)
                
