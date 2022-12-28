class MazeColors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'

class MazeGenerator:
	DIR_LIST = [0, 1, 2, 3] # N, E, S, W
	CELL_STACK = []
	DEAD_ENDS = []
	SOLUTION = []

	def __init__(self, maze_dimensions, initial_position, final_position):
		self.MAZE_MAP_DIMENSIONS = maze_dimensions
		self.COLUMNS = maze_dimensions[0]
		self.ROWS = maze_dimensions[1]
		self.INITIAL_POSITION = initial_position
		self.INITIAL_X = initial_position[0]
		self.INITIAL_Y = initial_position[1]
		self.FINAL_POSITION = final_position
		self.FINAL_X = final_position[0]
		self.FINAL_Y = final_position[1]
		self.init_maze()
		valdity_check = self.check_initial_parameters()
		if not valdity_check['valid']:
			raise Exception(valdity_check['error'])
	
	def init_maze(self):
		# MAZE = [# (E, S)
		#     (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
		#     (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
		#     (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), ('', 1), 
		#     (1, ''), (1, ''), (1, ''), (1, ''), (1, ''), ('', '')
		# ]
		self.MAZE = [# (E, S)
			(1, 1) for i in range(self.COLUMNS*self.ROWS)
		]

	def check_initial_parameters(self):
		if (self.INITIAL_X >= self.COLUMNS 
			or self.INITIAL_Y >= self.ROWS):
			err_mesg = 'Initial position is outside the dimensions of the maze map.'
			return {'valid': False, 'error': err_mesg}
		elif (self.FINAL_X >= self.COLUMNS 
			or self.FINAL_Y >= self.ROWS):
			err_mesg = 'Initial position is outside the dimensions of the maze map.'
			return {'valid': False, 'error': err_mesg}
		elif self.INITIAL_POSITION == self.FINAL_POSITION:
			err_mesg = 'Final position has to be different from the initial position.'
			return {'valid': False, 'error': err_mesg}
		return {'valid':True}

	def maze_map_index_from_coordinates(self, x, y):
		return self.COLUMNS*y + x

	def maze_to_string(self, 
		wall='██', space='  ', 
		color_walls='', color_spaces='', 
		highlighted_cells=[], highlight_color=MazeColors.FAIL,
		show_solution=False):
	
		# CONFIG
		# Set colors
		wall = color_walls + wall + MazeColors.ENDC
		space = color_spaces + space + MazeColors.ENDC
		# Get size of the printed maze
		width = self.COLUMNS*2 + 1
		height = self.ROWS*2 + 1
		# Initialize string maze
		maze_str = ''
		# If show_solution is set to TRUE, override
		# other cell highlights
		if show_solution:
			highlighted_cells = self.SOLUTION

		# CONVERT MAZE TO STRING
		# 1. Iterate over the rows
		for i in range(height):
			# 1.1 Handle first and last rows
			if i == 0 or i == height - 1:
				maze_str += wall*width + '\n'
			# 1.2 Handle even index rows (rows with no cells)
			elif i%2 == 0:
				# 1.2.1 Iterate over the columns
				for j in range(width):
					# 1.2.1.1 Handle the even columns - wall intersections are always walls
					if j%2 == 0:
						maze_str += wall
					# 1.2.1.2 Handle odd columns - may be open or closed
					else:
						x_idx = j//2
						y_idx = i//2-1
						box = self.MAZE[self.maze_map_index_from_coordinates(x_idx, y_idx)]
						if box[1]: 
							ch = wall
						else: 
							ch = space
							# If the wall is open and surrounding cells are highlighted,
							# highlight the space also
							if (
								(x_idx, y_idx) in highlighted_cells
								and 
								(x_idx, y_idx + 1) in highlighted_cells
								):
								ch = highlight_color + space + MazeColors.ENDC
						maze_str += ch
				maze_str += '\n'
			# 1.3 Handle odd index rows (rows with cells)
			else:
				# 1.3.1 Iterate over the columns
				for j in range(width):
					# 1.3.1.1 Handle the odd columns - cells are always spaces
					if j%2 != 0:
						ch = space
						x_idx = j//2
						y_idx = i//2                    
						if (x_idx, y_idx) in highlighted_cells:
							ch = highlight_color + ch + MazeColors.ENDC
						maze_str += ch
					# 1.3.1.2 Handle first and last columns (always walls) 
					elif j == 0 or j == width-1:
						maze_str += wall
					# 1.2.1.3 Handle odd columns - may be open or closed
					else:
						x_idx = j//2-1
						y_idx = i//2
						box = self.MAZE[self.maze_map_index_from_coordinates(x_idx, y_idx)]
						if box[0]:
							ch = wall
						else:
							ch = space
							# If the wall is open and surrounding cells are highlighted,
							# highlight the space also
							if (
								(x_idx, y_idx) in highlighted_cells
								and 
								(x_idx + 1, y_idx) in highlighted_cells
								):
								ch = highlight_color + space + MazeColors.ENDC
						maze_str += ch
				maze_str += '\n'
		return maze_str

	def random_directons(self):
		import random
		random.shuffle(self.DIR_LIST)
		return self.DIR_LIST

	def check_advance_direction(self, curr_x, curr_y, direction):
		if direction == 0: # North
			new_x, new_y = curr_x, curr_y - 1
			# First check bounds
			if new_y < 0 or new_y > self.ROWS-1:
				return False, None, None
			# Then check if visited
			if (new_x, new_y) in self.CELL_STACK + self.DEAD_ENDS:
				return False, None, None
			# Then check walls
			north_wall = self.MAZE[self.maze_map_index_from_coordinates(new_x,new_y)][1]
			if not north_wall:
				return False, None, None
			return True, new_x, new_y
		elif direction == 1: # East
			new_x, new_y = curr_x + 1, curr_y
			# First check bounds
			if new_x < 0 or new_x > self.COLUMNS-1:
				return False, None, None
			# Then check if visited
			if (new_x, new_y) in self.CELL_STACK + self.DEAD_ENDS:
				return False, None, None
			# Then check walls
			east_wall = self.MAZE[self.maze_map_index_from_coordinates(curr_x,curr_y)][0]
			if not east_wall:
				return False, None, None
			return True, new_x, new_y
		elif direction == 2: # South
			new_x, new_y = curr_x, curr_y + 1
			# First check bounds
			if new_y < 0 or new_y > self.ROWS-1:
				return False, None, None
			# Then check if visited
			if (new_x, new_y) in self.CELL_STACK + self.DEAD_ENDS:
				return False, None, None
			# Then check walls
			south_wall = self.MAZE[self.maze_map_index_from_coordinates(curr_x,curr_y)][1]
			if not south_wall:
				return False, None, None
			return True, new_x, new_y
		elif direction == 3: # West
			new_x, new_y = curr_x - 1, curr_y
			# First check bounds
			if new_x < 0 or new_x > self.COLUMNS-1:
				return False, None, None
			# Then check if visited
			if (new_x, new_y) in self.CELL_STACK + self.DEAD_ENDS:
				return False, None, None
			# Then check walls
			west_wall = self.MAZE[self.maze_map_index_from_coordinates(new_x,new_y)][0]
			if not west_wall:
				return False, None, None
			return True, new_x, new_y
		raise Exception(f'Invalid direction: {str(direction)}')

	def set_wall(self, curr_x, curr_y, direction, value=1):
		if direction == 0: # North
			new_x, new_y = curr_x, curr_y - 1
			i = self.maze_map_index_from_coordinates(new_x,new_y)
			self.MAZE[i] = (self.MAZE[i][0], value)
		elif direction == 1: # East
			# new_x, new_y = curr_x + 1, curr_y
			i = self.maze_map_index_from_coordinates(curr_x,curr_y)
			self.MAZE[i] = (value, self.MAZE[i][1])
		elif direction == 2: # South
			# new_x, new_y = curr_x, curr_y + 1
			i = self.maze_map_index_from_coordinates(curr_x,curr_y)
			self.MAZE[i] = (self.MAZE[i][0], value)
		elif direction == 3: # West
			new_x, new_y = curr_x - 1, curr_y
			i = self.maze_map_index_from_coordinates(new_x,new_y)
			self.MAZE[i] = (value, self.MAZE[i][1])
		else:
			raise Exception(f'Invalid direction: {str(direction)}')

	def remove_wall(self, curr_x, curr_y, direction):
		self.set_wall(curr_x, curr_y, direction, value=0)

	def add_wall(self, curr_x, curr_y, direction):
		self.set_wall(curr_x, curr_y, direction, value=1)

	def print_maze_step(self, pause=False):
		visited = [cell for cell in self.CELL_STACK + self.DEAD_ENDS]
		str_maze = self.maze_to_string(space='██', color_walls=MazeColors.OKBLUE, highlight_color=MazeColors.FAIL, highlighted_cells=self.CELL_STACK)
		print(str_maze)
		if pause:
			input('Press Enter to continue')

	def add_stack_cell(self, coords):
		if coords not in self.CELL_STACK:
			self.CELL_STACK.append(coords)
	
	def remove_stack_cell(self, coords):
		self.CELL_STACK = [c for c in self.CELL_STACK if c!=coords]

	def add_dead_end(self, coords):
		if coords not in self.DEAD_ENDS:
			self.DEAD_ENDS.append(coords)
	
	def remove_dead_end(self, coords):
		self.DEAD_ENDS = [c for c in self.DEAD_ENDS if c!=coords]

	def advance(self, curr_x, curr_y, verbose=False, pause=False, log=False):
		directions = self.random_directons()
		if verbose: self.print_maze_step(pause=pause)
		for direction in directions:
			can_advance, new_x, new_y = self.check_advance_direction(curr_x, curr_y, direction)
			if can_advance:
				msg = f'Advancing from ({curr_x}, {curr_y}) to ({new_x}, {new_y})'
				if verbose: print(msg)
				if log: 
					with open(log, 'a') as f: f.write(msg + '\n')
				self.add_stack_cell((new_x, new_y))
				self.remove_wall(curr_x, curr_y, direction)
				return self.advance(new_x, new_y, verbose=verbose, pause=pause, log=log)
		if verbose: print(f'Cannot advance... backtracking')
		return self.backtrack(curr_x, curr_y, verbose=verbose, pause=pause, log=log)
	
	def backtrack(self, curr_x, curr_y, verbose=False, pause=False, log=False):
		if (curr_x, curr_y) == self.FINAL_POSITION:
			self.SOLUTION = self.CELL_STACK + [self.FINAL_POSITION]
		if verbose: self.print_maze_step(pause=pause)
		current_cell = (curr_x, curr_y)
		del self.CELL_STACK[-1]
		if not self.CELL_STACK:
			return self.MAZE
		self.add_dead_end(current_cell)
		self.remove_stack_cell(current_cell)
		previous_cell = self.CELL_STACK[-1]
		msg = f'Backtracking from ({curr_x}, {curr_y}) to ({previous_cell[0]}, {previous_cell[1]})'
		if verbose: print(msg)
		if log: 
			with open(log, 'a') as f: f.write(msg + '\n')
		return self.advance(previous_cell[0], previous_cell[1], verbose=verbose, pause=pause, log=log)

	def generate_maze(self, verbose=False, pause=False, log=False):
		if log: 
			with open(log, 'w') as f:
				f.write('GENERATION LOG:\n')

		self.add_stack_cell(self.INITIAL_POSITION)
		maze = self.advance(self.INITIAL_X, self.INITIAL_Y, verbose=verbose, pause=pause, log=log)
		return maze
