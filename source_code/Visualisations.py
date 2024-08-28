# Import necessary components from matplotlib
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap, Normalize


def plot_maze(maze, title="Maze"):
    #   '#F5F5F5' - Background
    #   '#32424A' - Walls
    #   '#801515' - Start
    #   '#27566B' - goal position
    #   '#55AA55' - Path
    #   '#0000FF' - Traversed
    colors = ['#F5F5F5', '#32424A', '#801515', '#27566B', '#55AA55', '#0000FF']

    # color map from the list of colors
    cmap = ListedColormap(colors)

    norm = Normalize(vmin=0, vmax=len(colors) - 1)

    # specified size
    fig, ax = plt.subplots(figsize=(5, 5))

    ax.imshow(maze, cmap=cmap, norm=norm)

    # Set the title of the plot
    ax.set_title(title)

    # remove axes
    ax.set_axis_off()

    # show
    plt.show()
