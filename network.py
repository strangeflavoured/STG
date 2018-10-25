import networkx as nx
import tkinter as tk
from tkinter import messagebox,simpledialog,filedialog
import numpy as np
import canvasvg
import os
class ResizingCanvas(tk.Canvas):
	def __init__(self,parent,**kwargs):
		tk.Canvas.__init__(self,parent,**kwargs)
		self.bind("<Configure>", self.on_resize)
		self.height = self.winfo_reqheight()
		self.width = self.winfo_reqwidth()
		self.initial_ratio = self.width/self.height

	def on_resize(self,event):
		# determine the ratio of old width/height to new width/height
		wscale = float(event.width)/self.width
		hscale = float(event.height)/self.height
		self.width = event.width
		self.height = event.height
		# resize the canvas 
		self.config(width=self.width, height=self.height) 
		# rescale all the objects tagged with the "all" tag
		if (self.width/self.height) > self.initial_ratio:
			self.scale("all",0,0,hscale,hscale)
			#print("1")
		elif (self.width/self.height) < self.initial_ratio:
			self.scale("all",0,0,wscale,wscale)
			#print("2")
		elif (self.width/self.height) == self.initial_ratio:
			self.scale("all",0,0,wscale,hscale)
			#print("3")

def dragGraph(nodes,edges,pos):
	cord=[i for i in pos.values()]

	#nx.draw_networkx(G, pos=p)
	xmin=np.amin([i[0] for i in pos.values()])
	xmax=np.amax([i[0] for i in pos.values()])
	xl=xmax-xmin
	ymin=np.amin([i[1] for i in pos.values()])
	ymax=np.amax([i[1] for i in pos.values()])
	yl=ymax-ymin
	#plt.show()

	canvaswidth=750
	canvasheight=500
	nodesize=10
	window=tk.Tk()
	canvas=tk.Canvas(window,width=canvaswidth, height=canvasheight, bg='white')
	canvas = ResizingCanvas(window,width=750, height=500, bg="white", highlightthickness=0)
	canvas.pack(fill='both',expand='yes')

	def nodesize():
		canvas.update()
		return canvas.winfo_height()/50

	def transformx(a):
		return (a-xmin)*650/xl+50

	def transformy(a):
		return (ymax-cord[i][1])*400/yl+50

	def alpha(line):
		return np.arctan((canvas.coords(line)[1]-canvas.coords(line)[3])/(canvas.coords(line)[2]-canvas.coords(line)[0]))

	def beta(line):
		return np.arctan((canvas.coords(line)[2]-canvas.coords(line)[0])/(canvas.coords(line)[1]-canvas.coords(line)[3]))

	ids={}
	wids={}
	edict={}

	for i,j in enumerate(nodes):
		#print((cord[i][0]-xmin)*750/xl,(cord[i][0]-ymin)*500/yl)
		xtraf=transformx(cord[i][0])
		ytraf=transformy(cord[i][1])
		x0=xtraf-nodesize()
		x1=xtraf+nodesize()
		y0=ytraf-nodesize()
		y1=ytraf+nodesize()
		J=canvas.create_oval(x0,y0,x1,y1,fill='red')
		w=canvas.create_text(xtraf,ytraf,text=j)
		ids[j]=J
		wids[w]=J
		edict[J]=[]

	wdict={v: k for k, v in wids.items()}
	#print(wdict)
	#print(ids)
	#print(edict)
	IDict={}

	for k,l in enumerate(edges):    
		x0=np.mean((float(canvas.coords(ids[l[0]])[0]),float(canvas.coords(ids[l[0]])[2])))
		x1=np.mean((float(canvas.coords(ids[l[1]])[0]),float(canvas.coords(ids[l[1]])[2])))
		y0=np.mean((float(canvas.coords(ids[l[0]])[1]),float(canvas.coords(ids[l[0]])[3])))
		y1=np.mean((float(canvas.coords(ids[l[1]])[1]),float(canvas.coords(ids[l[1]])[3])))
		
		if x0!=x1:
			X0=x0+np.sign(x1-x0)*nodesize()*np.absolute(np.cos(np.arctan((y0-y1)/(x1-x0))))    
			Y0=y0+np.sign(y1-y0)*nodesize()*np.absolute(np.sin(np.arctan((y0-y1)/(x1-x0))))
		else:
			X0=x0+np.sign(x1-x0)*nodesize()*np.absolute(np.cos(np.pi/2))    
			Y0=y0+np.sign(y1-y0)*nodesize()*np.absolute(np.sin(np.pi/2))
		if y0!=y1:    
			X1=x1+np.sign(x0-x1)*nodesize()*np.absolute(np.sin(np.arctan((x1-x0)/(y0-y1))))
			Y1=y1+np.sign(y0-y1)*nodesize()*np.absolute(np.cos(np.arctan((x1-x0)/(y0-y1))))
		else:
			X1=x1+np.sign(x0-x1)*nodesize()*np.absolute(np.sin(np.pi/2))
			Y1=y1+np.sign(y0-y1)*nodesize()*np.absolute(np.cos(np.pi/2))
		ID=canvas.create_line(X0,Y0,X1,Y1,arrow=tk.LAST)
		edict[ids[l[0]]].append((ID,0))
		edict[ids[l[1]]].append((ID,1))
		IDict[ID]=[ids[l[0]],ids[l[1]]]
		canvas.tag_lower(ID)
	canvas.addtag_all("all")
	#print(edict)
		
	#FOR ARROW WIDGET IN CANVAS WIDGET#############################
	#label_1 = tk.Label(window, text = "from here", anchor = tk.W)
	#label_1.configure(width = 10, activebackground = "#33B5E5", relief = tk.FLAT)
	#label_1_window = canvas.create_window(280, 0, anchor=tk.NW, window=label_1)
	   
	def onClick(event):
		global item,push
		global stick,name
		item=canvas.find_enclosed(event.x-2*nodesize(), event.y-2*nodesize(), event.x+2*nodesize(), event.y+2*nodesize())
		if item:
			push=True
			for i,j in enumerate(item):
				#print(edict[j],wdict[j])
				if j in edict.keys():
					stick=edict[j]
					if j in wdict.keys():
						name=wdict[j]
						
	def rightclick(event):
		ev=canvas.find_enclosed(event.x-20, event.y-20, event.x+20, event.y+20)
		for i,j in enumerate(edict[ev[0]]):
			print(j[0],':\n',canvas.coords(j[0]))


	def onRelease(event):
		global item,push
		global stick,name
		item=None
		stick=None
		name=None
		push=False       
		window.update()
		
	def onDrag(event):
		global push
		if push:
			global stick,item,name
			#print(item,name)
			x=event.x
			y=event.y
			if item[0] in edict.keys():
				canvas.coords(item[0],x+nodesize(),y+nodesize(),x-nodesize(),y-nodesize())
				canvas.coords(name,x,y)
			if stick:                
				for i,j in enumerate(stick):                
					if j[1]==0:
						x1=np.mean((canvas.coords(IDict[j[0]][1])[0],canvas.coords(IDict[j[0]][1])[2]))
						y1=np.mean((canvas.coords(IDict[j[0]][1])[1],canvas.coords(IDict[j[0]][1])[3]))
						if y==y1 and x!=x1:
							dx0=-np.sign(x-x1)*nodesize()*np.absolute(np.cos(np.arctan((y-y1)/(x1-x))))
							dy0=np.sign(y1-y)*nodesize()*np.absolute(np.sin(np.arctan((y-y1)/(x1-x))))
							dx1=-np.sign(x1-x)*nodesize()*np.absolute(np.sin(np.pi/2))             
							dy1=np.sign(y-y1)*nodesize()*np.absolute(np.cos(np.pi/2))
						elif x==x1 and y!=y1:
							dx0=-np.sign(x-x1)*nodesize()*np.absolute(np.cos(np.pi/2))
							dy0=np.sign(y1-y)*nodesize()*np.absolute(np.sin(np.pi/2))
							dx1=-np.sign(x1-x)*nodesize()*np.absolute(np.sin(np.arctan((x1-x)/(y-y1))))               
							dy1=np.sign(y-y1)*nodesize()*np.absolute(np.cos(np.arctan((x1-x)/(y-y1))))
						elif x==x1 and y==y1:
							dx0=-np.sign(x-x1)*nodesize()*np.absolute(np.cos(np.pi/2))
							dy0=np.sign(y1-y)*nodesize()*np.absolute(np.sin(np.pi/2))
							dx1=-np.sign(x1-x)*nodesize()*np.absolute(np.sin(np.pi/2))             
							dy1=np.sign(y-y1)*nodesize()*np.absolute(np.cos(np.pi/2))
						else:                                            
							dx0=-np.sign(x-x1)*nodesize()*np.absolute(np.cos(np.arctan((y-y1)/(x1-x))))
							dy0=np.sign(y1-y)*nodesize()*np.absolute(np.sin(np.arctan((y-y1)/(x1-x))))
							dx1=-np.sign(x1-x)*nodesize()*np.absolute(np.sin(np.arctan((x1-x)/(y-y1))))               
							dy1=np.sign(y-y1)*nodesize()*np.absolute(np.cos(np.arctan((x1-x)/(y-y1))))                   
						canvas.coords(j[0],x+dx0,y+dy0,x1+dx1,y1+dy1)
						#print(1,dx1,dy1,dx1**2+dy1**2)
					elif j[1]==1:
						x0=np.mean((canvas.coords(IDict[j[0]][0])[0],canvas.coords(IDict[j[0]][0])[2]))
						y0=np.mean((canvas.coords(IDict[j[0]][0])[1],canvas.coords(IDict[j[0]][0])[3]))
						if y0==y and x0!=x:
							dx0=-np.sign(x0-x)*nodesize()*np.absolute(np.cos(np.arctan((y0-y)/(x-x0))))
							dy0=np.sign(y-y0)*nodesize()*np.absolute(np.sin(np.arctan((y0-y)/(x-x0))))
							dx1=-np.sign(x-x0)*nodesize()*np.absolute(np.sin(np.pi/2))               
							dy1=np.sign(y0-y)*nodesize()*np.absolute(np.cos(np.pi/2))
						elif x0==x and y0!=y:
							dx0=-np.sign(x0-x)*nodesize()*np.absolute(np.cos(np.pi/2))
							dy0=np.sign(y-y0)*nodesize()*np.absolute(np.sin(np.pi/2))
							dx1=-np.sign(x-x0)*nodesize()*np.absolute(np.sin(np.arctan((x-x0)/(y0-y))))            
							dy1=np.sign(y0-y)*nodesize()*np.absolute(np.cos(np.arctan((x-x0)/(y0-y))))
						elif x0==x and y0==y:
							dx0=-np.sign(x0-x)*nodesize()*np.absolute(np.cos(np.pi/2))
							dy0=np.sign(y-y0)*nodesize()*np.absolute(np.sin(np.pi/2))
							dx1=-np.sign(x-x0)*nodesize()*np.absolute(np.sin(np.pi/2))       
							dy1=np.sign(y0-y)*nodesize()*np.absolute(np.cos(np.pi/2))
						else:                                            
							dx0=-np.sign(x0-x)*nodesize()*np.absolute(np.cos(np.arctan((y0-y)/(x-x0))))
							dy0=np.sign(y-y0)*nodesize()*np.absolute(np.sin(np.arctan((y0-y)/(x-x0))))
							dx1=-np.sign(x-x0)*nodesize()*np.absolute(np.sin(np.arctan((x-x0)/(y0-y))))             
							dy1=np.sign(y0-y)*nodesize()*np.absolute(np.cos(np.arctan((x-x0)/(y0-y))))
						canvas.coords(j[0],x0+dx0,y0+dy0,x+dx1,y+dy1)
						#print(0,dx0,dy0,dx0**2+dy0**2)
			window.update()

	def savedialog():
		file = filedialog.asksaveasfilename(parent=window, initialdir=os.getcwd(), title="Please select a file name to save:", filetypes=[('png file','*.png'),('jpeg file','*.jpeg'),("svg file","*.svg")])
		if file:
			canvasvg.saveall(file, canvas)

	def save(event):
		savedialog()

	def close():
		saveimg=tk.messagebox.askyesno(message='Do you want to save?')
		if saveimg:
			savedialog()
		window.destroy()

		item=None
	stick=None
	name=None
	push=None

	button1=tk.Button(window,text='save',width=10)
	button1.pack(side='right')
	button1.bind('<Button-1>',save)

	window.bind('<ButtonRelease-1>',onRelease)
	window.bind('<Button-1>',onClick)    
	window.bind('<B1-Motion>',onDrag)
	window.bind('<Button-3>',rightclick)
	window.protocol("WM_DELETE_WINDOW", close)

	window.mainloop()
