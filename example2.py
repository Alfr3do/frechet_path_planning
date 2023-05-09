from rrt3d import RRT3D
from obstacle import Obstacle

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
	rrt = RRT3D(
			start= start1, 
			goal= goal1,
			obstacles=O, 
			expand_dis=10.0,
			rand_area=[-50,200]
		)

	start2 = [0,0,60]
	goal2 = [100,180,60]
	rrt2 = RRT3D(
			start= start2, 
			goal= goal2,
			obstacles=O, 
			expand_dis=10.0,
			rand_area=[-50,200],
			depth=60
		)

	path = rrt.planning(animation=True)
	path2 =  rrt2.planning(animation=True)
	if path is None:
		print("Cannot find path")
	else:
		print("found path!!")	

	O.draw(ax)
	ax.scatter(*start1,marker="x", color="r")
	ax.scatter(*start2,marker="x", color="r")
	ax.scatter(*goal1,marker="x", color="r")
	ax.scatter(*goal2,marker="x", color="r")
	rrt.draw(ax)
	rrt2.draw(ax)
	plt.show()


if __name__ == '__main__':
    main()