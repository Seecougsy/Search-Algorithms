import numpy as np
from Stack_class import Stack
from Helpers import is_legal_pos, get_path, offsets, string_to_int_array, find_start, find_goal


# DFS function based on (Andrews, 2023)
def dfs(maze, start, goal):
    stack = Stack()
    stack.push(start)
    predecessors = {start: None}
    traversed = []

    while not stack.is_empty():
        current_cell = stack.pop()
        traversed.append(current_cell)
        if current_cell == goal:
            return get_path(predecessors, start, goal), traversed
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                stack.push(neighbour)
                predecessors[neighbour] = current_cell
    return None, traversed

# # Load maze data and convert immediately
# maze_array_string = np.loadtxt('/Users/calebcougle/PycharmProjects/CAI104_COUGLE_A3/Mazes/a3maze.txt', dtype='str',
#                                delimiter=",")
# maze = string_to_int_array(maze_array_string)
#
# # Plot the original maze without path
#
#
# plot_maze(maze, "Depth first search")
#
# # Search for start point and path
# start_point = find_start(maze)  # Use the integer array 'maze'
# goal_point = find_goal(maze)
#
# # Assuming start and goal are correctly defined elsewhere, or using hard-coded values for example:
# plot_path(maze, start_point, goal_point, solution_path,
#           traversed)  # Ensure 'start_point' and 'goal' are correctly determined
