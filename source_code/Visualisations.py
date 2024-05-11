from matplotlib import pyplot as plt
from matplotlib.colors import ListedColormap, Normalize
from Depth_First_Search import dfs


def plot_maze(maze, title="Maze"):
    colors = ['#F5F5F5', '#32424A', '#801515', '#27566B', '#55AA55']  # Background, walls, start, end, path
    cmap = ListedColormap(colors)
    norm = Normalize(vmin=0, vmax=len(colors) - 1)
    fig, ax = plt.subplots(figsize=(5, 5))
    ax.imshow(maze, cmap=cmap, norm=norm)
    ax.set_title(title)
    ax.set_axis_off()
    plt.show()


def update_maze_with_path(maze, path):
    for position in path:
        maze[position[0], position[1]] = 4  # Mark path positions with 4
    return maze


def plot_path(maze, start, goal):
    if start:
        path = dfs(maze, start, goal)  # Ensure 'maze' is used, which should be the integer array
        if path:
            updated_maze = update_maze_with_path(maze.copy(), path)
            plot_maze(updated_maze, "Depth first search: Solution path")
            print("Path:", path)
        else:
            print("No path found.")
    else:
        print("No start point found.")
