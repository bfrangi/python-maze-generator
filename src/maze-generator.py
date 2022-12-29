from lib import MazeColors, MazeGenerator
import sys
sys.setrecursionlimit(1000000)

MAZE_MAP_DIMENSIONS = (34, 15)
INITIAL_POSITION = (0, 0)
FINAL_POSITION = (33, 14)


def main():
    # Initialize generator
    mg = MazeGenerator(
        maze_dimensions=MAZE_MAP_DIMENSIONS,
        initial_position=INITIAL_POSITION,
        final_position=FINAL_POSITION
    )

    # Generate the maze
    maze = mg.generate_maze()

    # Convert the current maze to a printable string
    maze_str = mg.maze_to_string()
    print(maze_str)

    # Convert the current maze to a printable string and highlight 
    # the solution
    maze_str_sol = mg.maze_to_string(show_solution=True)
    print(maze_str_sol)

if __name__ == '__main__':
    main()
