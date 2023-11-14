from __future__ import annotations
import pygame
from Global import IMAGES_OF_BLOCKS


class BlockBrick:
	def __init__(
		self: BlockBrick,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		size: int
	) -> None:

		"""
		Инициализация блока кирпича
		:param parent_x: x
		:param parent_y: y
		:param list_of_objects: массив блоков и танков
		:param size: размер блока
		"""

		list_of_objects.append(self)
		self.type = 'block'
		self.rect = pygame.Rect(parent_x, parent_y, size, size)

	def update(
		self: BlockBrick,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		"""
		Создано для предотвращения ошибки, ничего не выполняет
		:param list_of_keys: массив клавиш управления танком
		:param list_of_objects: массив блоков и танков
		:param list_of_bullets: массив снарядов
		:return: None
		"""

		pass

	def draw(
		self: BlockBrick,
		screen: pygame.Surface
	) -> None:

		"""
		Отображает себя
		:param screen: экран
		:return: None
		"""

		screen.blit(IMAGES_OF_BLOCKS[1], self.rect)


class BlockWater:
	def __init__(
		self: BlockWater,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		size: int
	) -> None:

		"""
		Инициализация блока воды
		:param parent_x: x
		:param parent_y: y
		:param list_of_objects: массив блоков и танков
		:param size: размер блока
		"""

		list_of_objects.append(self)
		self.type = 'water'
		self.rect = pygame.Rect(parent_x, parent_y, size, size)

	def update(
		self: BlockWater,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		"""
		Создано для предотвращения ошибки, ничего не выполняет
		:param list_of_keys: массив клавиш управления танком
		:param list_of_objects: массив блоков и танков
		:param list_of_bullets: массив снарядов
		:return: None
		"""

		pass

	def draw(
		self: BlockWater,
		screen
	) -> None:

		"""
		Отображает себя
		:param screen: экран
		:return: None
		"""

		screen.blit(IMAGES_OF_BLOCKS[3], self.rect)


class BlockArmor:
	def __init__(
		self: BlockArmor,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		size: int
	) -> None:

		"""
		Инициализация блока брони
		:param parent_x: x
		:param parent_y: y
		:param list_of_objects: массив блоков и танков
		:param size: размер блока
		"""

		list_of_objects.append(self)
		self.type = 'armor'
		self.rect = pygame.Rect(parent_x, parent_y, size, size)

	def update(
		self: BlockArmor,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		"""
		Создано для предотвращения ошибки, ничего не выполняет
		:param list_of_keys: массив клавиш управления танком
		:param list_of_objects: массив блоков и танков
		:param list_of_bullets: массив снарядов
		:return: None
		"""

		pass

	def draw(
		self: BlockArmor,
		screen: pygame.Surface
	) -> None:

		"""
		Отображает себя
		:param screen: экран
		:return: None
		"""

		screen.blit(IMAGES_OF_BLOCKS[0], self.rect)


class BlockBushes:
	def __init__(
		self: BlockBushes,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		size: int
	) -> None:

		"""
		Инициализация блока кустов
		:param parent_x: x
		:param parent_y: y
		:param list_of_objects: массив блоков и танков
		:param size: размер блока
		"""

		list_of_objects.append(self)
		self.type = 'bushes'
		self.rect = pygame.Rect(parent_x, parent_y, size, size)

	def update(
		self: BlockBushes,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		"""
		Создано для предотвращения ошибки, ничего не выполняет
		:param list_of_keys: массив клавиш управления танком
		:param list_of_objects: массив блоков и танков
		:param list_of_bullets: массив снарядов
		:return: None
		"""

		pass

	def draw(
		self: BlockBushes,
		screen: pygame.Surface
	) -> None:

		"""
		Отображает себя
		:param screen: экран
		:return: None
		"""

		screen.blit(IMAGES_OF_BLOCKS[2], self.rect)
