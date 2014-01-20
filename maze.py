#maze 2.0 ;)
from random import randint


class Maze(object):
	'''
	A maze is made up of cells. 
	We will give it a list of lists
	where the entire list represents
	a maze and the internal lists will
	represent rows containing the cells
	'''
	def __init__(self, row_list):
		self.rows = row_list

	def print_maze(self):
		#stores all the n/e/s/w walls in temp lists for printing
		for row in self.rows:
			self.first, self.second, self.third = [], [], []
			
			for cell in row:
			
				self.first.append(cell.north)
				
				self.second.append(cell.west)
				self.second.append(cell.east)
				
				self.third.append(cell.south)
				
			print "".join(self.first)
			print "".join(self.second)
			print "".join(self.third)
		
	def set_start(self):
		#randomizes the starting cell on the top or bottom
		
		start_col = randint(0,WIDTH-1)

		if randint(0,1) == 0:
			start_cell = self.rows[0][start_col]
			start_cell.walls[0] = 0 #north wall disabled
		
		else:
			start_cell = self.rows[HEIGHT-1][start_col]
			start_cell.walls[2] = 0 #south wall disabled
			
		start_cell.visited = True
		start_cell.set_walls()
		
		return start_cell
		
	def set_end(self, start):
		#randomizes the ending cell opposite of the start
		
		end_col = randint(0, WIDTH-1)
		
		if start.y == 0:
			end_cell = self.rows[HEIGHT-1][end_col]
			end_cell.walls[2] = 0
			
		elif start.y == HEIGHT-1:
			end_cell = self.rows[0][end_col]
			end_cell.walls[0] = 0
		
		end_cell.set_walls()
		
		return end_cell
			
	def get_moves(self, cell):
		#function that checks surrounding cells to see if they have been visited. If 
		#they have not, it will change the flag for the appropriate move (n, e, s, w)
		
		moves = [0, 0, 0, 0] #initialize at no possible movements
		
		if cell.y != 0: #check north
			if not self.rows[cell.y-1][cell.x].visited:
				moves[0] = 1
				
		if cell.x != WIDTH-1: #check east
			if not self.rows[cell.y][cell.x+1].visited:
				moves[1] = 1
				
		if cell.y != HEIGHT-1: #check south
			if not self.rows[cell.y+1][cell.x].visited:
				moves[2] = 1	
				
		if cell.x != 0: #check west
			if not self.rows[cell.y][cell.x-1].visited:
				moves[3] = 1
			
		return moves
	
	def random_direction(self, moves):
		#attempt to increase randomness in picking the direction. Each direction gets a
		#'roll'. The rolls are compared and the highest 'wins'
		
		rolls = []
		
		for i in range(4):
		
			if moves[i] == 1: #if you can move in this direction
				roll = randint(1, 100)
				rolls.append(roll)
				
			else: #if you can't move that way, make it a 0 so it can't win the roll
				rolls.append(0)
				
		return rolls.index(max(rolls))
		
	def check_unvisited(self, the_rows):
		#are there any remaining unvisited cells in the maze?
		for row in the_rows:
			for cell in row:
				if cell.visited == False:
					return True
		return False			 
							
	def move(self, cell):
		#Determine the move direction and the next cell. It adds the cell to the
		#'stack' (path) if there's a move and sets it to visited. If there are no moves
		#then it pops the current cell off the stack.
		moves = self.get_moves(cell)
			
		if moves.count(1) > 0:
			direct = self.random_direction(moves)
		
			if direct == 0: #north
				new_cell = self.rows[cell.y - 1][cell.x]
				cell.walls[0] = 0
				new_cell.walls[2] = 0
				
			elif direct == 1: #east
				new_cell = self.rows[cell.y][cell.x + 1]
				cell.walls[1] = 0
				new_cell.walls[3] = 0
				
			elif direct == 2: #south
				new_cell = self.rows[cell.y + 1][cell.x]
				cell.walls[2] = 0
				new_cell.walls[0] = 0
				
			elif direct == 3: #west
				new_cell = self.rows[cell.y][cell.x - 1]
				cell.walls[3] = 0
				new_cell.walls[1] = 0

			path.append(new_cell)
			new_cell.visited = True
			cell.set_walls()
			new_cell.set_walls()
		else:
			path.pop()			
	
	def generate_maze(self, start):
		#makes the path through the maze
		global path
		path = [start] #initialize the path

		while self.check_unvisited(myMaze.rows): #while unvisited cells remain...
			self.move(path[-1]) #call the move method on the last cell on the stack

		self.set_end(start)
			
			
			
class Cell(object):
	'''
	A cell is an object with a north, east, south, and west wall.
	It is given an x and y coordinate to identify and locate it within
	a list of cells. It has a 'visited' flag.
	'''
	def __init__(self, x, y, walls=[1, 1, 1, 1], visited=False):
		self.walls = walls #True = wall enabled, False = disabled
		self.x = x
		self.y = y
		self.visited  = visited
		self.set_walls() #Initialize all the walls
		
		
	def set_walls(self):
		#sets all walls based on the wall list flags
		#[N, E, S, W]; 1 = Enabled, 0 = Disabled
		
		if self.walls[0]: self.north = '+=+'
		else: self.north = '+ +'
			
		if self.walls[1]: self.east = ' |'
		else: self.east = '  '

		if self.walls[2]: self.south = '+=+' 
		else: self.south = '+ +'
			
		if self.walls[3]: self.west = '|'
		else: self.west = ' '
		

def make_cells():
	#generates rows of cells as lists and combines those into one 
	#master 'maze' list
	maze = []
	ypos = 0
	
	for i in range(HEIGHT):
		#starts a new row (height)
		row = []
		xpos = 0
		
		for i in range(WIDTH):
		#starts a new column(width)
			walls = [1, 1, 1, 1]
			temp_cell = Cell(xpos, ypos, walls)
			row.append(temp_cell)
			
			xpos += 1
			
		ypos += 1
		maze.append(row)
	return maze

def make_maze():
	start = myMaze.set_start()
	myMaze.generate_maze(start)
	myMaze.print_maze()
	
path = [] #the 'stack' of cells through which the generator moves

entry = ' '

while entry != 'x':
	entry = raw_input(
	"Generate New Maze('n') <> Exit <'x'>")
	
	if entry == 'n':
		#change the maze size here!
		WIDTH = randint(10, 25)	#number of cells wide
		HEIGHT = randint(8, 20) #number of cells tall
		maze = make_cells()
		myMaze = Maze(maze)		
		start = myMaze.set_start()
		myMaze.generate_maze(start)
		myMaze.print_maze()

	elif entry == 'x':
		break
	else:
		print "What?"