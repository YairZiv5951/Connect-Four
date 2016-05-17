import pygame

#Connect Four Game

#Colors
_WHITE = (255, 255, 255)
_BLACK = (0, 0, 0)
_RED = (255, 0, 0)
_BLUE = (0, 0, 255)
_YELLOW = (255, 255, 0)


#Variables
board_size = (7 * 100 + 10, 7 * 100 + 5)
board_line_width = 5
board_space_size = 100


#Board init
pygame.init()
gameDisplay = pygame.display.set_mode(board_size)
gameDisplay.fill(_WHITE)
pygame.display.set_caption("Connect Four")
pygame.display.update()


#Functions
#Draws the horizontal board lines
def draw_horizontal_lines_and_borders(board_size):
	size = board_size[0] - 105
	for i in range(8):
		if i == 0:
			pygame.draw.rect(gameDisplay, _BLUE, [0, 100, board_line_width, size])
		else:
			pygame.draw.rect(gameDisplay, _BLUE, [i * board_space_size + 5, 100, board_line_width, size])




#Draws the entire board, combines all board drawing functions
def draw_entire_board(board_size):
	pass



#Main logic of the game
def run(board_size):
	game_exit = False
	while not game_exit:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				game_exit = True

		draw_horizontal_lines_and_borders(board_size)
		pygame.display.update()

run(board_size)