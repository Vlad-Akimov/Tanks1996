from __future__ import annotations

import pygame

from GLOBAL.GLOB import\
	IMAGES_OF_BANGS


"""
==========
Класс Bang: работа со "взрывами"
----------
init(): вызывается из класса Bullet, при соприкосновении определённых объектов,
			добавляет "себя" в список объектов классов,
			создаёт переменные: о своём месте положения;
								информации (своём типе (bang); типе объекта, с которым столкнулся снаряд);
								таймер, отвечающий за условия: проигрывать ли звуки, какую картинку отображать
----------
update(): вызывается из PLAYING, 
			устанавливает определённую мелодию, 
			увеличивает значение таймера на 0.4, 
			удаляет "себя" из списка объектов классов
----------
draw(): вызывается из: класса Bullet, PLAYING; 
		отображает определённую картинку из списка картинок "взрывов" в месте, переданном в init()
==========
"""


class Bang:
	def __init__(
		self: Bang,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		type_of_object: str
	) -> None:

		list_of_objects.append(self)

		self.type = 'bang'
		self.other_type = type_of_object

		self.parent_x = parent_x
		self.parent_y = parent_y

		self.timer = 0

	def update(
		self: Bang,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		if self.timer == 0:
			if self.other_type == 'block':
				sound = pygame.mixer.Sound('../sounds/shot_block2.0.mp3')
				sound.set_volume(0.3)
				sound.play()

				sound1 = pygame.mixer.Sound('../sounds/shot_block.mp3')
				sound1.set_volume(0.9)
				sound1.play()
			elif self.other_type == 'armor':
				sound = pygame.mixer.Sound('../sounds/ricochet.mp3')
				sound.set_volume(0.2)
				sound.play()

				sound1 = pygame.mixer.Sound('../sounds/shot_armor.mp3')
				sound1.set_volume(0.9)
				sound1.play()

		self.timer += 0.4

		if self.timer >= 3:
			list_of_objects.remove(self)

	def draw(
		self: Bang,
		screen: pygame.Surface
	) -> None:

		image = IMAGES_OF_BANGS[int(self.timer)]
		rect = image.get_rect(center=(self.parent_x, self.parent_y))
		screen.blit(image, rect)
