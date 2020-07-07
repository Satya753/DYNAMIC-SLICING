import xml.etree.ElementTree as etree

class Algorithm:

	def __init__(self):
		self.adj=[[] for _ in range(1000)]
		self.stex=[0 for _ in range(1000)]
		self.ans=[]
		self.rev=[0 for _ in range(1000)] 
		self.nnm={}
		self.fin={}

	def make_empty(self):
		self.ans=[]
	def change_to_numbering(self, a):
		val = a.split('.')
		c=''
		for i in val:
			c=c+i
		if c in self.nnm:
			self.dfs(self.nnm[c])
		else:
			print("NO SUCH NODE EXIST IN DEPENDENCY GRAPH")
			return 

	def dfs(self , v):
		self.ans.append(self.stex[v])
		for i in self.adj[v]:
			self.dfs(i)

	def print_result(self):
		return self.ans

	def generate_graph(self, file):
		tree=etree.parse(file)
		self.root1=tree.getroot()
		cnt=0
		for mx in self.root1.iter('mxCell'):
			val = str(mx.get('value'))
			if(len(val)>0):
				print(val)
				if(val[0]>='0' and val[0]<='9'):
					print(val)
					ts=val.split('.')
					p=''
					c=''
					for i in range(len(ts)-1):
						c=c+ts[i]
					self.nnm[c]=cnt
					self.rev[cnt]=c
					self.stex[cnt]=ts[-1]
					cnt=cnt+1
		for i in range(0 , cnt):
			for j in range(i , cnt):
				if((len(self.rev[i])-len(self.rev[j])==1 or len(self.rev[j])-len(self.rev[i])==1) and ((self.rev[i][-1]==self.rev[j][-2]) or (self.rev[j][-1]==self.rev[i][-2]))):
					if ((len(self.rev[i])>len(self.rev[j])) and (self.rev[j][-1]==self.rev[i][-2])):
						self.adj[i].append(j)
					elif ((len(self.rev[j])>len(self.rev[i])) and (self.rev[i][-1]==self.rev[j][-2])):
						self.adj[j].append(i)
		
		key_list = list(self.nnm.keys())
		key_value=list(self.nnm.values())

		for j in self.adj[i]:
			print(self.rev[j], end=' ')

