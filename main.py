import itertools
import networkx as nx
import setting as s
from fkt import insrt
import network

##model: S,N,I,K1,K2,A

#start=(1,0,1,0,0,0)

lst=list(itertools.product([0,1], repeat=6))
#core=list(itertools.product([0,1],repeat=5))
#wt0=insrt(core,0)
#wt1=insrt(core,1)

##Delay of each component in time steps; for activation and inactivation
#delay=((0,0),(0,0),(0,0),(0,0),(0,0),(0,1))
pc1=((1,1),(2,2),(5,4),(3,3),(3,3),(5,6))
#pc2=((1,1),(1,1),(1,2),(1,1),(1,1),(1,3))


#s.alla(lst)
#s.alls(lst)
#s.traa(start)
#s.tras(start)
#s.td(start,delay)
#s.pct(start,pc2,name='2')
LIST=s.pca(lst,pc1,name='A',string='A')
#s.retim()

###s.codr('../stgres/tras2018-08-17.pickle','../stgres/tras22018-08-17.pickle')

#LIST=s.diff('../stgres/pcaGA2018-10-25.pickle','../stgres/pcaGB2018-10-25.pickle')
network.dragGraph(LIST[0][1],LIST[0][2],nx.kamada_kawai_layout(LIST[0][0]))
