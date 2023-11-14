from __future__ import annotations
import pygame
from Global import WINDOW


class UI:
	def __init__(
		self: UI
	) -> None:

		"""
		Воспроизведение мелодии в начале боя
		"""

		pygame.mixer.music.load('sounds/start.mp3')
		pygame.mixer.music.set_volume(0.6)
		pygame.mixer.music.play()

	def draw(
		self: UI,
		list_of_objects: list,
		flag_of_win: bool,
		score_of_red: int,
		score_of_blue: int,
	) -> tuple[bool, int, int, bool]:

		"""
		Отрисовка счёта после победы одного из участников
		:param list_of_objects: массив блоков и танков
		:param flag_of_win: флаг, означающий победу в бою
		:param score_of_red: счётчик побед красного
		:param score_of_blue: счётчик побед синего
		:return: paused, score_of_blue, score_of_red, flag_of_full_win: флаг(стоит ли игра на паузе),
																		счётчик побед синего,
																		счётчик побед красного,
																		флаг победы в матче (5 побед с одной из сторон)
		"""

		flag_of_full_win = False
		paused = False
		if flag_of_win:
			for _object in list_of_objects:
				if _object.type == 'tank':
					if _object.color == 'blue':
						score_of_blue += 1
					else:
						score_of_red += 1

					if score_of_red == 5 or score_of_blue == 5:
						if score_of_red != score_of_blue:
							pygame.draw.rect(WINDOW, _object.color, (275, 175, 250, 250))
							font = pygame.font.Font(None, 64)
							text_of_win = font.render('Победил', True, 'black')

							if _object.color == 'blue':
								text_of_color = font.render('синий', True, 'black')
							else:
								text_of_color = font.render('красный', True, 'black')

							rect1 = text_of_win.get_rect(center=(400, 280))
							rect2 = text_of_color.get_rect(center=(400, 320))
							WINDOW.blit(text_of_win, rect1)
							WINDOW.blit(text_of_color, rect2)
						else:
							pygame.draw.rect(WINDOW, _object.color, (275, 175, 250, 250))
							font = pygame.font.Font(None, 64)
							text_of_win = font.render('Ничья', True, 'black')
							rect1 = text_of_win.get_rect(center=(410, 290))
							WINDOW.blit(text_of_win, rect1)

						flag_of_full_win = True
					else:
						font = pygame.font.Font(None, 64)
						text_of_win = font.render(f'Синий:{score_of_blue}', True, 'black')
						text_of_color = font.render(f'Красный:{score_of_red}', True, 'black')
						pygame.draw.rect(WINDOW, _object.color, (275, 175, 250, 250))
						rect1 = text_of_win.get_rect(center=(370, 280))
						rect2 = text_of_color.get_rect(center=(400, 320))
						WINDOW.blit(text_of_win, rect1)
						WINDOW.blit(text_of_color, rect2)

					paused = False
		return paused, score_of_blue, score_of_red, flag_of_full_win
