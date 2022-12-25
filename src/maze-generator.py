from lib import MazeGenerator
import sys
sys.setrecursionlimit(1000000)

MAZE_MAP_DIMENSIONS = (40, 16)
INITIAL_POSITION = (0, 0)
FINAL_POSITION = (0, 1)

# maze_map = [# (E, S)
#     (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
#     (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
#     (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
#     (1, ''), (1, ''), (1, ''), (1, ''), (1, ''), ('', '')
# ]

position_buffer = [INITIAL_POSITION]


def main():
    mg = MazeGenerator(
        maze_dimensions=MAZE_MAP_DIMENSIONS,
        initial_position=INITIAL_POSITION,
        final_position=FINAL_POSITION
    )
    mg.generate_maze(verbose=True, pause=True)
    print(mg.maze_to_string())

    # print(mg.maze_to_string(
    #     space='██', 
    #     color_walls=bcolors.OKBLUE, 
    #     highlighted_cells=[(0, 0),(0, 1),(0, 2),(5, 3),(2, 1),(2, 3),(2, 2),(5, 2),(4, 3),]
    #     ))

if __name__=='__main__':
    main()