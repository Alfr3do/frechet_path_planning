from graph import Graph
from obstacle import Obstacle
import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def main():
	numVertex = 100
	G = Graph()
	F = Graph()

	O = Obstacle( Obstacle.TYPE_CIRCULAR)

	O.addPos([10,70,81])
	O.addPos([70,10,81])
	O.addPos([50,20,60])

	O.setRadius(0,50)
	O.setRadius(1,30)
	O.setRadius(2,10)


	actual = 0
	for pos in (np.random.rand(numVertex,2)*200):
		while (O.collides(np.append(pos,81))):
			pos = [pos[0]+1,pos[1]+1]
		G.addPos(np.append(pos,81))
		G.setAdjacent(actual,G.getCloser(actual))
		actual+=1

	actual = 0
	for pos in (np.random.rand(numVertex,2)*200):
		while (O.collides(np.append(pos,60))):
			pos = [pos[0]+1,pos[1]+1]
		F.addPos(np.append(pos,60))
		F.setAdjacent(actual,F.getCloser(actual))
		actual+=1


	fig = plt.figure()
	ax = fig.add_subplot(111, projection="3d")

	G.draw(ax)
	F.draw(ax, c_edge="b", c_vertex="r", mark="*")
	O.draw(ax)
	plt.show()




if __name__ == '__main__':
    main()