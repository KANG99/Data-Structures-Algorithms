class LinkedQueue:

    class _Node:
        __slots__ = '_element','_next'
        def  __init__(self,element,next):
            self._element = element
            self._next = next  

    def  __init__(self):
        self._head = None
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
            raise Exception("Queue is empty")
        return self._head._element
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        answer = self._head._element
        self._content.pop(0)
        self._size -= 1
        if self.is_empty():
            self._tail =  None
        self._head = self._head._next
        return answer
    
    def enqueue(self,e):
        newest = self._Node(e,None)
        self._content.append(e)
        if self.is_empty():
            self._head = newest
        else:
            self._tail._next =  newest
        self._tail = newest
        self._size += 1


if __name__ == "__main__":

    queue = LinkedQueue()
    queue.enqueue("hello")
    queue.enqueue("world")
    print(queue)
    print(queue.dequeue())
    print(queue)
