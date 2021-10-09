'''This is me (Nemynoc) trying to make a pthfinding algorithm, and to create the system that let you try it with a map'''

from sys import argv


class Direction:
    def __init__(self, name, alpha):
        self.name = name
        self.alpha = alpha

    def move(self, location):
        return(location[0]+self.alpha[0], location[1]+self.alpha[1])

UP = Direction("NORTH", (-1, 0))
DOWN = Direction("SOOUTH", (1, 0))
RIGHT = Direction("EAST", (0, 1))
LEFT = Direction("WEST", (0, -1))

class State:
    def __init__(self, size, obstacles, location, cost, action, parent, goal):
        self.size = size
        self.obstacles = obstacles
        self.location = location
        self.cost = cost
        self.action = action
        self.parent = parent
        self.goal = goal

    def successors(self, directions=(UP, DOWN, LEFT, RIGHT)): #generate all the child states from the current state
        childs = []
        for dir_ in directions:
            newLocation = dir_.move(self.location) #new coordinates of the system
            if (newLocation in self.obstacles) or (newLocation[0] not in range(self.size[0] or newLocation[1] not in range(self.location[1]))): continue #bump into an obstacle
            childs.append(State(size=self.size, obstacles=self.obstacles, location=newLocation, cost=self.cost+1, action=dir_, parent=self, goal=self.goal)) #add the new state
        return childs

    def __hash__ (self):
        return(hash(self.location))

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
        print(self.location, self.score())
        map_ = [[' ' for x in range(self.size[1])] for y in range(self.size[0])]

        for (y, x) in self.obstacles: map_[y][x] = '#'
        map_[self.location[0]][self.location[1]] = '@'
        if self.goal == self.location: map_[self.location[0]][self.location[1]] = '+'
        else: map_[self.goal[0]][self.goal[1]] = '.'

        for line in map_:
            print(" ".join(line))


class InvertedPriorityQueue():
    def __init__(self):
        self.queue = []
    
    def insert(self, priority, data):
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
    table = []
    queue = InvertedPriorityQueue()
    queue.insert(model.score(), model) #Insert to the queue the first state
    table.append(model.location)
    while not queue.is_empty(): #if there still is some states to explore
        state = queue.delete()[1] #grab the state with the lowest score
        if state.achieved_state():
            return(state.give_path())
        
        for child in state.successors():
            if child.location in table: continue #security, in order not to explore the same state multiple times
            table.append(child.location)
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
            if lines[l][c] == '#':
                obstacles.append((l, c)) #wall, house, water etc
            elif lines[l][c] == '.':
                goal = (l, c) #goal
            elif lines[l][c] == '@':
                location = (l, c) #system location
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

wM = create_world_model(inputFile) #Parsing the map to create the first world model
wM.draw_state()
location = [wM.goal, wM.location]
bestPath = a_star(wM) #launch A star and search for the best path
if bestPath == None: #no paths
    print("No path could be found")
else:
    print("{}->{} : [{}]".format(location[1], location[0], ", ".join(clean_path(bestPath))))

