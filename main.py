import itertools

import setting as s
from fkt import insrt

start=(1,0,1,0,0,0)
lst=list(itertools.product([0,1], repeat=6))
core=list(itertools.product([0,1],repeat=5))
wt0=insrt(core,0)
wt1=insrt(core,1)

#s.alla(lst)
#s.alls(lst)
#s.traa(start)
#s.tras(start)