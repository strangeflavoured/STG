import networkx as nx
import matplotlib.pyplot as plt

from fkt import *
##STG OF ALL STATES##
def alla(lst):
	states=lst

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
	plt.show()

	G.clear()
	plt.close()

def alls(lst):
	states=lst
	im=[]
	for i,j in enumerate(states):
		im.append(image(j))

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		G.add_edge(j,im[i])

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',node_shape='s',with_labels=True, font_weight='bold')
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

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		G.add_edge(j,im[i])

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',with_labels=True, font_weight='bold')
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