'''This is me (Nemynoc) trying to make a pthfinding algorithm, and to create the system that let you try it with a map'''

from sys import argv

try:
    inputFile = argv[1]
except IndexError:
    inputFile = None


class Direction:
    def __init__(self, name, alpha):
        self.name = name
        self.alpha = alpha

    def move(self, location):
        return(location[0]+self.alpha[0], location[1]+self.alpha[1])




class State:
    def __init__(self, size, obstacles, location, cost, action, parent, goal):
        self.size = size
        self.obstacles = obstacles
        self.location = location
        self.cost = cost
        self.action = action
        self.parent = parent
        self.goal = goal

    def succesors(self, directions): #generate all the child states from the current state
        childs = []
        for dir_ in directions:
            newLocation = dir_.move(self.location) #new coordinates of the system

            if newLocation in self.obstacles: continue #bump into an obstacle
            elif newLocation == self.parent.location: continue #revert the last action

            childs.append(State(size=self.size, obstacles=self.obstacles, location=newLocation, cost=self.cost+1, action=dir_, parent=self, goal=self.goal)) #add the new state
    
    def __eq__ (self, other):
        return(self.location == self.location)

    def score(self):
        return(self.cost + abs(self.location[0] - self.goal[0]) + abs(self.location[1] - self.goal[1]))

class InvertedPriorityQueue():
    def __init__(self):
        self.queue = []
    
    def insert(self, data, priority):
        self.queue.append([priority, data])
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def delete(self):
        if self.is_empty(): return []
        else:
            min_ = 0
            for i in range(len(self.queue)):
                if self.queue[i][0] < self.queue[min_][0]:
                    min_ = i
            item = self.queue[min_]
            del self.queue[min_]
            return item

def a_star(model: State):
    queue = InvertedPriorityQueue()
    queue.insert(model.score(), model) #Insert to the queue the first state






