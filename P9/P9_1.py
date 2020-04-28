
class _DoublyLinkedBase:

    class _Node:
        __slots__ = '_element','_prev','_next'
        def  __init__(self,element,prev,next):
            self._element = element
            self._prev = prev
            self._next = next
    
    def __init__(self):
        self._header = self._Node(None,None,None)
        self._tail = self._Node(None,None,None)
        self._header._next = self._tail
        self._tail._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size
    
    def is_empty(self):
        return self._size == 0
    
    def _insert_between(self,e,predecessor,successor):
        newest = self._Node(e,predecessor,successor)
        predecessor._next = newest
        successor._prev = newest
        self._size += 1
        return newest
    
    def _delete_node(self,node):
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element
        node._element=node._prev=node._next = None
        return element


class PositionalList(_DoublyLinkedBase):
    '''
    拥有_header,_tail,_element,_size属性
    '''
    
    class Position:

        def __init__(self,container,node):
            self._container = container
            self._node = node
        
        def element(self):
            return self._node._element
        
        def __eq__(self,other):
            return type(other) is type(self) and other._node is self._node
        
        def __ne__(self,other):
            return not(self == other)
        
    def _validate(self,p):
        '''
        无效元素
        １、不属于Position类型
        ２、该元素指向的位置被占用
        ３、该元素无后继节点
        '''
        if not isinstance(p,self.Position):
            raise TypeError('p must be proper Position type')
        if p._container is not self:
            raise ValueError('p does not blong to this container')
        if p._node._next is None:
            raise ValueError('p is no longer valid')
        return p._node
    
    def _make_position(self,node):
        if node is self._header or node is self._tail:
            return None
        else:
            return self.Position(self,node)
        
    def first(self):
        return self._make_position(self._header._next)
    
    def last(self):
        return self._make_position(self._tail._prev)

    def before(self,p):
        node = self._validate(p)
        return self._make_position(node._prev)
    
    def after(self,p):
        node = self._validate(p)
        return self._make_position(node._next)
    
    def __iter__(self):
        cusor = self.first()
        #print(cusor)
        while cusor is not None:
            yield cusor.element()
            cusor = self.after(cusor)
        
    def _insert_between(self,e,predecessor,successor):
        node = super()._insert_between(e,predecessor,successor)
        return self._make_position(node)
    
    def add_first(self,e):
        return self._insert_between(e,self._header,self._header._next)

    def add_last(self,e):
        return self._insert_between(e,self._tail._prev,self._tail)
    
    def add_before(self,p,e):
        original = self._validate(p)
        return self._insert_between(e,original._prev,original)
    
    def add_afert(self,p,e):
        original = self._validate(p)
        return self._insert_between(e,original,original._next)

    def delete(self,p):
        original = self._validate(p)
        return self._delete_node(original)

    def replace(self,p,e):
        original =  self._validate(p)
        old_element = original._element
        original._element = e
        return old_element
        
def insert_sort(L):
    if len(L) > 1:
        marker = L.first()
        while marker != L.last():
            pivot = L.after(marker)
            value = pivot.element()
            if value > marker.element():
                marker = pivot
            else:
                walk = marker
                while walk != L.first() and L.before(walk) > value:
                    walk = L.before(walk)
                L.delete(pivot)
                L.add_before(walk,value)


class PriorityQueueBase:

	class _item:

		__slots__ = '_key','_value'

		def __init__(self,key,value):
			self._key = key
			self._value = value

		def __it__(self,other):
			return self._key < other._key

	def is_empty(self):
		return len(self) == 0


class UnsortedPriorityQueue(PriorityQueueBase):

	def _find_min(self):
		if self.is_empty():
			raise Exception('Priority queue is empty ')
		small = self._data.first()
		walk = self._data.after(small)
		while walk is not None:
			if small.element < walk.element():
				small = walk
			walk = self._data.after(walk)
		return small

	def __init__(self):
		self._data = PositionalList()

	def __len__(self):
		return len(self._data)


	def add(self,key,value):
		self._data.add_last(self._item(key,value))

	def min(self):
		p = self._find_min()
		item = p.element()
		return item._key,item._value

	def remove_min(self):
		 p = self._find_min()
		 item = self._data.delete(p)
		 return item._key,item._value


class SortedProtityQueue(PriorityQueueBase):

	def __init__(self):
		self._data = PositionalList()

	def len(self):
		return len(self._data)


	def add(self,key,value):
		newest = self._item(key,value)
		walk = self._data.last()
		while walk is not None and newest < walk.element():
			walk = self._data.before(walk)

		if walk is None:
			self._data.add(newest)
		else:
			self._data.add_afert(walk)

	def min(self):
		if self.is_empty():
			raise Exception('Priority queue is empty')
		p = self._data.first()
		item = p.element()
		return item._key,item._value

	def remove_min(self):
		if self.is_empty():
			raise Exception('Priority queue is empty')
		item = self._data.delete(self._data.first())
		return item._key,item._value


class HeapPriorityQueue(PriorityQueueBase):

	def _parent(self,j):
		return (j-1)//2

	def _left(self,j):
		return 2*j+1

	def _right(self,j):
		return 2*(j+1)

	def _has_left(self,j):
		return self._left(j) < len(self._data)

	def _has_right(self.j):
		return self._right(j) < len(self._data)

	def _swap(self,i,j):
		self._data[i],self._data[j] = self._data[j],self._data[i]

	def _upheap(self,j):
		parent = self._parent(j)
		if j>0 and self._data[j] < self._data[parent]:
			self._swap(j,parent)
			self._upheap(parent)

	def _downheap(self,j):

		if self._has_left(j):
			left = self._left(j)
			small_child = left
			if self._has_right(j):
				right = self._right(j)
				if self._data[right]<self._data[left]:
					small_child = right
				if self._data[small_child]<self._data[j]:
					self._swap(j,small_child)
					self._downheap(small_child)

	def __init__(self):
		self._data = []

	'''
	#自底向上构建
	def __init(self,contents = ()):
		self._data = [self._item(k,v) for k,v in contents]
		if len(self._data) > 1:
			self._heapify()

	def _heapify(self):
		start = self._parent(len(self)-1)
		for j in range(start,-1,-1):
			self._downheap(j)
	'''

	def __len__(self):
		return len(self._data)

	def add(self,key,value):
		self._data.append(self._item(key,value))
		self._upheap(len(self._data)-1)

	def min(self):
		if self.is_empty():
			raise Exception('Priority queue is empty')
		return self._data[0]

	def remove_min(self):
		if self.is_empty():
			raise Exception('Priority queue is empty')
		self._swap(0,len(self._data)-1)
		item = self._data.pop()
		self._downheap(0)
		return item._key,item._value

class AdaptablePriorityQueue(HeapPriorityQueue):

	class Locator(HeapPriorityQueue._item):

		__slots__ = 'index'

		def __init__(self,k,v,j):
			super().__init__(k,v)
			self._index = j

	def  _swap(self,i,j):
		super._swap(i,j)
		self._data[i]._index = i
		self._data[j]._index = j

	def _bubble(self,j):
		if j>0 and self._data[j]<self._data[self._parent(j)]:
			self._upheap(j)
		else:
			self._downheap(j)

	def add(self,key,value):
		token = self.Locator(key,value,len(self._data))
		self._data.append(token)
		self._upheap(len(self._data)-1)
		return token

	def update(self,loc,newkey,newval):
		j = loc._index
		if not (0<=j<len(self)) and self._data[j] is loc:
			raise ValueError('Invalid locator')
		loc._key = newkey
		loc._value = newval
		self._bubble(j)

	def remove(self,loc):
		j = loc.index
		if not (0<=j<len(self)) and self._data[j] is loc:
			raise ValueError('Invalid locator')
		if j==len(self)-1:
			self._data.pop()
		else:
			self._swap(j,len(self)-1)
			self._data.pop()
			self._bubble(j)
		return loc._key,loc.value





		


		






