from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap, Normalize


def plot_maze(maze, title="Maze"):
    # Colors: Background, walls, start, end, path, traversed path
    colors = ['#F5F5F5', '#32424A', '#801515', '#27566B', '#55AA55', '#0000FF']
    cmap = ListedColormap(colors)
    norm = Normalize(vmin=0, vmax=len(colors) - 1)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(maze, cmap=cmap, norm=norm)
    ax.set_title(title)
    ax.set_axis_off()
    plt.show()


# def update_maze_with_path(maze, path):
#     for position in path:
#         maze[position[0], position[1]] = 4  # Mark path positions with 4
#     return maze


# def plot_path(maze, start, goal, solution_path, traversed):
#     if start:
#         path = dfs(maze, start, goal)  # Ensure 'maze' is used, which should be the integer array
#         if path:
#             updated_maze = update_maze_with_path(maze.copy(), path)
#             plot_maze(updated_maze, "Depth first search: Solution path")
#             print("Path:", path)
#         else:
#             print("No path found.")
#     else:
#         print("No start point found.")
