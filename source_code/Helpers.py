import numpy as np
'''
These are functions that assist in the function of the algoritms
'''
from Visualisations import plot_maze

# Dict that manages the possible legal actions
# It performs an operations on the index of the current node
offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}



# Checks if the action is legal (Andrews, 2023)

def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze) #<-- doesnt exceed length of rows
    num_cols = len(maze[0]) #<-- or columns
    # Below checks within boundaries and that the node is not a wall
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != 1


# Get path code based on (Andrews, 2023)
def get_path(predecessors, start, goal):
    # Initialize the goal set to current node
    current = goal
    # Create an empty list to store the path
    path = []

    # Loop until intial state
    while current != start:
        # Append  current node to the  list
        path.append(current)
        # Set redecessor of the current node.
        current = predecessors[current]

    # add initial state to node to the path.
    path.append(start)
    # Reverse the path to show it from start to goal.
    path.reverse()
    # Return the completed path.
    return path


# Convert string to int in array
def string_to_int_array(maze_string):
    maze_int = np.where(maze_string == '1', 1, 0)  # Initialize all to 0, set walls to 1
    maze_int[maze_string == '9'] = 9  # Set endpoint
    maze_int[maze_string == '2'] = 2  # Set start point (I changed form -1 — sorry! it was annoying to have the -
    # symbol)
    return maze_int


# Find the start of maze
# This is for scalability to load more mazes.
def find_start(maze):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == 2:  # Check for integer 2
                return (i, j) #<-- return index
    return None

# Find the goal
# This is for scalability to load more mazes.
def find_goal(maze):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == 9:  # Check for integer 9
                return (i, j)
    return None


''' Pass in the maze, the solution path, the traversed nodes list, the start and end point to plot on graph
'''
def update_maze_with_path(maze, path, traversed, maze_start_point, maze_goal_point):
    new_maze = maze.copy()
    for position in traversed:
        if position != maze_start_point and position != maze_goal_point:
            new_maze[position[0], position[1]] = 6  # Mark traversed positions
    for position in path:
        if position != maze_start_point and position != maze_goal_point:
            new_maze[position[0], position[1]] = 4  # Ensure path is marked last
    return new_maze # <-- return the new maze

