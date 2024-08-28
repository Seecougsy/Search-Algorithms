import numpy as np
from Stack_class import Stack
from Helpers import is_legal_pos, get_path, offsets, string_to_int_array, find_start, find_goal
import numpy as np
from Stack_class import Stack
from Helpers import is_legal_pos, get_path, offsets, string_to_int_array, find_start, find_goal

# DFS function based on (Andrews, 2023)
def dfs(maze, start, goal):
    # initialize the stack with the start
    stack = Stack()
    stack.push(start)

    # maps relationships of nodes parent/child
    predecessors = {start: None}

    # List to record traversed nodes
    traversed = []

    # Continue until stack is empty
    while not stack.is_empty():
        current_cell = stack.pop()
        traversed.append(current_cell)

        # Check if goal is reached
        if current_cell == goal:
            return get_path(predecessors, start, goal), traversed

        # Explore neighbors in legal possible actions directions
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)

            # Push legal and unvisited to stack
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                stack.push(neighbour)
                predecessors[neighbour] = current_cell

    # Return None and traversed path if no path is found
    return None, traversed
