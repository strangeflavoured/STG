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