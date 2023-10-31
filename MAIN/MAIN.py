import pygame
from PLAYING.PLAYING import game
from GLOBAL.GLOB import OBJECTS, BULLETS, WIN_FLAG, WINDOW, SCORE, SCORE_RED, SCORE_BLUE


if __name__ == '__main__':
	game(OBJECTS, BULLETS, WIN_FLAG, WINDOW, SCORE, SCORE_RED, SCORE_BLUE)
	pygame.quit()
