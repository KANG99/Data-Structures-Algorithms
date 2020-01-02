from P8_2 import BinaryTree

class LinkedBinaryTree(BinaryTree):

    class _Node:

        __slots__ = '_element','_parent','_left','_right'
        def __init__(self,element,parent=None,left=None,right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right
        
    class Position(BinaryTree.Position):
        def __init__(self,container,node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node

        

