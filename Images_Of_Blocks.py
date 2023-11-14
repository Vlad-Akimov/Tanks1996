import sys
import pygame
import time
from random import randint
from Global import IMAGES_OF_BLOCKS, IMAGES_OF_BANGS, IMAGE_OF_BLUE_TANK, IMAGE_OF_RED_TANK, IMAGE_OF_INTRO_TANK, CURSOR


def images(
	screen: pygame.Surface,
	score: int
) -> None:

	"""
	Отображает все картинки, используемые в игре
	:param screen: экран
	:param score: флаг количества заходов на главный экран
	:return: None
	"""

	screen.fill('black')

	font = pygame.font.Font(None, 60)

	text_exit = font.render('   Escape  -  Выход', True, (190, 190, 190))
	screen.blit(text_exit, (150, 550))

	pygame.mouse.set_cursor(CURSOR)

	playing = True
	while playing:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sound = pygame.mixer.Sound('sounds/shot.wav')
				sound.set_volume(0.7)
				sound.play()

				time.sleep(0.2)

				pygame.quit()
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					playing = False

		if not pygame.mixer.music.get_busy():
			if score == 0:
				pygame.mixer.music.load('sounds/background_music.mp3')
				pygame.mixer.music.set_volume(0.5)
				pygame.mixer.music.play(-1)

			else:
				pygame.mixer.music.load(f'music/music{str(randint(2, 10))}.mp3')
				pygame.mixer.music.set_volume(0.8)
				pygame.mixer.music.play()

		screen.blit(IMAGE_OF_INTRO_TANK, (288, 30))
		screen.blit(IMAGE_OF_BLUE_TANK, (184, 152))
		screen.blit(IMAGE_OF_RED_TANK, (584, 152))
		screen.blit(IMAGES_OF_BANGS[0], (152, 304))
		screen.blit(IMAGES_OF_BANGS[1], (383, 304))
		screen.blit(IMAGES_OF_BANGS[2], (630, 304))
		screen.blit(IMAGES_OF_BLOCKS[0], (100, 456))
		screen.blit(IMAGES_OF_BLOCKS[1], (300, 456))
		screen.blit(IMAGES_OF_BLOCKS[2], (500, 456))
		screen.blit(IMAGES_OF_BLOCKS[3], (700, 456))

		pygame.display.update()

	sound = pygame.mixer.Sound('sounds/shot.wav')
	sound.set_volume(0.7)
	sound.play()
