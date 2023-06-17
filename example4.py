from prm3d import PRM3D
from obstacle import Obstacle
from graph import Graph

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
	print("start "+__file__)
	O = Obstacle( Obstacle.TYPE_CIRCULAR)

	O.addPos([10,70,81])
	O.addPos([70,10,81])
	O.addPos([50,20,60])
	O.addPos([100,50,60])


	O.setRadius(0,50)
	O.setRadius(1,30)
	O.setRadius(2,10)
	O.setRadius(3,60)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")

	start1 = [0,0,81]
	goal1 = [200,150,81]
	prm = PRM3D(
			start= start1, 
			goal= goal1,
			obstacles=O, 
			rand_area=[-50,200],
			n_samples = 250,
			n_near_conn = 4,
			max_dist_conn = 60
		)
	prm.planning()

	prm.draw(ax, c_edge='purple')

	start2 = [0,0,60]
	goal2 = [100,180,60]
	prm2 = PRM3D(
			start= start2, 
			goal= goal2,
			obstacles=O, 
			rand_area=[-50,200],
			n_samples = 200,
			n_near_conn = 4,
			depth = 60,
			max_dist_conn = 40
		)
	prm2.planning()

	prm2.draw(ax)


	biGraph = Graph()
	biGraph.addPos([0,0])
#	is_in_list = np.any(np.all([21,20] == biGraph.v, axis=0))

	
	cutOff_distance = 350

	for i in range(len(prm.v)):
		if i in prm.adj:
			tmp = [x.v_to for x in prm.adj[i]]
			tmp.append(i)
			for j in range(len(prm2.v)):

				if j in prm2.adj:
					dist1 = Graph.distance(prm.v[i], prm2.v[j])
					if  dist1 > cutOff_distance:
						#print("continuing")
						continue;
					tmp2 = [x.v_to for x in prm2.adj[j]]
					tmp2.append(j)
					inter = [[x,y] for x in tmp for y in tmp2 ]
					del inter[inter.index([i,j])]
					if ([i,j] not in biGraph.v):
						biGraph.addPos([i,j])
					from_biGraph = biGraph.v.index([i,j]) 
					for k in inter:
						if k not in biGraph.v:
							biGraph.addPos(k)
						to_biGraph = biGraph.v.index(k) 
						
						dist2 = Graph.distance(prm.v[k[0]], prm2.v[k[1]])

						#add an edge between [i,j] and k
						#the distance has to be the distance betwen the segments
						biGraph.setAdjacent(from_biGraph, to_biGraph, max(dist1, dist2))
						#print(from_biGraph, to_biGraph, len(biGraph.v))

			#	print(prm.adj[i])
				#tmp = [x for x in prm.adj[i]]
				#print(tmp)
				#tmp = 
				#print( tmp )

#	for e in biGraph.getEdges():
#		print(biGraph.v[e[0]]," --> ", biGraph.v[e[1]])

	print(prm.v.index(goal1), prm2.v.index(goal2))

	if [prm.v.index(goal1), prm2.v.index(goal2)] in biGraph.v:
		biGoal = biGraph.v.index([prm.v.index(goal1), prm2.v.index(goal2)])

		res = biGraph.dijsktra(0,biGoal)
		print(res)
		if res['found']:
			response = Graph()
			k = 0
			for i in res['path']:
				print("--->",i)
				response.addPos(prm.v[i[0]])
				response.addPos(prm2.v[i[1]])
				response.setAdjacent(k,k+1)
				k += 2
			response.draw(ax, c_edge='r')

	O.draw(ax)
	ax.scatter(*start1, marker='D', color='black')
	ax.scatter(*start2, marker='D', color='black')

	ax.scatter(*goal1, marker='X', color='cyan')
	ax.scatter(*goal2, marker='X', color='cyan')

	plt.show()


if __name__ == '__main__':
    main()