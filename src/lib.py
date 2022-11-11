import random

class bcolors:
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
	def __init__(self, maze_dimensions, initial_position, final_position):
		self.MAZE_MAP_DIMENSIONS = maze_dimensions
		self.INITIAL_POSITION = initial_position
		self.FINAL_POSITION = final_position
		valdity_check = self.check_initial_parameters()
		if not valdity_check['valid']:
			raise Exception(valdity_check['error'])
	
	def check_initial_parameters(self):
		if (self.INITIAL_POSITION[0] >= self.MAZE_MAP_DIMENSIONS[0] 
			or self.INITIAL_POSITION[1] >= self.MAZE_MAP_DIMENSIONS[1]):
			err_mesg = 'Initial position is outside the dimensions of the maze map.'
			return {'valid': False, 'error': err_mesg}
		elif (self.FINAL_POSITION[0] >= self.MAZE_MAP_DIMENSIONS[0] 
			or self.FINAL_POSITION[1] >= self.MAZE_MAP_DIMENSIONS[1]):
			err_mesg = 'Initial position is outside the dimensions of the maze map.'
			return {'valid': False, 'error': err_mesg}
		elif self.INITIAL_POSITION == self.FINAL_POSITION:
			err_mesg = 'Final position has to be different from the initial position.'
			return {'valid': False, 'error': err_mesg}
		return {'valid':True}

	def maze_map_index_from_coordinates(self, x, y):
		return self.MAZE_MAP_DIMENSIONS[0]*y + x

	def maze_to_string(self, 
		maze, wall='██', space='  ', 
		color_walls='', color_spaces='', 
		highlighted_cells=[], highlight_color=bcolors.FAIL):
	
		# CONFIG
		# Set colors
		wall = color_walls + wall + bcolors.ENDC
		space = color_spaces + space + bcolors.ENDC
		# Get size of the printed maze
		width = self.MAZE_MAP_DIMENSIONS[0]*2 + 1
		height = self.MAZE_MAP_DIMENSIONS[1]*2 + 1
		# Initialize string maze
		maze_str = ''

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
						box = maze[self.maze_map_index_from_coordinates(x_idx, y_idx)]
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
								ch = highlight_color + space + bcolors.ENDC
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
							ch = highlight_color + ch + bcolors.ENDC
						maze_str += ch
					# 1.3.1.2 Handle first and last columns (always walls) 
					elif j == 0 or j == width-1:
						maze_str += wall
					# 1.2.1.3 Handle odd columns - may be open or closed
					else:
						x_idx = j//2-1
						y_idx = i//2
						box = maze[self.maze_map_index_from_coordinates(x_idx, y_idx)]
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
								ch = highlight_color + space + bcolors.ENDC
						maze_str += ch
				maze_str += '\n'
		return maze_str

	def random_directons():
		return random.shuffle([0, 1, 2, 3])

	def advance(self,curr_x, curr_y):
		directions = self.random_directons()
		for direction in directions:
			pass

	def generate_maze(self):
		return self.maze_map
