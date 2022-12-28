# Python Backtracking Maze Generator

This repo hosts a recursive backtracking maze generator implemented in `python`. The algorithm (**Randomized depth-first search**) is explained in [this](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_depth-first_search) Wikipedia article.

## Usage

The generator is implemented as a class named `MazeGenerator`. In order to generate a maze, the first step would be to create an instance of the generator, by giving it the size of the maze (`(columns, rows)`) that you would like to generate and the initial/final positions of the maze.

```python
from lib import MazeGenerator
MAZE_MAP_DIMENSIONS = (20, 20)
INITIAL_POSITION = (19, 0)
FINAL_POSITION = (0, 19)

mg = MazeGenerator(
    maze_dimensions=MAZE_MAP_DIMENSIONS,
    initial_position=INITIAL_POSITION,
    final_position=FINAL_POSITION
)
```

This will create a $20\times20$ maze with the start at the top right and the end at the bottom left of the maze.

Once that is done, you can generate the maze by invoking the `generate_maze` method of the generator:

```python
# Generate the maze
maze = mg.generate_maze()
```
This returns a list of `columns * rows` two-element tuples representing the maze. Each tuple represents one of the cells, and the corresponding tuple elements represent if that cell has a wall on its east (`1` means wall, `0` means no wall) and on its south. Thus, the whole maze is defined.

As the output format is slightly complicated to visualize, you can print the maze to the terminal in readable format like this:

```python
# Convert the current maze to a printable string
maze_str = mg.maze_to_string()
print(maze_str)
```
Both of these methods have several optional arguments that will be explained in the following sections.

### `MazeGenerator.maze_to_string`

The optional parameters of this function can be used to customize the way in which the maze is displayed:

* `wall` (defaults to `'██'`): This parameter determines the sequence of characters that are used to represent a maze wall.
* `space` (defaults to `'  '`): This is the set of characters used to represent a maze space.
* `color_walls` (defaults to `''`): This determines the color of the walls. The color can be chosen from the class `MazeColors` also defined in the same file as the `MazeGenerator`.
* `color_spaces` (defaults to `''`): This is the color of the maze spaces.
* `highlighted_cells` (defaults to `[]`): The function admits highlighting of a specific set of cells in a certain color. The cell coordinates should be passed as a list of `(x, y)` tuples in this parameter.
* `highlight_color` (defaults to `MazeColors.FAIL`): color of the highlighted cells.
* `highlight_char` (defaults to `'██'`): characters used to represent a highlighted space.
* `show_solution` (defaults to `False`): If this parameter is set to `True`, the `highlighted_cells` parameter is overriden by the solution to the generated maze.

    ```python
    # Convert the current maze to a printable string and highlight the solution
    maze_str_sol = mg.maze_to_string(show_solution=True)
    print(maze_str_sol)
    ```
### `MazeGenerator.generate_maze`

The function `generate_maze` also has some optional parameters that can be used to customize how it behaves:

* `print_steps` (defaults to `False`): If set to `True`, the maze is printed at every advance/backtrack step with the current cell stack highlighted in red.
* `pause` (defaults to `False`): This parameter is only relevant when `print_steps` is `True`. If set to `True`, it causes the program to pause at each advance/backtrack step, right after printing the maze at that step. The program only continues after the user has pressed enter.
* `log` (defaults to `False`): If set to a string containing a filename (for example, `'log.txt'`), a file is created with that name containing each step of the maze generation process.
* The following properties are the same as in `MazeGenerator.maze_to_string`, and they are used to customize the maze printed at each step: `wall`, `space`, `color_walls`, `color_spaces`, `highlight_color` and `highlight_char`.

```python
# Generate the maze, pausing, printing the maze and logging to `log.txt` at every step
maze = mg.generate_maze(
    print_steps=True,
    log='log.txt',
    pause=True
)
```
## References

See also [Recursive VS Iterative Dynamic Backtracking Maze Generator with C++](https://github.com/jbarciv/Backtracking-Maze-Generator).
