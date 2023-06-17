"""

Path planning in 3D space with Probabilistics roadmap (PRM)

author: @Alfr3do based on AtsushiSakai(@Atsushi_twi)

"""
from graph import Graph
import random
from scipy.spatial import cKDTree
import numpy as np


class PRM3D(Graph):
	

	
	def __init__(self, 
				 start, 
				 goal,
				 obstacles, 
				 rand_area,
                 depth = 81, 
				 n_samples=50,
				 n_near_conn = 2,
				 max_dist_conn = 30
				 ):
		"""
        start: Start Position [x,y,z]
        goal: Goal Position [x,y,z]
        """
		random.seed(10)
		Graph.__init__(self)
		self.addPos(start)
		self.goal = goal
		self.obstacles = obstacles
		self.min_rand = rand_area[0]
		self.max_rand = rand_area[1]
		self.depth = depth
		self.n_samples = n_samples
		self.n_near_conn =  n_near_conn
		self.max_dist_conn = max_dist_conn

	def planning(self):
		"""
		prm path planning
		animation: flag for animation on or off
		"""
		# getting samples
		while len(self.v) < self.n_samples:
			tx = random.uniform(self.min_rand, self.max_rand)
			ty = random.uniform(self.min_rand, self.max_rand)
			if not self.obstacles.collides((tx,ty,self.depth)):
				self.addPos((tx,ty,self.depth))
		self.tree = cKDTree(self.v)

		self.addPos(self.goal)


		for vertex in range(len(self.v)):
			dists, indexes = self.tree.query(self.v[vertex], k = self.n_near_conn)

			for i in range(0,len(indexes)):
				if (dists[i] <= self.max_dist_conn):
					self.setAdjacent(indexes[i], vertex)