from P7_2 import LinkedQueue

class Tree:

    class Position:
        '''
        抽象表示单个元素的位置
        '''
        #返回位置在P的元素
        def element(self):
            raise NotImplementedError('must be implemented by subclass')
        
        #判断其它对象和此对象位置是否相同
        def __eq__(self,other):
            raise NotImplementedError('must be implemented by subclass')
        
         #判断其它对象和此对象位置是否不相同
        def __ne__(self,other):
            return not(self == other)
    
    #返回树的根节点Position对象
    def root(self):
        raise NotImplementedError('must be implemented by subclass')
    
    #返回节点p的父节点(Position 对象)
    def parent(self,p):
        raise NotImplementedError('must be implemented by subclass')

    #返回位置为p的子节点的数目
    def num_children(self,p):
        raise NotImplementedError('must be implemented by subclass')

    #产生位置为p的子节点的一个迭代
    def children(self,p):
        raise NotImplementedError('must be implemented by subclass')
    
    #返回所有节点的数目
    def __len__(self):
        raise NotImplementedError('must be implemented by subclass')
    
    #判断是否为根节点
    def is_root(self,p):
        return self.root() == p
    
    #判断是否为叶子节点
    def is_leaf(self,p):
        return self.num_children(p) == 0
    
    #判断这个树是否为空
    def is_empty(self):
        return len(self) == 0
    
    #计算节点的深度
    def depth(self,p):
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))
    
    #计算一个节点的高度
    def _height2(self,p):
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    def height(self,p=None):
        if p is None:
            p =self.root
        return self._height2(p)
    
    #基于迭代树的所有位置的所有元素的迭代机制
    def __iter__(self):
        for p in self.positions():
            yield p

    #树的所有位置的迭代机制
    def positions(self):
        return self.preorder()

    #先序遍历
    '''
    Algorithm preorder(T,p):
        perform the "visit" action for position p
        for each child c in T.children(p) do
            preorder(T,c)
    '''
    def preorder(self):
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):
                yield p

    def _subtree_preorder(self,p):
        yield p
        for c in self.children(p):
            for other in self._subtree_preorder(c):
                yield other

    #后续遍历
    '''
    Algorithm postorder(T,p):
        for each child c in T.children(p) do
            postorder(T,c)
        perform the "visit" action for position p
    '''
    def postorder(self):
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self,p):
        for c in self.children(p):
            for other in self._subtree_postorder(c):
                yield other
        yield p
    
    #广度优先遍历
    '''
    Algorithm breadthfirst(T):
        Initialize queue Q to contains T.root()
        while Q not empty() do
            p = Q.dequeue()
            perform the "visit" action for position p 
            for each child c in T.childern(p):
                Q.enqueue(c)  

    '''
    def breadthfirst(self):
        if not self.is_empty():
            q = LinkedQueue()
            q.enqueue(self.root())
            while not q.is_empty():
                p = q.dequeue()
                yield p
                for c in self.children(p):
                    q.enqueue(c)
    

    
