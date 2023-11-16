from sys import getsizeof
from pickle import dumps ,loads
global b
global tnum
global tnom
global tprnom
b=0
tnum = 10
tnom = 20
tprenom = 20
Tetud = tnum + tnom + tprenom + 1
teng = '#' * Tetud
Tbloc = [0,[teng]*b]
blocsize = getsizeof(dumps(Tbloc))+len(teng)*(b-1)+(b-1)
print(blocsize)
def ecrireDir (F,i,buf):
    dp=2*getsizeof(dumps(0))+i*getsize
    P.seek(dp)
    f.write(dumps(buf))
    load(buf)