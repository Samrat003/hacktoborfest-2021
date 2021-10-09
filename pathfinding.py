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
    def move(self, location, alpha):
        return(location[0]+alpha[0], location[1]+alpha[1])

class State:
    def __init__(self, size, obstacles, location):
        self.size = size
        self.obstacles = obstacles
        self.location = location

    def succesors(self):

