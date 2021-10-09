'''This is me (Nemynoc) trying to make a pthfinding algorithm, and to create the system that let you try it with a map'''

from sys import argv


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
            childs.append(State(size=self.size, obstacles=self.obstacles, location=newLocation, cost=self.cost+1, action=dir_, parent=self, goal=self.goal, path=self.path)) #add the new state
        return childs
    
    def __eq__ (self, other):
        return(self.location == other.location)

    def score(self):
        return(self.cost + abs(self.location[0] - self.goal[0]) + abs(self.location[1] - self.goal[1]))

    def give_path(self):
        truePath = []
        p = self
        while p.action != None:
            truePath.insert(0, p.action)
            p = p.parent
        return(truePath)

    def achieved_state(self):
        return(self.location == self.goal)
    
    def draw_state(self):
        map_ = [[' ' for x in range(self.size[1])] for y in range(self.size[0])]

        for (y, x) in self.obstacles: map_[y][x] = '#'
        map_[self.location[0]][self.location[1]] = '@'
        if self.goal == self.location: map_[self.location[0]][self.location[1]] = '+'
        else: map_[self.goal[0]][self.goal[1]] = '.'


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

    while not queue.is_empty():
        state = queue.delete()

        if state.achievedState():
            return(state.path)
        
        for child in state.successors():
            queue.insert(child.score(), child)
        
    return(None)

def create_world_model(inputFile): #input file parsing to create the initial world model
    obstacles = []
    location = ()
    goal = ()
    size = [0, 0]
    with open(inputFile, mode='r', encoding="utf-8") as f:
        lines = f.readlines()
        size[0] = len(lines) #get the map size (height)

    for l in range(len(lines)):
        if size[1] < len(lines[l]): size[1] = len(lines[1]) #get the max size of the map (weidth)
        for c in range(len(lines[l])):
            if lines[l][c] == '#': obstacles.append((l, c)) #wall, house, water etc
            elif lines[l][c] == '.': goal = (l, c) #goal
            elif lines[l][c] == '@': location = (l, c) #system location
            elif lines[l][c] == '+': #system on the goal
                location = (l, c)
                goal = (l, c)
            if(goal == () or location == ()): raise ValueError("You need to specifiy 1 goal and 1 system position in the map")
    
    return(State(size=size, obstacles=obstacles, location = location, cost=0, action=None, parent=None, goal=goal))

def clean_path(path):
    cleanPath = []
    for i in path:
        cleanPath.append(i.name)
    return(cleanPath)


##### Treatment pipeline
try:
    inputFile = argv[1]
except IndexError:
    inputFile = None

wM = create_world_model(inputFile)
location = [wM.goal, wM.location]
bestPath = a_star(wM)
if bestPath == None:
    print("No path would be found")
else:
    print("{}->{} : [{}]".format(location[1], location[0], ", ".join(bestPath)))

