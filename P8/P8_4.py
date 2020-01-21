#目录表
def preoder_indent(T,p,d):
    print(2*d*' ' + str(p.element()))
    for c in T.children(p):
        preoder_indent(T,c,d+1)

#目录表标签
def preoder_label(T,p,d,path):
    label = '.'.join(str(j+1) for j in path)
    print(2*d*' ' + label + ' ' + str(p.element()))
    path.append(0)
    for c in T.children(p):
        preoder_label(T,c,d+1,path)
        path[-1] += 1
    path.pop()

#输出树的附加说明字符串表示函数
def parenthesize(T,p):
    print(p.element(),end='')
    if not T.is_leaf(p):
        first_time = True
        for c in T.children(p):
            sep = ' (' if first_time else ', '
            print(sep,end='')
            first_time = False
            parenthesize(T,c)
        print(')',end='')


if __name__ == '__main__':
    
    from P8_3 import LinkedBinaryTree

    bt = LinkedBinaryTree()
    bt._add_root("怪诞行为学")
    bt._add_left(bt.root(),"金钱的诱惑")
    bt._add_left(bt.left(bt.root()),"激励的动机")
    bt._add_right(bt.left(bt.root()),"社会压力下的市场")
    bt._add_right(bt.root(),"工作的意义")
    preoder_indent(bt,bt.root(),0)
    print()
    path = []
    preoder_label(bt,bt.root(),0,path)
    print()
    parenthesize(bt,bt.root())
    print()
