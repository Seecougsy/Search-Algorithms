import numpy as np

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


