import sys

import pygame
import time

from random import randint

from GLOBAL.GLOB import CURSOR


"""

вызывается в draw_intro

отрисовка инструкции
	по управлению танками

"""


def rules(
	screen: pygame.Surface,
	score: int
) -> None:

	pygame.mouse.set_cursor(
		CURSOR
	)

	"""
	
	подготовка экрана,
		с последующим созданием переменных,
			в которых заложен необходимые размер и
										  тексты
		и отображением их на экране
	
	"""

	screen.fill(
		'black'
	)

	font = pygame.font.Font(
		None,
		60
	)

	text_q = font.render(
		'Q  -  Стрелять',
		True,

		(
			0,
			0,
			190
		)
	)

	text_w = font.render(
		'W  -  Вперёд',
		True,

		(
			0,
			0,
			190
		)
	)

	text_a = font.render(
		'A   -  Налево',
		True,

		(
			0,
			0,
			190
		)
	)

	text_s = font.render(
		'S   -  Назад',
		True,

		(
			0,
			0,
			190
		)
	)

	text_d = font.render(
		'D   -  Направо',
		True,

		(
			0,
			0,
			190
		)
	)

	text_m = font.render(
		'M  -  Стрелять',
		True,

		(
			190,
			0,
			0
		)
	)

	text_up0 = font.render(
		'^',
		True,

		(
			190,
			0,
			0
		)
	)

	text_up1 = font.render(
		'|    -  Вперёд',
		True,

		(
			190,
			0,
			0
		)
	)

	text_left = font.render(
		'<-  -  Налево',
		True,

		(
			190,
			0,
			0
		)
	)

	text_down0 = font.render(
		'|    -  Назад',
		True,

		(
			190,
			0,
			0
		)
	)

	text_down1 = font.render(
		'v',
		True,

		(
			190,
			0,
			0
		)
	)

	text_right = font.render(
		'->  -  Направо',
		True,

		(
			190,
			0,
			0
		)
	)

	text_exit = font.render(
		'   Escape  -  Выход',
		True,

		(
			190,
			190,
			190
		)
	)

	screen.blit(
		text_exit,

		(
			50,
			550
		)
	)

	screen.blit(
		text_q,

		(
			50,
			50
		)
	)

	screen.blit(
		text_w,

		(
			50,
			130
		)
	)

	screen.blit(
		text_a,

		(
			50,
			200
		)
	)

	screen.blit(
		text_s,

		(
			50,
			280
		)
	)

	screen.blit(
		text_d,

		(
			50,
			350
		)
	)

	screen.blit(
		text_m,

		(
			450,
			50
		)
	)

	screen.blit(
		text_up0,

		(
			450,
			120
		)
	)

	screen.blit(
		text_up1,

		(
			456,
			130
		)
	)

	screen.blit(
		text_left,

		(
			450,
			200
		)
	)

	screen.blit(
		text_down0,

		(
			456,
			270
		)
	)

	screen.blit(
		text_down1,

		(
			450,
			280
		)
	)

	screen.blit(
		text_right,

		(
			450,
			350
		)
	)

	"""
	
	игровой цикл с
		возможностью закрыть окно,
		выйти на предыдущий экран
						( draw_intro() )
		установить определённую музыку,
			в зависимости от:
			
			    значения переменной score
			     
				"занятости" mixer.music
	
	"""

	start_flag = True
	while start_flag:

		for event in pygame.event.get():
			if event.type == pygame.QUIT:

				sound = pygame.mixer.Sound(
					'../sounds/shot.wav'
				)
				sound.set_volume(
					0.7
				)
				sound.play()

				time.sleep(
					0.2
				)

				pygame.quit()
				sys.exit()

			elif event.type == pygame.KEYDOWN:
				if event.key == pygame.K_ESCAPE:

					start_flag = False

		if not pygame.mixer.music.get_busy():
			if score == 0:

				pygame.mixer.music.load(
					'../sounds/background_music.mp3'
				)

				pygame.mixer.music.set_volume(
					0.5
				)
				pygame.mixer.music.play(
					-1
				)

			else:

				pygame.mixer.music.load(
					f'../music/music{str(randint(2, 10))}.mp3'
				)

				pygame.mixer.music.set_volume(
					0.8
				)
				pygame.mixer.music.play()

		pygame.display.update()

	sound = pygame.mixer.Sound(
		'../sounds/shot.wav'
	)
	sound.set_volume(
		0.7
	)
	sound.play()
