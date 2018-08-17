import networkx as nx
import matplotlib.pyplot as plt
import itertools
from fkt import *

def retim():
	while True:
		try:
			inp=input('state: ')
			mv=False
			if not inp:
				break
			elif len(inp) !=6:
				if len(inp)==5:
					if inp[3]=='2':
						inp=inp[:3]+'01'+inp[4:]
					elif inp[3]=='1' or inp[3]=='0':
						inp=inp[:4]+'0'+inp[4:]
					mv=True						
				else:
					raise IndexError		
			
			l=''.join(str(i) for i in image(list(map(int,inp))))
			if mv:
				if l[4]=='1':
					l=l[:3]+'2'+l[5:]
				elif l[4]=='0':
					l=l[:4]+l[5:]
			print('image: '+l)
		except IndexError:
			print('IndexError: Please enter 5 (multivalued) or 6 (boolean) digits')
		except ValueError:
			print('ValueError: Please enter integers 0,1 (2 only multivalued)')
			
##STG OF ALL STATES##
			
	
def alla(lst,**kwargs):
	strg=kwargs.get('string','')
	states=lst

	im=[]
	for i,j in enumerate(states):
		im.append(imgs(j))

	dic=fulldict(states,im)
	save('../stgres/alla',dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		for k in range(0,len(im[i])):
			G.add_edge(j,im[i][k])

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_networkx(G, pos=nx.kamada_kawai_layout(G),node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.savefig('../graphics/alla{}.svg'.format(strg),dpi=500)
	plt.show()

	G.clear()
	plt.close()

def alls(lst):
	states=lst
	im=[]
	for i,j in enumerate(states):
		im.append(image(j))

	dic=fulldict(states,im)
	save('../stgres/alls',dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		G.add_edge(j,im[i])

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.show()

	G.clear()
	plt.close()

##STG OF ONE STARTING STATE##

def tras(start):
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

	dic=fulldict(states,im)
	save('../stgres/tras',dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		G.add_edge(j,im[i])

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.show()

	G.clear()
	plt.close()	

def traa(start):
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

	dic=fulldict(states,im)
	save('../stgres/traa',dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		for k in range(0,len(im[i])):
			G.add_edge(j,im[i][k])

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.show()

	G.clear()
	plt.close()

def td(start,delay):
	Del=delay
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

	dic=fulldict(states,im)
	save('../stgres/td',dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		for k in range(0,len(im[i])):
			G.add_edge(j,im[i][k])

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.show()

	G.clear()
	plt.close()

def cotr(**args):
	B={}
	for m,n in enumerate(list(itertools.combinations(args.keys(),2))):
		A={}
		for k,l in enumerate([n,n[::-1]]):				
			for i in args[l[0]]:
				if i not in args[l[1]]:
					if i not in A:
						A[i]=args[l[0]][i]
					else:
						if A[i]!=args[l[0]][i]:
							for j in args[l[0]][i]:
								if j not in A[i]:
									A[i].append(j)
				else:
					if args[l[0]][i]!=args[l[1]][i]:
						var=[]
						for j in args[l[0]][i]:
							if j not in args[l[1]][i]:
								var.append(j)
						if var:
							if i not in A:
								A[i]=var
							else:
								A[i].append(var)
		N=n[0]+n[1]
		B[N]=A
	return B