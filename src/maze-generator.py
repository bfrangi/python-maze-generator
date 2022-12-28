from lib import bcolors, MazeGenerator
import sys
sys.setrecursionlimit(1000000)

MAZE_MAP_DIMENSIONS = (60, 30)
INITIAL_POSITION = (0, 0)
FINAL_POSITION = (59, 29)


def main():
    mg = MazeGenerator(
        maze_dimensions=MAZE_MAP_DIMENSIONS,
        initial_position=INITIAL_POSITION,
        final_position=FINAL_POSITION
    )
    mg.generate_maze(
        verbose=False,
        pause=True
        )

    print(mg.maze_to_string(
        space='██', 
        color_walls=bcolors.OKBLUE,
        show_solution=True
        ))

    print(mg.maze_to_string(
        space='██', 
        color_walls=bcolors.OKBLUE,
        ))

if __name__=='__main__':
    main()