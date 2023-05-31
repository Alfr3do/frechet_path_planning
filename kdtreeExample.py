import numpy as np

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

from scipy.spatial import cKDTree


def main():
	points = [(0,0,0),(1,1,1),(2,2,2)]
	tree = cKDTree(points)
	dist, pos = tree.query((0,1,1))

	print ("distance: ",dist," index: ", pos," point: ", points[pos])
	dist, pos = tree.query((0,0,1))
	print ("distance: ",dist," index: ", pos," point: ", points[pos])

if __name__ == '__main__':
	main()