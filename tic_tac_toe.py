import pygame as pg, sys
from pygame.locals import *
import time

# Begin with global variables
XO = "x"
winner = None
draw = False
width = 400
height = 400
white = (255, 255, 255)
line_color = (10, 10, 10)

# Make the board for the game of 3x3
TTT = [[None] * 3, [None] * 3, [None] * 3]

# Init the pygame window
pg.init()
fps = 30
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height + 100), 0, 32)
pg.display.set_caption("Tic Tac Toe")



