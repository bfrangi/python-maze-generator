from lib import MazeColors, MazeGenerator
import sys
sys.setrecursionlimit(1000000)

MAZE_MAP_DIMENSIONS = (20, 20)
INITIAL_POSITION = (19, 0)
FINAL_POSITION = (0, 19)


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

    # Generate the maze, pausing, printing the maze and logging 
    # to `log.txt` at every step
    maze = mg.generate_maze(
        print_steps=True,
        log='log.txt',
        pause=True
    )

    # Convert the current maze to a printable string
    # maze_str = mg.maze_to_string(
    #     space='██',
    #     color_walls=MazeColors.OKBLUE,
    #     show_solution=True
    # )
    # print(maze_str)

    # Convert the current maze to a printable string and highlight
    # the solution
    # maze_str_solved = mg.maze_to_string(
    #     space='██',
    #     color_walls=MazeColors.OKBLUE,
    # )
    # print(maze_str_solved)


if __name__ == '__main__':
    main()
