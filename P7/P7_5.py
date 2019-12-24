from  P7_4 import _DoublyLinkedBase

class LinkedDequeue(_DoublyLinkedBase):

    def first(self):
        if self.is_empty():
            raise Exception('Dequeue is empty')
        return self._header._next._element

    def last(self):
        if self.is_empty():
            raise Exception('Dequeue is empty')
        return self._tail._prev._element
    
    def insert_first(self,e):
        self._insert_between(e,self._header,self._header._next)
    
    def insert_last(self,e):
        self._insert_between(e,self._tail._prev,self._tail)

    def delete_first(self):
        if self.is_empty():
            raise Exception('Dequeue is empty')
        element = self._delete_node(self._header._next)
        return element
    
    def delete_last(self):
        if self.is_empty():
            raise Exception('Dequeue is empty')
        element = self._delete_node(self._tail._prev)
        return element
    
if __name__ == "__main__":
    queue = LinkedDequeue()
    queue.insert_first("hello")
    queue.insert_last("world")
    print(queue.delete_last())