import networkx as nx
import matplotlib.pyplot as plt
import itertools
from ast import literal_eval as tpl

from fkt import *

def retim():#returns image of a state given as input
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
	#calculates and plots asynchronous STG for a list of states
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
	save('../stgres/allaG',G)

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_networkx(G, pos=nx.kamada_kawai_layout(G),node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.savefig('../graphics/alla{}.svg'.format(strg),dpi=500)
	plt.show()

	G.clear()
	plt.close()

def alls(lst,**kwargs):
	#calculates and plots synchronous STG for a list of states
	strg=kwargs.get('string','')

	states=lst
	im=[]
	for i,j in enumerate(states):
		im.append(tuple(image(j)))


	dic=fulldict(states,im)
	save('../stgres/alls',dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		G.add_edge(j,im[i])
	save('../stgres/allsG',G)

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.savefig('../graphics/alls{}.svg'.format(strg),dpi=500)
	plt.show()

	G.clear()
	plt.close()

##STG OF ONE STARTING STATE##

def tras(start,**kwargs):
	#calculates and plots synchronous trajectory from an initial state
	strg=kwargs.get('string','')

	states=[start]
	im=[tuple(image(start))]

	states.append(im[-1])
	im.append(tuple(states[-1]))

	i=0
	while not rep(states):	
		states.append(im[-1])
		im.append(tuple(image(states[-1])))
		if i>=10:
			break
		i+=1

	dic=fulldict(states,im)
	save('../stgres/tras',dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		G.add_edge(j,im[i])
	save('../stgres/trasG',G)

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.savefig('../graphics/tras{}.svg'.format(strg),dpi=500)
	plt.show()

	G.clear()
	plt.close()	

def traa(start,**kwargs):
	#calculates and plots asynchronous trajectory from an initial state
	strg=kwargs.get('string','')

	states=[start]
	im=[imgs(start)]

	k=0
	while k<len(states):
		if k>0:
			im.append(imgs(states[k]))
		for j in range(0,len(im[-1])):
			if im[-1][j] not in states:
				states.append(im[-1][j])		
		k+=1

	dic=fulldict(states,im)
	save('../stgres/traa',dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		for k in range(0,len(im[i])):
			G.add_edge(j,im[i][k])
	save('../stgres/traaG',G)

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.savefig('../graphics/traa{}.svg'.format(strg),dpi=500)
	plt.show()

	G.clear()
	plt.close()

def td(start,delay,**kwargs):
	#work in progress: calculates and plots STG with time delay of components
	strg=kwargs.get('string','')

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
	save('../stgres/tdG',G)

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.savefig('../graphics/td{}.svg'.format(strg),dpi=500)
	plt.show()

	G.clear()
	plt.close()

def pca(lst,priority,**kwargs):
	#calculates and plots priority class trajectories from a given state
	strg=kwargs.get('string','')
	string=kwargs.get('name','')

	states=lst
	
	im=[]
	for i,j in enumerate(states):
		im.append(prior(j,priority))

	dic=fulldict(states,im)
	save('../stgres/pca'+string,dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		for k in range(0,len(im[i])):
			G.add_edge(j,im[i][k])
	save('../stgres/pcaG'+string,G)

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.savefig('../graphics/pca{}.svg'.format(strg),dpi=500)
	plt.show()

	G.clear()
	plt.close()

def pct(start,priority,**kwargs):
	#calculates and plots priority class trajectories for all states
	strg=kwargs.get('string','')
	string=kwargs.get('name','')
	
	states=[start]
	im=[prior(start,priority)]

	k=0
	while k<len(states):
		if k>0:
			im.append(prior(states[k],priority))
		for j in range(0,len(im[-1])):
			if im[-1][j] not in states:
				states.append(im[-1][j])		
		k+=1

	dic=fulldict(states,im)
	save('../stgres/pct'+string,dic)

	G=nx.DiGraph()
	G.add_nodes_from(states)
	for i,j in enumerate(states):
		for k in range(0,len(im[i])):
			G.add_edge(j,im[i][k])
	save('../stgres/pctG'+string,G)

	label=labdic(states)

	fig,ax=plt.subplots(1,1)
	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10,labels=label)
	plt.savefig('../graphics/pct{}.svg'.format(strg),dpi=500)
	plt.show()

	G.clear()
	plt.close()
	
###########################################################################################################
###OBSOLETE: networkx.difference(G,H)###
#def cotr(dicts):
#	#calculates something to do with the combinations of two states
#	#important
#	B={}
#	for m,n in enumerate(list(itertools.combinations(dicts.keys(),2))):		
#		A={}
#		for k,l in enumerate([n,n[::-1]]):				
#			for i in dicts[l[0]]:
#				if i not in dicts[l[1]]:
#					if i not in A:
#						A[i]=[dicts[l[0]][i]]
#					else:
#						if A[i]!=dicts[l[0]][i]:
#							for j in dicts[l[0]][i]:
#								if j not in A[i]:
#									A[i].append(j)
#				else:
#					if dicts[l[0]][i]!=dicts[l[1]][i]:
#						var=[]
#						for j in dicts[l[0]][i]:
#							if j not in dicts[l[1]][i]:
#								var.append(j)
#						if var:
#							if i not in A:
#								A[i]=var
#							else:
#								A[i].append(var)
#		N=n[0]+n[1]
#		B[N]=A
#	return B

#def comp(*args):
#	data={}
#	for i,j in enumerate(args):
#		data[str(i)]=restore(j)
#	res=cotr(data)
#	return res
	
#def codr(*args):
#	#compares and plots trajectories
#	res=comp(*args)
#	for i in res:
#		G=nx.DiGraph()
#		val=[]
#		for n,o in enumerate(res[i].values()):
#			for p,q in enumerate(o):
#				val.append(q)
#		G.add_nodes_from(res[i].keys())
#		G.add_nodes_from(val)
#		for j,k in enumerate(res[i]):
#			for l,m in enumerate(res[i][k]):
#				G.add_edge(k,m)
#	fig,ax=plt.subplots(1,1)
#	nx.draw_kamada_kawai(G, node_color='w',edgecolors='w',scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color='r',font_size=10)#,labels=label)
#	plt.show()

#	G.clear()
#	plt.close()
##############################################################################################################

def diff(*args):
	graphs=[]
	for i,j in enumerate(args):
		graphs.append(restore(j))
	DIFF=[]
	for k,l in enumerate(list(itertools.combinations(range(len(graphs)),2))):
		DIFF.append(nx.symmetric_difference(graphs[l[0]],graphs[l[1]]))
		#DIFF.append((nx.difference(graphs[l[0]],graphs[l[1]]),nx.difference(graphs[l[1]],graphs[l[0]])))

	fig,ax=plt.subplots(1,1)
	
	#cl=[(('k','r'),('b','g'))]
	#for m,n in enumerate(DIFF):
	#	nx.draw_kamada_kawai(n[0], node_color='w',edgecolors=cl[m][0][0],scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color=cl[m][0][1],font_size=10,labels=labdic(n[0].nodes()))
	#	nx.draw_kamada_kawai(n[1], node_color='w',edgecolors=cl[m][1][0],scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color=cl[m][1][1],font_size=10,labels=labdic(n[1].nodes()))
		
	cl=[('k','r')]
	for m,n in enumerate(DIFF):
		label=labdic(n.nodes())
		nx.draw_kamada_kawai(n, node_color='w',edgecolors=cl[m][0],scale=5,node_shape='s',node_size=0,with_labels=True, font_weight='bold',font_color=cl[m][1],font_size=10,labels=label)
	
	plt.show()
	plt.close()
