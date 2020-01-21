from P8_3 import LinkedBinaryTree

#表达树
class ExpressionTree(LinkedBinaryTree):
    def __init__(self,token,left=None,right=None):
        super().__init__()
        if not isinstance(token,str):
            raise TypeError('Token must be a string')
        self._add_root(token)
        if left is not None:
            if token not in '+-*x/':
                raise ValueError('Token must be valid operator')
            self._attach(self.root(),left,right)
    
    def __str__(self):
        pieces = []
        self._parenthesize_recur(self.root(),pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self,p,result):
        if self.is_leaf(p):
            result.append(str(p.element()))
        else:
            result.append('(')
            self._parenthesize_recur(self.left(p),result)
            result.append(p.element())
            self._parenthesize_recur(self.right(p),result)
            result.append(')')

#表达树的评估
'''
Algorithmn evaluate_recur(p):
    if p is a leaf then
        return the value stored at p
    else 
        let o be the operator stored at p 
        x = evaluate_recur(left(p))
        y = evaluate_recur(right(p))
        return x o y

'''