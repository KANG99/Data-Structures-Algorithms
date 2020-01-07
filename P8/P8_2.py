from P8_1 import Tree

class BinaryTree(Tree):

    #获得左孩子
    def left(self,p):
        raise NotImplementedError('must be implemented by subclass')
    
    #获得右孩子
    def right(self,p):
        raise NotImplementedError('must be implemented by subclass')
    
    #获得兄弟节点
    def sibling(self,p):
        parent = self.parent(p)
        if parent is None:
            return None
        else:
            if p == self.left(parent):
                return self.right(parent)
            else:
                return self.left(parent)
    
    #获得子节点的迭代
    def children(self,p):
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)
    
    #中序遍历二叉树
    '''
    Algorithm inorder:
        if p has a left child lc then
            inorder(lc)
        perform the "visit" action for position p
        if p has a right child rc then
            inorder(rc)
    '''
    def inorder(self):
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p
    
    def _subtree_inorder(self,p):
        if self.left(p) is not None:
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):
                yield other
    
    def positions(self):
        return self.inorder()
