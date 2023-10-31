import sys
import pygame
import time
from DRAW_INTRO.DRAW_INTRO import draw_intro
from UI.UI import UI
from GLOBAL.GLOB import FPS, CLOCK


"""
цикл процесса игры, с вызовом определённых методов, в определённые моменты
"""


def game(
	list_of_objects: list,
	list_of_bullets: list,
	flag_of_win: bool,
	screen: pygame.Surface,
	score: int,
	score_of_red: int,
	score_of_blue: int
) -> None:

	flag_of_full_win = True

	score, score_of_red,  score_of_blue,  list_of_objects \
		= draw_intro(list_of_objects, screen, score, score_of_red, score_of_blue, flag_of_full_win)

	ui = UI()

	paused = False
	play = True
	while play:

		pygame.mouse.set_visible(False)

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.mixer.music.load('../sounds/finish.mp3')
				pygame.mixer.music.set_volume(0.9)
				pygame.mixer.music.play()

				time.sleep(2)

				pygame.quit()
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					flag_of_full_win = True
					paused = False

					pygame.mixer.music.load('../sounds/finish.mp3')
					pygame.mixer.music.set_volume(0.9)
					pygame.mixer.music.play()

					time.sleep(2)

					score_of_red, score_of_blue = 0, 0
					list_of_bullets, list_of_objects = list(), list()

					screen.fill('black')

					pygame.mixer.music.stop()

					score, score_of_red, score_of_blue, list_of_objects\
						= draw_intro(list_of_objects, screen, score, score_of_red, score_of_blue, flag_of_full_win)

					ui = UI()

				elif event.key == pygame.K_RETURN:
					f = pygame.font.Font(None, 64)

					text_blue = f.render(f'Синий:{score_of_blue}', True, 'black')
					text_red = f.render(f'Красный:{score_of_red}', True, 'black')
					text_pause = f.render('Пауза', True, 'black')

					pygame.draw.rect(screen, (230, 230, 230), (275, 175, 250, 250))

					radius1 = text_blue.get_rect(center=(370, 300))
					radius2 = text_red.get_rect(center=(400, 360))
					radius3 = text_pause.get_rect(center=(390, 200))

					screen.blit(text_blue, radius1)
					screen.blit(text_red, radius2)
					screen.blit(text_pause, radius3)

					pygame.display.update()

					if paused:
						paused = False
					else:
						paused = True

		if not paused:
			keys = pygame.key.get_pressed()
			for _object in list_of_objects:
				_object.update(keys, list_of_objects, list_of_bullets)
			for bullet in list_of_bullets:
				flag_of_win = bullet.update(list_of_objects, list_of_bullets)

			screen.fill('black')

			"""
			создание одного списка объектов, вместо двух для более правильной отрисовки объектов,
			таким образом: сначала отображаются танки и вода, потом снаряды, после этого, оставшееся;
			это необходимо для того, чтобы снаряды проходили "над" танками и водой, 
											но "под" кустами, и остальными блоками
			"""

			list_1 = list_of_objects[:2]
			list_2 = list_of_objects[2:21]
			list_3 = list_of_bullets
			list_4 = list_of_objects[21:]

			list_result = list()
			list_result.extend(list_2)
			list_result.extend(list_3)
			list_result.extend(list_1)
			list_result.extend(list_4)

			for _object in list_result:
				_object.draw(screen)

			paused, score_of_blue, score_of_red, flag_of_full_win\
				= ui.draw(list_of_objects, flag_of_win, score_of_red, score_of_blue)

			pygame.display.update()

		CLOCK.tick(FPS)

		if not pygame.mixer.music.get_busy():
			pygame.mixer.music.load('../sounds/background_music.mp3')
			pygame.mixer.music.set_volume(0.3)
			pygame.mixer.music.play(-1)

		if flag_of_win:
			flag_of_win = False
			paused = False

			time.sleep(0.5)

			pygame.mixer.music.load('../sounds/finish.mp3')
			pygame.mixer.music.set_volume(0.9)
			pygame.mixer.music.play()

			time.sleep(2)

			list_of_bullets, list_of_objects = list(), list()

			screen.fill('black')

			pygame.mixer.music.stop()

			score, score_of_red, score_of_blue, list_of_objects\
				= draw_intro(list_of_objects, screen, score, score_of_red, score_of_blue, flag_of_full_win)

			ui = UI()
