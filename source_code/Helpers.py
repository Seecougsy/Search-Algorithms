import numpy as np

from Visualisations import plot_maze

offsets = {
    "right": (0, 1),
    "left": (0, -1),
    "up": (-1, 0),
    "down": (1, 0)
}


# Get path code based on (Andrews, 2023)
def is_legal_pos(maze, pos):
    i, j = pos
    num_rows = len(maze)
    num_cols = len(maze[0])
    return 0 <= i < num_rows and 0 <= j < num_cols and maze[i][j] != 1


# Get path code based on (Andrews, 2023)
def get_path(predecessors, start, goal):
    current = goal
    path = []
    while current != start:
        path.append(current)
        current = predecessors[current]
    path.append(start)
    path.reverse()
    return path


def string_to_int_array(maze_string):
    maze_int = np.where(maze_string == '1', 1, 0)  # Initialize all to 0, set walls to 1
    maze_int[maze_string == '9'] = 9  # Set endpoint
    maze_int[maze_string == '2'] = 2  # Set start point
    return maze_int


def find_start(maze):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == 2:  # Check for integer 2
                return (i, j)
    return None


def find_goal(maze):
    for i, row in enumerate(maze):
        for j, value in enumerate(row):
            if value == 9:  # Check for integer 2
                return (i, j)
    return None


def update_maze_with_path(maze, path, traversed, goal_point, start_point):
    for position in traversed:
        if position != start_point and position != goal_point:
            maze[position[0], position[1]] = 6  # Mark traversed positions
    for position in path:
        if position != start_point and position != goal_point:
            maze[position[0], position[1]] = 4  # Ensure path is marked last
    return maze


def plot_path(maze, start, goal, path, traversed):
    if start and goal:
        if path:
            updated_maze = update_maze_with_path(maze.copy(), path, traversed)
            plot_maze(updated_maze, "Breadth first search: Solution path")
            print("Path:", path)
        else:
            print("No path found.")
    else:
        print("No start point found.")
