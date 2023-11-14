import pygame
from Playing import game
from Global import OBJECTS, BULLETS, WIN_FLAG, WINDOW, SCORE, SCORE_RED, SCORE_BLUE


if __name__ == '__main__':
	game(OBJECTS, BULLETS, WIN_FLAG, WINDOW, SCORE, SCORE_RED, SCORE_BLUE)
	pygame.quit()
