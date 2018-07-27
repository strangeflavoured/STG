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

#################################################
def image(x):
	return (NOT(x[2]),ID(x[0]),AND(x[0],x[1]))
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