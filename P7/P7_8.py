from P7_7 import FavoritesList
from P7_7 import PositionalList

class FavoritesListMTF(FavoritesList):

    def _move_up(self,p):
        if p != self._data.first():
            self._data.add_first(self._data.delete(p))

    def top(self,k):
        if not 1<= k <= len(self):
            raise ValueError('Illegal value for k')
        temp = PositionalList()
        for item in self._data:
            temp.add_last(item)
            #print(item._value)
            #print(type(item))
            #print(item.element())

            
        for j in range(k):
            highPos = temp.first()
            #print(type(highPos.element()))
            walk = temp.after(highPos)
            while walk is not None:
                #print(walk.element()._count,highPos.element()._count)
                if walk.element()._count > highPos.element()._count:
                    #print(walk.element()._count,highPos.element()._count)
                    highPos = walk
                walk = temp.after(walk)
            #print(type(highPos.element()))
            yield highPos.element()._value
            temp.delete(highPos)

if __name__ == '__main__':
    print('welcome to python world!\n'.upper())
    flm = FavoritesListMTF()
    flm.access('python')
    flm.access('sql')
    flm.access('python')
    flm.access('html')
    flm.access('python')
    flm.access('git')
    flm.access('python')
    flm.access('java')
    flm.access('git')
    flm.access('java')
    flm.access('git')
    flm.access('python')
    for i in flm.top(3):
        print(i)
    
