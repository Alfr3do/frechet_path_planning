import numpy as np
class Polygon:
	def __init__(self):
		self.v = []
		
	def getCloserToPoint(self, vertex):
		closer = -1
		min_dist = np.inf
		for i in range(len(self.v)):
			dist = self.distance(self.v[i], vertex)
			if dist < min_dist:
				min_dist = dist
				closer = i
		return closer

	def getCloser(self, vertex_ind):
		closer = -1
		min_dist = np.inf
		for i in range(len(self.v)):
			if (i != vertex_ind):
				dist = self.distanceBetween(i, vertex_ind)
				if dist < min_dist:
					min_dist = dist
					closer = i
		return closer

	def distance(self, vertex1, vertex2):
		return np.linalg.norm(np.array(vertex1) - np.array(vertex2))

	def distanceBetween(self, vertex_ind1, vertex_ind2):
		if (len(self.v) < vertex_ind1 or len(self.v) < vertex_ind2 or self.v[vertex_ind1][0] == np.inf or self.v[vertex_ind2][0] == np.inf):
			return np.inf
		return self.distance(self.v[vertex_ind1], self.v[vertex_ind2])

	def setVerticesPos(self,vertices): 
		# receives a list of verteces positions   
		self.v = vertices;

	def addVertexXYZ(self,x,y,z,vertex): 
		self.v.append([x,y,z]);

	def getPos(self, vertex):
		return self.v[vertex] if vertex<len(self.v) else np.empty((1,2))*np.nan	

	def addPos(self,v):
		self.v.append(np.array(v));
	def setPos(self,v,vertex): 
		if len(self.v) > vertex:
			self.v[vertex] = v;
