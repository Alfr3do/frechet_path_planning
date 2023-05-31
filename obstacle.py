import numpy as np
from polygon import Polygon

class Obstacle(Polygon):
	TYPE_CIRCULAR = 0;
	TYPE_POLY = 1;
	def __init__(self, type):
		Polygon.__init__(self)
		self.type = type
		if (self.type == self.TYPE_CIRCULAR):
			self.radii = []#np.repeat(0,n) 

	def collides(self, v):
		if self.type == self.TYPE_CIRCULAR:
			for i in range(len(self.v)):
				if (self.distance(self.v[i], v) < self.radii[i] and abs(self.v[i][2] - v[2]) < 0.1):
					return True
			return False
		elif self.type == self.TYPE_POLY:
			raise NotImplementedError("Don't know how to tell whether v collides")
		else:
			return False;

	''' n_V: index of vertex '''
	def setRadius(self, n_v, radius):
		if (self.type == self.TYPE_CIRCULAR and n_v < len(self.v)):
			self.radii[n_v] = radius

	def addPos(self,v, rad=0):
		self.radii.append(rad)
		self.v.append(v);


	def draw(self, axis_plot, c_edge="g", c_vertex="b", mark="*"):

		print("drawing")

		if self.type == self.TYPE_CIRCULAR:
			for i in range(len(self.v)):
				if (self.radii[i] > 0):
					theta = np.linspace(0, 2 * np.pi, 201)
					y = self.radii[i]*np.sin(theta)
					z = self.radii[i]*np.cos(theta)
					phi = 1.6*np.pi
					axis_plot.plot(y*np.sin(phi)+self.v[i][0], z+self.v[i][1], self.v[i][2])
		elif self.type == self.TYPE_POLY:
			raise NotImplementedError("Don't know how to tell whether v collides")
		else:
			return false;
