##########################
# Program 2 Mazes
# Daniel Jaffe
# Date Created: 7/12/24
##########################

# pip install --upgrade --force-reinstall git+https://github.com/jgourd/CSC201UT

from CSC201UT import MazeUtils


# Maze Class
class Maze:
  def __init__(self, item = None):
    self._item = item
    self._N = None
    self._S = None
    self._W = None
    self._E = None


#######
# MAIN
#######

# don't change it once you've begun to explore your maze
# (you might get a different maze and invalidate all of your hard work)
#Ask user for name
YOUR_NAME = "Daniel Jaffe"

# change these constants so that they contain the paths out of your maze and labyrinth
PATH_OUT_OF_MAZE = "SENEESWSESNWWSW"
PATH_OUT_OF_LABYRINTH = "SNSWWSWNEW"

startLocation = MazeUtils.mazeFor(YOUR_NAME)

# *******************************************************
# set a breakpoint on the next line to explore your maze!
if (MazeUtils.isPathToFreedom(startLocation, PATH_OUT_OF_MAZE)):
  print("Congratulations! You've found everything that's hidden in the maze.")
else:
  print("Sorry, but you haven't found everything that's hidden in the maze.")

startLocation = MazeUtils.labyrinthFor(YOUR_NAME)

# ************************************************************
# set a breakpoint on the next line to explore your labyrinth!
if (MazeUtils.isPathToFreedom(startLocation, PATH_OUT_OF_LABYRINTH)):
  print("Congratulations! You've found everything that's hidden in the labyrinth.")
else:
  print("Sorry, but you haven't found everything that's hidden in the labyrinth.")
