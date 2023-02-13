from __future__ import annotations

import pygame

from GLOBAL.GLOB import IMAGES_OF_BLOCKS


"""

==========

класс BlockBrick:

	работа с блоков "кирпича"

----------

init():

----------

добавляет "себя" в список объектов классов

создаёт переменные:
	
	о своём типе
	
	pygame.Rect с:
		
		местоположением
		
		размером

используется в draw_blocks

----------

update():

----------

ничего не происходит

используется в PLAYING ( game )

----------

draw():

----------

отрисовка себя

используется в PLAYING ( game )

==========

"""


class BlockBrick:
	def __init__(
		self: BlockBrick,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		size: int
	) -> None:

		list_of_objects.append(
			self
		)
		self.type = 'block'

		self.rect = pygame.Rect(
			parent_x,
			parent_y,

			size,
			size
		)

	def update(
		self: BlockBrick,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		pass

	def draw(
		self: BlockBrick,
		screen: pygame.Surface
	) -> None:

		screen.blit(
			IMAGES_OF_BLOCKS[
				1
			],
			self.rect
		)


"""

==========

класс BlockWater:

	работа с блоков "воды"

----------

init():

----------

добавляет "себя" в список объектов классов

создаёт переменные:
	
	о своём типе
	
	pygame.Rect с:
		
		местоположением
		
		размером

используется в draw_blocks

----------

update():

----------

ничего не происходит

используется в PLAYING ( game )

----------

draw():

----------

отрисовка себя

используется в PLAYING ( game )

==========

"""


class BlockWater:
	def __init__(
		self: BlockWater,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		size: int
	) -> None:

		list_of_objects.append(
			self
		)
		self.type = 'water'

		self.rect = pygame.Rect(
			parent_x,
			parent_y,

			size,
			size
		)

	def update(
		self: BlockWater,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		pass

	def draw(
		self: BlockWater,
		screen
	) -> None:

		screen.blit(
			IMAGES_OF_BLOCKS[
				3
			],
			self.rect
		)


"""

==========

класс BlockArmor:

	работа с блоков "брони"

----------

init():

----------

добавляет "себя" в список объектов классов

создаёт переменные:
	
	о своём типе
	
	pygame.Rect с:
		
		местоположением
		
		размером

используется в draw_blocks

----------

update():

----------

ничего не происходит

используется в PLAYING ( game )

----------

draw():

----------

отрисовка себя

используется в PLAYING ( game )

==========

"""


class BlockArmor:
	def __init__(
		self: BlockArmor,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		size: int
	) -> None:

		list_of_objects.append(
			self
		)
		self.type = 'armor'

		self.rect = pygame.Rect(
			parent_x,
			parent_y,

			size,
			size
		)

	def update(
		self: BlockArmor,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		pass

	def draw(
		self: BlockArmor,
		screen: pygame.Surface
	) -> None:

		screen.blit(
			IMAGES_OF_BLOCKS[
				0
			],
			self.rect
		)


"""

==========

класс BlockBushes:

	работа с блоков "кустов"

----------

init():

----------

добавляет "себя" в список объектов классов

создаёт переменные:
	
	о своём типе
	
	pygame.Rect с:
		
		местоположением
		
		размером

используется в draw_blocks

----------

update():

----------

ничего не происходит

используется в PLAYING ( game )

----------

draw():

----------

отрисовка себя

используется в PLAYING ( game )

==========

"""


class BlockBushes:
	def __init__(
		self: BlockBushes,
		parent_x: int,
		parent_y: int,
		list_of_objects: list,
		size: int
	) -> None:

		list_of_objects.append(
			self
		)
		self.type = 'bushes'

		self.rect = pygame.Rect(
			parent_x,
			parent_y,

			size,
			size
		)

	def update(
		self: BlockBushes,
		list_of_keys: list,
		list_of_objects: list,
		list_of_bullets: list
	) -> None:

		pass

	def draw(
		self: BlockBushes,
		screen: pygame.Surface
	) -> None:

		screen.blit(
			IMAGES_OF_BLOCKS[
				2
			],
			self.rect
		)
