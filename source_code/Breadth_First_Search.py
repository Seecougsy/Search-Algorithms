from FIFO_class import Fifo
from Helpers import get_path, is_legal_pos, offsets


# Code based on (Andrews, 2023)


def bfs(maze, start, goal):
    # create an instance of the class FIFO
    # Load the inital state into the class
    queue = Fifo()
    queue.enqueue(start)

    # DICT maps the relationsip parent/ child node
    predecessors = {start: None}
    # Lists visted to return for visualisation
    traversed = []  # List to keep track of all traversed cells

    # while there is something in the queue
    while not queue.is_empty():
        current_cell = queue.dequeue()  #<-- current sell is the first item off the list
        traversed.append(current_cell)  # Record the traversed cell

        if current_cell == goal:  # <-- Goal check
            return get_path(predecessors, start, goal), traversed  #<-- return the results if goal
        for direction in ["up", "right", "down", "left"]:  #<-- Keys that contain legal actions (offest)
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            if is_legal_pos(maze, neighbour) and neighbour not in predecessors:  # <-- check that the move is legal,
                # and the nodes haven't been visited before
                queue.enqueue(neighbour)  #<-- add neighbour to queue
                predecessors[neighbour] = current_cell
    return None, traversed  # Return None for path if no path found and the list of traversed cells
