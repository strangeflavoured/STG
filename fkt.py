import numpy as np
import pickle as p
import datetime

def ID(a):
	return a

def NOT(a):
	return not a

def AND(a,b):
	return a and b

def OR(a,b):
	return a or b

def XOR(a,b):
	return a and not b or not a and b

def intlog(x):
	ref=list(x).copy()
	for i,j in enumerate(ref):
		if ref[i]==0:
			ref[i]=False
		elif ref[i]==1:
			ref[i]=True
		else:
			raise ValueError
	return ref

def logint(ref):
	for i,j in enumerate(ref):
		if ref[i]:
			ref[i]=1
		else:
			ref[i]=0
	return ref

################## MODELL ########################
###(S,N,I,K1,K2,A)
def image(x):
	ref= intlog(x)	
	im=[ref[0],
	not ref[2],
	not ref[4] and not ref[3] or ref[1] and not ref[4],
	ref[0] and ref[5],
	ref[0] and not ref[5],
	ref[1]]
	im=logint(im)
	return im
#################################################

def imgs(x):
	im=image(x)
	img=[]
	for i,j in enumerate(im):
		if j!=x[i]:
			a=list(x)
			a[i]=j
			img.append(tuple(a))
	return img
	
def rep(a):
	for i in range(0,len(a)-1):
		if a[i]==a[-1]:
			return True
			break
		else:
			return False

def strg(a):
	S=[]
	for i,j in enumerate(a):
		J=''
		for k,l in enumerate(j):
			J+='{}'.format(l)
		S.append(J)
	return S

def labdic(a):
	S=strg(a)
	l={}
	for i,j in enumerate(a):
		l.update({j:mv(S[i])})
	return l

def mv(state):
	s=''.join(map(str,state))
	if s[4]=='1':
		s=s[:3]+'2'+s[5:]
	else:
		s=s[:4]+s[5:]
	return s

def insrt(lst,val,**kwargs):
	pos=kwargs.get('position',0)
	l=[]
	for i,j in enumerate(lst):
		a=list(j)
		a.insert(pos,val)
		l.append(tuple(a))
	return l

def Delay(state,delay):
	im=image(state)
	l=[]
	for i,j in enumerate(state):
		if j<im[i]:
			l.append(delay[i][0])
		elif j>im[i]:
			l.append(-1*delay[i][1])
		else:
			l.append('')
	return l

def delimg(state,images,delay,itr):
	Del=Delay(state,delay)
	lst=[]
	for i in Del:
		if isinstance(i,int) or isinstance(i,float):
			lst.append(abs(i))
	new=np.amax(lst)
	print(new)
	for i in range(0,new+itr):
		try:
			images[i+itr]
		except IndexError:
			images.append(images[-1].copy())
	for i,j in enumerate(Del):
		try:
			print(images,abs(j),itr,i)
			images[abs(j)+itr][i]+=np.sign(j)
		except TypeError:
			continue

def fulldict(states,images):
	dic={}
	for i,j in enumerate(states):
		dic[j]=images[i]
	return dic

def save(path,data):
	with open(path+'{}.pickle'.format(datetime.date.today()), 'wb+') as f:
		p.dump(data, f, p.HIGHEST_PROTOCOL)

def restore(path):
	with open(path,'rb') as f:
		data=p.load(f)
	return data

def prior(x,priority):
	im=image(x)
	img=[]
	IMG=[]
	for i,j in enumerate(im):	
		if j<x[i]:
			img.append(priority[i][-1])
		elif j>x[i]:
			img.append(priority[i][0])
		else:
			img.append('')
	try:
		m=min(k for k in img if isinstance(k,int))
		ind=[]
		for l,n in enumerate(img):
			if n==m:
				ind.append(l)
		for o,p in enumerate(ind):
			st=list(x)
			st[p]=im[p]
			IMG.append(tuple(st))
	except ValueError:
		IMG.append(x)	
	return IMG