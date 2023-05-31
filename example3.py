from prm3d import PRM3D
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
	prm = PRM3D(
			start= start1, 
			goal= goal1,
			obstacles=O, 
			rand_area=[-50,200],
			n_samples = 80,
			n_near_conn = 3,
			max_dist_conn = 300
		)
	prm.planning()

	prm.draw(ax)

	start2 = [0,0,60]
	goal2 = [100,180,60]
	prm2 = PRM3D(
			start= start2, 
			goal= goal2,
			obstacles=O, 
			rand_area=[-50,200],
			n_samples = 80,
			n_near_conn = 3,
			depth = 60,
			max_dist_conn = 300
		)
	prm2.planning()

	prm2.draw(ax)


	O.draw(ax)

	plt.show()


if __name__ == '__main__':
    main()