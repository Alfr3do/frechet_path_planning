from graph import Graph

g = Graph(bidirectional = True)

g.v.append(1)
g.v.append(2)
g.v.append(3)
g.v.append(4)
g.v.append(5)
g.v.append(6)

g.setAdjacent(0,1,7)
g.setAdjacent(0,5,14)
g.setAdjacent(0,2,9)
g.setAdjacent(1,2,10)
g.setAdjacent(1,3,15)
g.setAdjacent(2,5,2)
g.setAdjacent(2,3,11)
g.setAdjacent(3,4,6)
g.setAdjacent(4,5,9)


path = g.dijsktra(0,4)

print(path['found'])

