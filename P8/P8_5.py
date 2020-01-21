class EulerTour:

    def __init__(self,tree):
        self._tree = tree
    
    def tree(self):
        return self._tree

    def excute(self):
        if len(self._tree) > 0:
            return self._tutor(self._tree.root(),0,[])
    
    def _tutor(self,p,d,path):
        self._hook_previsit(p,d,path)
        results = []
        path.append(0)
        for c in self._tree.children(p):
            results.append(self._tutor(c,d+1,path))
            path[-1] += 1
        path.pop()
        answer = self._hook_postvisit(p,d,path,results)
        return answer

    def _hook_previsit(self,p,d,path):
        pass

    def _hook_postvisit(self,p,d,path,results):
        pass

class PreorderPrintIndentedTour(EulerTour):
    def _hook_previsit(self,p,d,path):
        print(2*d*' '+str(p.element()))

class PreorderPrintIndentedLabeledTour(EulerTour):
    def _hook_previsit(self,p,d,path):
        label = '.'.join(str(j+1) for j in path)
        print(2*d*' '+label,p.element())

class ParenthesizeTour(EulerTour):
    def _hook_previsit(self,p,d,path):
        if path and path[-1]>0:
            print(', ',end='')
        print(p.element(),end='')
        if not self.tree().is_leaf(p):
            print(' (',end='')

    def _hook_postvisit(self,p,d,path,results):
        if not self.tree().is_leaf(p):
            print(')',end='')

class DiskSpaceTour():
    def _hook_postvisit(self,p,d,path,results):
        return p.element().space()+sum(results)


class BinaryEulerTour(EulerTour):
    def _tutor(self,p,d,path):
        results = [None,None]
        self._hook_previsit(p,d,path)
        if self._tree.left(p) is not None:
            path.append(0)
            results[0] = self._tutor(self._tree.left(p),d+1,path)
            path.pop()
        self._hook_invisit(p,d,path)
        if self._tree.right(p) is not None:
            path.append(1)
            results[1] = self._tutor(self._tree.right(p),d+1,path)
            path.pop()
        answer = self._hook_postvisit(p,d,path,results)
        return answer
        

class BianryLayout(BinaryEulerTour):
    def __init__(self,tree):
        super().__init__(tree)
        self._count = 0
    
    def _hook_invisit(self,p,d,path):
        p.element().setX(self.count)
        p.element().setY(d)
        self._count += 1

if __name__ == "__main__":

    from P8_3 import LinkedBinaryTree

    # bt = LinkedBinaryTree()
    # bt._add_root("怪诞行为学")
    # bt._add_left(bt.root(),"金钱的诱惑")
    # bt._add_left(bt.left(bt.root()),"激励的动机")
    # bt._add_right(bt.left(bt.root()),"社会压力下的市场")
    # bt._add_right(bt.root(),"工作的意义")
    class TreeFactory:

        def __init__(self):
            self._tree = LinkedBinaryTree()
            self._node = None
            

        def excute(self,e,d=None,p=None):
            if self._tree.is_empty():
                self._tree._add_root(e)
                self._node = self._tree.root()
            elif d == 'left':
                self._tree._add_left(p,e)
                self._node =self._tree.left(p)
            elif d == 'right':
                self._tree._add_right(p,e)
                self._node =self._tree.right(p)
            return self._tree,self._node

    bt = TreeFactory()
    _,root = bt.excute("怪诞行为学")
    _,left_1 = bt.excute("金钱的诱惑",'left',root)
    _,left_2 = bt.excute("激励的动机",'left',left_1)
    _,right_2 = bt.excute("社会压力下的市场",'right',left_1)
    tree,right_1 = bt.excute("工作的意义",'right',root)
    path = []
    ppt = PreorderPrintIndentedTour(tree)
    ppt.excute()
    print()
    pptl = PreorderPrintIndentedLabeledTour(tree)
    pptl.excute()
    print()
    pt = ParenthesizeTour(tree)
    pt.excute()
