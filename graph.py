import numpy as np
from polygon import Polygon
class Graph(Polygon):
	class Edge:
		def __init__(self, v_from, v_to, weight):
			
			self.v_from=v_from
			self.v_to = v_to
			self.weight = weight

	def __init__(self):
		Polygon.__init__(self)
		#self.adj=np.zeros((n,n))
		self.adj={}


	def getEdges(self):
		res = []
		for i in self.adj:
			for j in self.adj[i]:
				res.append([j.v_from,j.v_to])
					#print(str(i)+" -> "+str(j))
		return res

	def setAdjacent(self, v_from, v_to, weight=1):
		if (v_from>=0 and v_to>=0 and len(self.v)>v_from and len(self.v)>v_to ):
			if v_from not in self.adj.keys():
				self.adj[v_from] = []
			self.adj[v_from].append(self.Edge(v_from, v_to , weight));

	def draw(self, axis_plot, c_edge="g", c_vertex="b", mark="*"):
		#axis_plot.plot(*self.getEdges(), 'b')
		for i,j in self.getEdges():
			#print(self.v[i],"-->",self.v[j])
			axis_plot.plot(*zip(self.v[i],self.v[j]), color=c_edge)
		for i in self.v:
			axis_plot.scatter(*i,marker=mark, color=c_vertex)
