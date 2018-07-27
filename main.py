import itertools
import networkx as nx
import matplotlib.pyplot as plt

def ID(a):
	if a==1:
		return 1
	else:
		return 0

def NOT(a):
	if a==0:
		return 1
	else:
		return 0

def AND(a,b):
	if a==1 and b==1:
		return 1
	else:
		return 0

def OR(a,b):
	if a==1 or b==1:
		return 1
	else:
		return 0

def XOR(a,b):
	if a==1 and b==0 or a==0 and b==1:
		return 1
	else:
		return 0

def rep(a):
	for i in range(0,len(a)-1):
		if a[i]==a[-1]:
			return True
			break
		else:
			return False

def image(x):
	return (NOT(x[2]),ID(x[0]),AND(x[0],x[1]))

def imgs(x):
	im=image(x)
	img=[]
	for i,j in enumerate(im):
		if j!=x[i]:
			a=list(x)
			a[i]=j
			img.append(tuple(a))
	return img

##STG OF ALL STATES##

states=list(itertools.product([0,1], repeat=3))

###ASYNCHRONOUS##
im=[]
for i,j in enumerate(states):
	im.append(imgs(j))

G=nx.DiGraph()
G.add_nodes_from(states)
for i,j in enumerate(states):
	for k in range(0,len(im[i])):
		G.add_edge(j,im[i][k])

fig,ax=plt.subplots(1,1)
nx.draw_kamada_kawai(G, node_color='w',node_shape='s',with_labels=True, font_weight='bold')
#plt.show()

G.clear()
plt.close()

###SYNCHRONOUS###
im=[]
for i,j in enumerate(states):
	im.append(image(j))

G=nx.DiGraph()
G.add_nodes_from(states)
for i,j in enumerate(states):
	G.add_edge(j,im[i])

fig,ax=plt.subplots(1,1)
nx.draw_kamada_kawai(G, node_color='w',node_shape='s',with_labels=True, font_weight='bold')
#plt.show()

G.clear()
plt.close()

##STG OF ONE STARTING STATE##
start=(1,0,1)

###SYNCHRONOUS###
states=[start]
im=[image(start)]

states.append(im[-1])
im.append(states[-1])

i=0
while not rep(states):	
	states.append(im[-1])
	im.append(image(states[-1]))
	if i>=10:
		break
	i+=1

G=nx.DiGraph()
G.add_nodes_from(states)
for i,j in enumerate(states):
	G.add_edge(j,im[i])

fig,ax=plt.subplots(1,1)
nx.draw_kamada_kawai(G, node_color='w',with_labels=True, font_weight='bold')
#plt.show()

G.clear()
plt.close()	

###ASYNCHRONOUS###
states=[start]
im=[imgs(start)]

k=0
while k<len(states):
	for j in range(0,len(im[-1])):
		if im[-1][j] not in states:
			states.append(im[-1][j])
	if k>0:
		im.append(imgs(states[k]))
	k+=1

G=nx.DiGraph()
G.add_nodes_from(states)
for i,j in enumerate(states):
	for k in range(0,len(im[i])):
		G.add_edge(j,im[i][k])

fig,ax=plt.subplots(1,1)
nx.draw_kamada_kawai(G, node_color='w',with_labels=True, font_weight='bold')
plt.show()

G.clear()
plt.close()	
