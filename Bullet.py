from __future__ import annotations
import pygame
from Bang import Bang
from Global import WIDTH, HEIGHT, WINDOW


class Bullet:
	def __init__(
		self: Bullet,
		parent,  # :Tank
		parent_x: int,
		parent_y: int,
		vector_x: int,
		vector_y: int,
		color: str,
		list_of_bullets: list
	) -> None:

		"""
		Создание переменных-характеристик снарядов
		:param parent: Танк, которому принадлежит снаряд
		:param parent_x: x
		:param parent_y: y
		:param vector_x: направление по x
		:param vector_y: направление по y
		:param color: цвет
		:param list_of_bullets: массив снарядов
		"""

		sound = pygame.mixer.Sound('sounds/tank_shot.mp3')
		sound.set_volume(0.4)
		sound.play()

		list_of_bullets.append(self)

		self.parent = parent
		self.parent_x = parent_x
		self.parent_y = parent_y

		self.vector_x = vector_x
		self.vector_y = vector_y

		self.color = color
		self.count = 16
		self.flag = True

	def update(
		self: Bullet,
		list_of_objects: list,
		list_of_bullets: list
	) -> bool:

		"""
		Обновления снарядов
		:param list_of_objects: массив блоков и танков
		:param list_of_bullets: массив снарядов
		:return: flag_of_win: флаг, означающий победу в бою
		"""

		flag_of_win = False

		self.parent_x += self.vector_x
		self.parent_y += self.vector_y

		if self.parent_x < 0 or self.parent_x > WIDTH or self.parent_y < 0 or self.parent_y > HEIGHT:
			list_of_bullets.remove(self)
			Bang(self.parent_x, self.parent_y, list_of_objects, 'armor').draw(WINDOW)

		else:
			for _object in list_of_objects:
				if _object != self.parent and _object.type != 'bang':
					if _object.rect.collidepoint(self.parent_x, self.parent_y):
						if _object.type != 'water' and _object.type != 'bushes':
							if _object.type == 'block':
								list_of_objects.remove(_object)

							list_of_bullets.remove(self)
							Bang(self.parent_x, self.parent_y, list_of_objects, _object.type).draw(WINDOW)
							if _object.type == 'tank':
								flag_of_win = _object.damage(list_of_objects)
		return flag_of_win

	def draw(
		self: Bullet,
		screen: pygame.Surface
	) -> None:

		"""
		Отображает выстрел и полёт снаряда
		:param screen: экран
		:return: None
		"""

		if self.count != 0:
			pygame.draw.circle(
				screen, (255, 165, 0), (self.parent_x + 2 * self.vector_x, self.parent_y + 2 * self.vector_y), self.count
			)
			self.count -= 2

		if not self.flag:
			pygame.draw.circle(
				screen, (255, 165, 0), (self.parent_x - self.vector_x, self.parent_y - self.vector_y), 3
			)
			pygame.draw.circle(
				screen, (255, 215, 0), (self.parent_x - 2 * self.vector_x, self.parent_y - 2 * self.vector_y), 2
			)

		pygame.draw.circle(screen, self.color, (self.parent_x, self.parent_y), 4)
		self.flag = False
