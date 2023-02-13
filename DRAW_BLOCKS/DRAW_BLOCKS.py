import pygame

from random import randint

from TANK.TANK import Tank

from GLOBAL.GLOB import\
	IMAGE_OF_BLUE_TANK, \
	IMAGE_OF_RED_TANK, \
	WIDTH, \
	HEIGHT, \
	TILE

from BLOCKS.BLOCKS import\
	BlockBrick, \
	BlockWater, \
	BlockArmor, \
	BlockBushes

"""

вызывается в draw_blocks()

создаёт:

	синий танк
	
	красный танк
	
	20 блоков:
	    
	    воды
	    
	    брони
	
	50 блоков кирпича
	
	30 блоков кустов

"""


def draw_blocks(
	list_of_objects: list
) -> None:

	Tank(
		'blue',

		100,
		50,

		2,

		(
			pygame.K_a,
			pygame.K_d,
			pygame.K_w,
			pygame.K_s,
			pygame.K_q
		),

		IMAGE_OF_BLUE_TANK,

		list_of_objects,
	)

	Tank(
		'red',

		650,
		500,

		0,

		(
			pygame.K_LEFT,
			pygame.K_RIGHT,
			pygame.K_UP,
			pygame.K_DOWN,
			pygame.K_m
		),

		IMAGE_OF_RED_TANK,

		list_of_objects,
	)

	for _ in range(20):

		while True:

			while True:

				x = randint(
					0,
					WIDTH // TILE
				) * TILE

				if x != 96 and\
					x != 640:

					break

			while True:

				y = randint(
					0,
					HEIGHT // TILE
				) * TILE

				if y != 64 and \
					y != 512:

					break

			rect = pygame.Rect(
				x,
				y,

				TILE,
				TILE
			)

			fined = False

			for _object in list_of_objects:
				if rect.colliderect(
					_object.rect
				):

					fined = True

			if not fined:
				break

		BlockWater(
			x,
			y,

			list_of_objects,

			TILE
		)

	for _ in range(20):

		while True:

			while True:

				x = randint(
					0,
					WIDTH // TILE
				) * TILE

				if x != 96 and \
					x != 640:

					break

			while True:

				y = randint(
					0,
					HEIGHT // TILE
				) * TILE

				if y != 64 and \
					y != 512:

					break

			rect = pygame.Rect(
				x,
				y,

				TILE,
				TILE
			)

			fined = False

			for _object in list_of_objects:
				if rect.colliderect(
					_object.rect
				):

					fined = True

			if not fined:
				break

		BlockArmor(
			x,
			y,

			list_of_objects,

			TILE
		)

	for _ in range(50):

		while True:

			x = randint(
				0,
				WIDTH // TILE
			) * TILE

			y = randint(
				0,
				HEIGHT // TILE
			) * TILE

			rect = pygame.Rect(
				x,
				y,

				TILE,
				TILE
			)

			fined = False

			for _object in list_of_objects:
				if rect.colliderect(
					_object.rect
				):

					fined = True

			if not fined:
				break

		BlockBrick(
			x,
			y,

			list_of_objects,

			TILE
		)

	for _ in range(30):

		while True:

			x = randint(
				0,
				WIDTH // TILE
			) * TILE

			y = randint(
				0,
				HEIGHT // TILE
			) * TILE

			rect = pygame.Rect(
				x,
				y,

				TILE,
				TILE
			)

			fined = False

			for _object in list_of_objects:
				if rect.colliderect(
					_object.rect
				):

					fined = True

			if not fined:
				break

		BlockBushes(
			x,
			y,

			list_of_objects,

			TILE
		)
