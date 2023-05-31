"""

Path planning in 3D space with Randomized Rapidly-Exploring Random Trees (RRT)

author: @Alfr3do based on AtsushiSakai(@Atsushi_twi)

"""
from graph import Graph
import random

class RRT3D(Graph):
    START_POINT = 0
    def __init__(self, 
				 start, 
				 goal,
				 obstacles, 
				 rand_area,
                 depth = 81, 
				 expand_dis=3.0,
				 path_resolution=0.5,
				 goal_sample_rate=5,
				 max_iter=500):
        """
        start: Start Position [x,y,z]
        goal: Goal Position [x,y,z]
        """
        Graph.__init__(self)
        self.addPos(start)
        self.goal = goal
        self.obstacles = obstacles
        self.min_rand = rand_area[0]
        self.max_rand = rand_area[1]
        self.expand_dis = expand_dis
        self.path_resolution = path_resolution
        self.goal_sample_rate = goal_sample_rate
        self.max_iter = max_iter
        self.depth = depth


    def planning(self, axis_plot, animation=True):
        """
        rrt path planning

        animation: flag for animation on or off
        """

        for i in range(self.max_iter):
            rnd_node = self.get_random_node()
            nearest_ind = self.getCloserToPoint(rnd_node)
            nearest_node = self.v[nearest_ind]

            new_node = self.steer(nearest_node, rnd_node, self.expand_dis)

            if not self.obstacles.collides(new_node):
                self.addPos(new_node)
                self.setAdjacent(nearest_ind, len(self.v)-1)


            if self.distance(self.v[-1],self.goal) <= self.expand_dis:
                final_node = self.steer(self.v[-1], self.goal,
                                        self.expand_dis)
                if not self.obstacles.collides(final_node):
                    pass
                    #return self.generate_final_course(len(self.v) - 1)


        return None  # cannot find path



    def get_random_node(self):
        if random.randint(0, 100) > self.goal_sample_rate:
            rnd = [
                random.uniform(self.min_rand, self.max_rand),
                random.uniform(self.min_rand, self.max_rand),
                self.depth
                ]
        else:  # goal point sampling
            rnd = self.goal
        return rnd

    def steer(self, from_node, to_node, extend_length=float("inf")):

        d = self.distance(from_node, to_node)

        if extend_length > d:
            extend_length = d

        t = extend_length/d

        new_node = [from_node[i]+(to_node[i]-from_node[i])*t for i in range(3)]

        #print(f"from {from_node} to {to_node} distance {d}  intended {extend_length} final {new_node}")

        return new_node

    def generate_final_course(self, goal_ind):
        path = [[self.goal]]
        while goal_ind in self.adj.keys():
            path.append(self.v[self.adj[goal_ind].v_from])
            goal_ind = self.adj[goal_ind].v_from
        if goal_ind in self.adj and self.adj[goal_ind].v_from in self.v:
            path.append(self.v[self.adj[goal_ind].v_from])
        else:
            print(f"{goal_ind} not in adj {len(self.v)}")

        return path