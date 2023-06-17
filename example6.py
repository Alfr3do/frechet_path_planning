from obstacle import Obstacle
from graph import Graph

import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def main():
	print("start "+__file__)

	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")

	start1 = [0,0,81]
	goal1 = (200,150,81)
	prm = Graph(bidirectional = True)


	prm.addPos((10,10,81))
	prm.addPos((20,20,81))	
	prm.addPos((30,30,81))
	prm.addPos((40,40,81))
	prm.addPos((50,50,81))
	prm.addPos((60,60,81))
	prm.addPos((70,70,81))
	prm.addPos((80,80,81))
	prm.addPos((90,90,81))
	prm.addPos((100,100,81))
	prm.addPos((110,110,81))
	prm.addPos((120,120,81))
	prm.addPos(tuple(goal1))
	
	prm.setAdjacent(0,1,81)
	prm.setAdjacent(1,2,81)
	prm.setAdjacent(2,3,81)
	prm.setAdjacent(3,4,81)
	prm.setAdjacent(4,5,81)
	prm.setAdjacent(5,6,81)
	prm.setAdjacent(6,7,81)
	prm.setAdjacent(7,8,81)
	prm.setAdjacent(8,9,81)
	prm.setAdjacent(9,10,81)
	prm.setAdjacent(10,11,81)
	prm.setAdjacent(11,12,81)
	prm.draw(ax, labels=True)
	start2 = [0,0,60]
	goal2 = (100,180,60)
	prm2 = Graph(bidirectional = True)
	prm2.v.append((15,5,60))
	prm2.v.append((121,100,60))
	prm2.v.append((128, 45, 60))
	prm2.v.append((  7, 38, 60))
	prm2.v.append((129, 141, 60))
	prm2.v.append(( 92, 129, 60))
	prm2.v.append(( 50, 150, 60))
	prm2.v.append(( 30, 109, 60))
	prm2.v.append(( 80, 175, 60))
	prm2.v.append((25, 178, 60))
	prm2.v.append((154, 124, 60))
	prm2.v.append((140, 168, 60))

	prm2.v.append(tuple(goal2))
#	prm2.v.append(4)
#	prm2.v.append(5)
#	prm2.v.append(6)
	
	prm2.setAdjacent(0,1,81)
	prm2.setAdjacent(1,5,81)
	prm2.setAdjacent(0,2,81)
	prm2.setAdjacent(6,8,81)
	prm2.setAdjacent(5,6,81)
	prm2.setAdjacent(9,7,81)
	prm2.setAdjacent(9,6,81)
	prm2.setAdjacent(4,10,81)
	prm2.setAdjacent(3,5,81)
	prm2.setAdjacent(4,5,81)
	prm2.setAdjacent(12,11,81)
	prm2.setAdjacent(10,11,81)


	prm2.draw(ax, labels=True)


	biGraph = Graph()
	biGraph.addPos([0,0])
#	is_in_list = np.any(np.all([21,20] == biGraph.v, axis=0))

	
	cutOff_distance = 100

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


	plt.show()


if __name__ == '__main__':
    main()