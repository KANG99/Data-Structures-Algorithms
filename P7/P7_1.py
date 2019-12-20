class  LinkedStack:
    
    class _Node:
        __slots__ = '_element','_next'
        def  __init__(self,element,next):
            self._element = element
            self._next = next
    
    def __init__(self):
        self._head = None
        self._content = []
        self._size = 0
        

    def __len__(self):
        return self._size

    def  is_empty(self):
        return self._size == 0

    def push(self,e):
        self._head =  self._Node(e,self._head)
        self._content.append(e)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise Exception('Stack is empty')
        answer =  self._head._element
        self._head = self._head._next
        self._content.pop()
        self._size -= 1
        return answer

    def __str__(self):
        return str(self._content)

if __name__ == "__main__":

    stack =  LinkedStack()
    stack.push('hello')
    stack.push("world")
    print(stack)
    print(len(stack))
    stack.pop()
    print(stack)
    print(len(stack))
 

