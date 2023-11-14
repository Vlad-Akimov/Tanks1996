from __future__ import annotations
import pygame
from Global import IMAGES_OF_BANGS


class Bang:
	def __init__(
		self: Bang,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		type_of_object: str
	) -> None:

		"""
		Обрабатывает взрывы
		:param parent_x: x
		:param parent_y: y
		:param list_of_objects: массив блоков и танков
		:param type_of_object: тип объекта
		"""

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

		"""
		Обрабатывает попадания по блокам
		:param list_of_keys: массив клавиш управления танком
		:param list_of_objects: массив блоков и танков
		:param list_of_bullets: массив снарядов
		:return: None
		"""

		if self.timer == 0:
			if self.other_type == 'block':
				sound = pygame.mixer.Sound('sounds/shot_block2.0.mp3')
				sound.set_volume(0.3)
				sound.play()

				sound1 = pygame.mixer.Sound('sounds/shot_block.mp3')
				sound1.set_volume(0.9)
				sound1.play()
			elif self.other_type == 'armor':
				sound = pygame.mixer.Sound('sounds/ricochet.mp3')
				sound.set_volume(0.2)
				sound.play()

				sound1 = pygame.mixer.Sound('sounds/shot_armor.mp3')
				sound1.set_volume(0.9)
				sound1.play()

		self.timer += 0.4

		if self.timer >= 3:
			list_of_objects.remove(self)

	def draw(
		self: Bang,
		screen: pygame.Surface
	) -> None:

		"""
		Отображает картинку в месте соприкосновения снаряда и блока
		:param screen: экран
		:return: None
		"""

		image = IMAGES_OF_BANGS[int(self.timer)]
		rect = image.get_rect(center=(self.parent_x, self.parent_y))
		screen.blit(image, rect)
