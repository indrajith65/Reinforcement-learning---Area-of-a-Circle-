# Reinforcement learning

import math
import numpy as np

class CircleEnv():
    def __init__(self, radius = 10, clockwise = True):
        self.radius = radius
        self.clockwise = clockwise
        self.points = [(1,1), (3,3), (8,6), (9, 3), (7, -3)]

    def get_states(self):
        outline = []
        states = []
        for x in range(-self.radius, self.radius + 1):
            y = math.ceil((self.radius**2 - x**2)**0.5)
            outline.append((x,y))
            print(f"({x}, {y})")
        
        for x,y in outline:
            for i in range(-y,y+1):
                states.append((x,i))
        states.remove((0,0))
        self.states = states

    def enforce_direction(self, reference_point):
        x,y = abs(reference_point[0]), abs(reference_point[1])
        linePoints = []
        for i in range(-self.radius, self.radius + 1):
            pass

    def individual_area(self, pt1, pt2):
        pt1 = np.array([pt1])
        pt2 = np.array([pt2])
        return np.linalg.norm(pt1 - pt2)
            
    def area(self):
        area = 0
        for i in range(len(self.points)-1):
            area += self.individual_area(self.points[i], self.points[i+1])
        area += self.individual_area(self.points[-1], self.points[0])
        return area
            
a= CircleEnv()
print(a.area())