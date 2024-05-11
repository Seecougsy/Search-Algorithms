from FIFO_class import Fifo
from Helpers import get_path, is_legal_pos, offsets


# Code based on (Andrews, 2023)
def bfs(maze, start, goal):
    queue = Fifo()
    queue.enqueue(start)
    predecessors = {start: None}
    traversed = []  # List to keep track of all traversed cells

    while not queue.is_empty():
        current_cell = queue.dequeue()
        traversed.append(current_cell)  # Record the traversed cell

        if current_cell == goal:
            return get_path(predecessors, start, goal), traversed
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:
                queue.enqueue(neighbour)
                predecessors[neighbour] = current_cell
    return None, traversed  # Return None for path if no path found and the list of traversed cells
