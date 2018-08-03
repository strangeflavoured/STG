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

################## MODELL ########################
def image(x):
	return (ID(x[0]),
	NOT(x[2]),
	OR(NOT(OR(x[3],x[4])),AND(x[1],NOT(x[3]))),
	AND(x[0],NOT(OR(x[5],OR(x[3],x[4])))),
	AND(x[0],OR(NOT(x[5]),OR(x[3],x[4]))),
	x[1])
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
		l.update({j:S[i]})
	return l

def insrt(lst,val,**kwargs):
	pos=kwargs.get('position',0)
	l=[]
	for i,j in enumerate(lst):
		a=list(j)
		a.insert(pos,val)
		l.append(tuple(a))
	return l