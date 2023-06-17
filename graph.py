import numpy as np
from polygon import Polygon
class Graph(Polygon):
	class Edge:
		def __init__(self, v_from, v_to, weight):
			
			self.v_from=v_from
			self.v_to = v_to
			self.weight = weight
		def __str__(self):
			return str(self.v_from)+"-->"+str(self.v_to)

	class Queue:
		def __init__(self):
			self.data = {}
			pass

		def put(self, d):
			self.data[d[1]] = d[0]

		def get(self):
			min = np.inf
			index = 0
			for i in self.data:
				if self.data[i] < min:
					min = self.data[i]
					index = i
			del self.data[index]
			return (min, index)

		def empty(self):
			return len(self.data)== 0


	def __init__(self, bidirectional = False):
		Polygon.__init__(self)
		#self.adj=np.zeros((n,n))
		self.bidirectional = bidirectional
		self.adj={}


	def getEdges(self):
		res = []
		for i in self.adj:
			for j in self.adj[i]:
				res.append([j.v_from,j.v_to])
					#print(str(i)+" -> "+str(j))
		return res

	def setAdjacent(self, v_from, v_to, weight=1):
		if (v_from>=0 and v_to>=0 and len(self.v)>v_from and len(self.v)>v_to and v_from != v_to):
			if v_from not in self.adj.keys():
				self.adj[v_from] = []
			self.adj[v_from].append(self.Edge(v_from, v_to , weight));
			
			if self.bidirectional:
				if v_to not in self.adj.keys():
					self.adj[v_to] = []
				self.adj[v_to].append(self.Edge(v_to, v_from , weight));	


	def draw(self, axis_plot, c_edge="g", c_vertex="b", mark="*", labels=False):
		#axis_plot.plot(*self.getEdges(), 'b')
		for i,j in self.getEdges():
			#print(self.v[i],"-->",self.v[j])
			axis_plot.plot(*zip(self.v[i],self.v[j]), color=c_edge)
		txt = 0
		for i in self.v:
			axis_plot.scatter(*i, marker=mark, color=c_vertex)
			if labels:
				axis_plot.text(*i, txt)
			txt += 1
		
			

	def dijsktra(self, source, goal):
		q = self.Queue()
		dist = {}
		prev = {}
		q.put((0, source))
		dist[source] = 0

		while not q.empty():
			next_i = q.get()
			#print("found ",self.v[next_i[1]], " distance ",next_i[0])
			if next_i[1] not in self.adj:
				continue
			for edge in self.adj[next_i[1]]:
				dist_to_adj = next_i[0] +  edge.weight
				if edge.v_to in dist:
					if dist[edge.v_to] > dist_to_adj:
						#print("to ",self.v[edge.v_to]," better distance ",dist_to_adj)
						dist[edge.v_to] = dist_to_adj
						prev[edge.v_to] = next_i[1]	
						q.put((dist_to_adj, edge.v_to))
					else:
						#print("to ",self.v[edge.v_to]," distance not better ",dist_to_adj)
						pass
					# node already  discovered, check if better

				else:
					#print("added ",self.v[edge.v_to]," (",dist_to_adj,") ")
					dist[edge.v_to] = dist_to_adj
					prev[edge.v_to] = next_i[1]
					q.put((dist_to_adj, edge.v_to))

		#print(dist)
		#print(prev)
		tmp = goal
		path = [self.v[tmp]]#str(self.v[tmp])+"-->"

		while tmp in prev:
			#res += str(self.v[prev[tmp]])+"-->"
			path.append(self.v[prev[tmp]])
			tmp = prev[tmp]
			if tmp == source:

				return {'found':True, 'path': path}
				break;
		#print(res)
		return {'found':False, 'path': path}
#		for v in range(len(self.v)):
#			dist[v] = np.inf
#			prev[v] = None
#			q.put(())